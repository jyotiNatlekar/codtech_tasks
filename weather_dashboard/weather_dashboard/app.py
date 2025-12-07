"""Flask Weather Dashboard - Backend
- Provides web UI, API endpoint, and stores search history in SQLite.
- Replace OPENWEATHER_API_KEY with your API key or set it as an environment variable.
"""
import os
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, g, jsonify, flash
import requests

# ----- Configuration -----
DATABASE = os.path.join(os.path.dirname(__file__), 'weather.db')

# Prefer environment variable for API key; fallback to placeholder.
OPENWEATHER_API_KEY = os.environ.get('Default','879b2cc8a8aeb9365f090108423cde03')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET', 'dev-secret-change-me')

# ----- Database helpers -----
def get_db():
    """Return a database connection, creating the DB if needed."""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def init_db():
    """Create the searches table if not exists."""
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS searches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT NOT NULL,
                temp REAL,
                description TEXT,
                humidity INTEGER,
                wind REAL,
                timestamp TEXT NOT NULL
            )
        ''')
        db.commit()

@app.teardown_appcontext
def close_connection(exception):
    """Close DB connection at request end."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# ----- Helper to call OpenWeatherMap -----
def fetch_weather(city):
    """Call OpenWeatherMap API and return parsed data or raise an exception."""
    params = {
        'q': city,
        'appid': OPENWEATHER_API_KEY,
        'units': 'metric'
    }

    resp = requests.get(BASE_URL, params=params, timeout=10)
    data = resp.json()

    if resp.status_code != 200:
        message = data.get('message', 'Unknown error from weather API')
        raise ValueError(message)

    parsed = {
        'city': data.get('name', city).title(),
        'temp': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'wind': data['wind']['speed'],
        'description': data['weather'][0]['description'].title(),
        'icon': data['weather'][0]['icon']
    }
    return parsed

# ----- Routes -----
@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    error = None

    if request.method == 'POST':
        city = request.form.get('city', '').strip()

        if not city:
            flash('Please enter a city name.', 'error')
            return redirect(url_for('index'))

        try:
            weather = fetch_weather(city)

            # Save to DB
            db = get_db()
            db.execute('''
                INSERT INTO searches (city, temp, description, humidity, wind, timestamp)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (weather['city'], weather['temp'], weather['description'],
                  weather['humidity'], weather['wind'], datetime.utcnow().isoformat()))
            db.commit()

        except Exception as e:
            error = str(e)

    return render_template('index.html', weather=weather, error=error)

@app.route('/history')
def history():
    db = get_db()
    cur = db.execute('SELECT * FROM searches ORDER BY id DESC LIMIT 100')
    rows = cur.fetchall()
    return render_template('history.html', rows=rows)

@app.route('/delete/<int:row_id>', methods=['POST'])
def delete_entry(row_id):
    db = get_db()
    db.execute('DELETE FROM searches WHERE id = ?', (row_id,))
    db.commit()
    flash('Entry deleted.', 'info')
    return redirect(url_for('history'))

@app.route('/api/weather')
def api_weather():
    city = request.args.get('city', '').strip()

    if not city:
        return jsonify({'error': 'Missing city parameter'}), 400

    try:
        weather = fetch_weather(city)

        # Optionally save to DB
        db = get_db()
        db.execute('''
            INSERT INTO searches (city, temp, description, humidity, wind, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (weather['city'], weather['temp'], weather['description'],
              weather['humidity'], weather['wind'], datetime.utcnow().isoformat()))
        db.commit()

        return jsonify(weather)

    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception:
        return jsonify({'error': 'Failed to fetch weather'}), 500

# ----- Start App -----
if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
