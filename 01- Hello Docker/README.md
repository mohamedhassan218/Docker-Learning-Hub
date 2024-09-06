
# Hello Docker

This project is a simple Express.js application that runs inside a Docker container. The application includes two routes:

- `/`: Returns a greeting message.
- `/hello/:name`: Returns a personalized greeting message.

## Project Structure

- `index.js`: The main entry point of the application.
- `package.json`: Contains metadata about the project and its dependencies.
- `Dockerfile`: Defines the Docker image for the application.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [Docker](https://www.docker.com/get-started)
- [Node.js](https://nodejs.org/) (if running locally without Docker)

## Running the Application with Docker

Follow these steps to build and run the application in a Docker container:

### 1. Build the Docker Image

```bash
docker build -t hello-docker .
```

This command builds a Docker image named `hello-docker` based on the instructions in the `Dockerfile`.

### 2. Run the Docker Container

```bash
docker run -p 3000:3000 hello-docker
```

This command runs the Docker container and maps port `3000` on your local machine to port `3000` inside the container.

### 3. Access the Application

Open your browser and navigate to:

- `http://localhost:3000/`: To see the message "Hello from containerized express.js".
- `http://localhost:3000/hello/YourName`: To receive a personalized greeting, e.g., "Hello YourName from containerized express.js".


## Key Dockerfile Instructions

- **`FROM node:lts-alpine`**: Uses a lightweight Node.js image based on Alpine Linux.
- **`WORKDIR /usr/src/app`**: Sets the working directory inside the container.
- `COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]`: Copies necessary files to the container.
- **`RUN npm install --production --silent`**: Installs production dependencies.
- **`EXPOSE 3000`**: Exposes port 3000 to be accessible from the host.
- **`USER node`**: Runs the application as a non-root user for security.
- **`CMD ["node", "index.js"]`**: Specifies the command to run the application.



## Running the Application Locally

If you prefer to run the application locally without Docker:

### 1. Install Dependencies

```bash
npm install
```

### 2. Run the Application

```bash
node index.js
```

### 3. Access the Application

Open your browser and navigate to the same URLs mentioned above.