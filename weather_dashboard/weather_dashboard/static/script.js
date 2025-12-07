// script.js: Simple AJAX to call /api/weather and display result without full page reload.
document.addEventListener('DOMContentLoaded', function () {
    const ajaxBtn = document.getElementById('ajaxBtn');
    const cityInput = document.getElementById('cityInput');

    ajaxBtn?.addEventListener('click', async function () {
        const city = cityInput.value.trim();
        if (!city) {
            alert('Please enter a city name.');
            return;
        }
        try {
            const resp = await fetch('/api/weather?city=' + encodeURIComponent(city));
            const data = await resp.json();
            if (!resp.ok) {
                alert('Error: ' + (data.error || 'Unknown error'));
                return;
            }
            // Build a small result box
            const box = document.querySelector('.weather-box') || document.createElement('div');
            box.className = 'weather-box';
            box.innerHTML = `
                <h2>${data.city}</h2>
                <img src="https://openweathermap.org/img/wn/${data.icon}@2x.png" />
                <p><strong>Temperature:</strong> ${data.temp} °C</p>
                <p><strong>Condition:</strong> ${data.description}</p>
                <p><strong>Humidity:</strong> ${data.humidity}%</p>
                <p><strong>Wind:</strong> ${data.wind} m/s</p>
            `;
            // Insert/replace under the form
            const container = document.querySelector('.container');
            const existing = document.querySelector('.weather-box');
            if (existing) existing.replaceWith(box);
            else container.insertBefore(box, container.querySelector('p'));
        } catch (err) {
            alert('Failed to fetch weather: ' + err.message);
        }
    });
});
