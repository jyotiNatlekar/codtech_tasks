# Weather Dashboard (Flask + SQLite)

This is an end-to-end Weather Dashboard built with Python (Flask) for backend, SQLite for database,
and simple HTML/CSS/JS for frontend. It fetches weather data from OpenWeatherMap and stores search history.

## Features
- Search weather by city (server-rendered form and AJAX API).
- Stores search history in SQLite database (`weather.db`).
- View and delete history entries.

## Setup (VS Code / Local)
1. Clone or unzip the project in VS Code.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set your OpenWeatherMap API key (recommended):
   ```bash
   export OPENWEATHER_API_KEY=your_api_key_here    # macOS/Linux
   set OPENWEATHER_API_KEY=your_api_key_here       # Windows (cmd)
   $env:OPENWEATHER_API_KEY="your_api_key"         # PowerShell
   ```
   Or edit `app.py` and replace `'YOUR_API_KEY_HERE'`.
5. Run the app:
   ```bash
   python app.py
   ```
6. Open http://127.0.0.1:5000 in your browser.

## Files
- `app.py` - Flask backend and DB handling
- `templates/` - HTML templates
- `static/` - CSS and JavaScript
- `requirements.txt` - Python dependencies

## Notes
- This project uses a local SQLite file `weather.db` created automatically.
- For production, do NOT store API keys in source code; use environment variables or a secrets manager.
