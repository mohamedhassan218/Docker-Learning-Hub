# Weather API Service with Docker Compose

This project demonstrates how to build a simple Flask application that fetches weather data for a city using the OpenWeatherMap API and stores it in MongoDB. The application is containerized using Docker and orchestrated with Docker Compose.

## Prerequisites

- Docker
- Docker Compose
- OpenWeatherMap API Key

## Setup

1. Clone this repository.
2. Navigate to the project directory.
3. Create a `requirements.txt` file with the dependencies.
4. Add your OpenWeatherMap API key in the `app.py` file.

## Running the Project

1. Build and run the containers using Docker Compose:
   ```bash
   docker-compose up --build
   ```

2. The application will be available at http://localhost:5000.

## Usage
To get the weather data for a city, use the following endpoint:

bash
Copy code
http://localhost:5000/weather?city=London
Replace London with any city name.

Stopping the Application
To stop and remove the containers, run:

``` bash
docker-compose down
```

This project uses Python with Flask, MongoDB as a service, and Docker Compose for orchestration. It fetches weather data from the OpenWeatherMap API and stores it in MongoDB, making it a great example of integrating a Python web service with a NoSQL database.
