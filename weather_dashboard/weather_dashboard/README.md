# API-INTEGRATION-AND-DATA-VISUALIZATION
# Weather Dashboard (Flask + SQLite)

COMPANY : CODTECH IT SOLUTIONS

NAME : JYOTI VIJAY NATLEKAR

INTERN ID : CT04DR2389

DOMAIN : PYTHON PROGRAMMING

DURATION : 4 WEEKS

MENTOR : NEELA SANTOSH

The Weather Dashboard task was assigned to me during my internship at CodTech IT Solutions under the Python Programming domain. The purpose of this task was to help me understand how to build a complete web application using Python and how real-time data from the internet can be used in practical applications. This task allowed me to work on backend development, database handling, API integration, and basic frontend design in a single project.

The Weather Dashboard is an end-to-end web application that shows real-time weather information for different cities. It is developed using Python with Flask for the backend, SQLite for storing data, and HTML, CSS, and JavaScript for the frontend. The application fetches live weather data from the OpenWeatherMap API, which provides information such as temperature, humidity, and weather conditions.

The main objective of this task was to gain hands-on experience in API integration and full-stack development. Instead of learning concepts only from theory, this task helped me understand how real-world applications are designed and implemented step by step. It also helped me learn how different technologies work together in a single project.

In this Weather Dashboard application, the user can enter the name of any city in the search box. When the user submits the city name, the request is sent to the Flask backend. The backend then sends a request to the OpenWeatherMap API using the provided API key. The API responds with weather data in JSON format. The backend processes this data and sends only the required information to the frontend. The weather details are then displayed on the web page in a simple and easy-to-read format.
One important feature of this project is search history storage. Every time a user searches for a city, the city name and its weather details are stored in an SQLite database. SQLite was chosen because it is lightweight, easy to use, and suitable for small applications. The database file (weather.db) is created automatically when the application runs for the first time. The user can view previously searched cities and also delete any record if required. This helped me understand how data is inserted, read, and deleted from a database.

For the frontend part, I used HTML to design the structure of the web pages and CSS to improve the appearance of the application. JavaScript was used to make the application interactive. I also implemented AJAX, which allows the application to fetch weather data without refreshing the entire page. This improves the speed and user experience of the application.

During the implementation of this task, I learned how to create and manage Flask routes, how to connect Flask with a database, and how to handle API responses properly. I also learned how to use environment variables to store sensitive information like API keys instead of hard-coding them into the source code. This is an important security practice used in real-world projects.

This task helped me learn many important concepts. I learned how APIs work and how Python communicates with external services. I learned how JSON data is handled and converted into usable information. I also gained practical experience with database operations and understood how backend and frontend communicate with each other.

I also improved my problem-solving and debugging skills while working on this project. I learned how to handle errors such as invalid city names, API failures, and database issues. These experiences helped me understand how to make applications more reliable and user-friendly.

In conclusion, the Weather Dashboard task was a very valuable learning experience during my internship at CodTech IT Solutions. It helped me understand full-stack web development in a simple and practical way. This project improved my confidence in Python programming, backend development, and API integration. Overall, the task was successfully completed and provided me with real-world development experience that will be useful for future projects and career growth.

## Notes
- This project uses a local SQLite file `weather.db` created automatically.
- For production, do NOT store API keys in source code; use environment variables or a secrets manager.
