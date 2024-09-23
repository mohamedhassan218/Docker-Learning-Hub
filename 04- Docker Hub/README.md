# Docker Hub

## What is Docker Hub?
Docker Hub is a cloud-based repository where you can store, manage, and share Docker container images. It serves as a central platform for Docker users to distribute and access containerized applications. By pushing your images to Docker Hub, you make them accessible from anywhere, allowing others (or yourself) to easily pull and run your applications on any system with Docker installed.

Docker Hub also enables versioning of images, supports public and private repositories, and integrates with CI/CD pipelines for automated builds. It’s a powerful tool for developers looking to streamline the deployment and sharing of containerized applications.

In this lesson, we'll be using Docker Hub to push a simple **Express.js server** image, demonstrating how to upload your projects to the cloud and share them globally.

## Objective
The goal of this lesson is to:
- Create a simple Express.js server.
- Write a `Dockerfile` to containerize the server.
- Build a Docker image locally from the project.
- Push the image to Docker Hub for public access.

## Usage

### Prerequisites
Before proceeding, ensure you have the following installed:
- [Node.js](https://nodejs.org/) (version 16 or later)
- [Docker](https://www.docker.com/get-started)
- A [Docker Hub](https://hub.docker.com/) account.

### Steps

1. **Change your directory to the server path**:
   ```bash
   cd simple-express-server
   ```

2. **Install dependencies:**
   Ensure all dependencies are installed:
   ```bash
   npm install
   ```

3. **Build the Docker Image:**
   - Use the provided `Dockerfile` to build the image:
     ```bash
     docker build -t simple-express-server .
     ```

4. **Run the Docker Container:**
   - Run the image locally to test:
     ```bash
     docker run -p 8080:3000 simple-express-server
     ```
   - Open your browser and go to `http://localhost:8080/` to confirm the server is running.

5. **Push the Image to Docker Hub:**
   - First, log in to Docker:
     ```bash
     docker login -u <user_name> -p <password>
     ```
   - Tag your image:
     ```bash
     docker tag simple-express-server <user_name>/simple-express-server:latest
     ```
   - Push the image to Docker Hub:
     ```bash
     docker push <user_name>/simple-express-server:latest
     ```

6. **Pull the image on any device:**
   - Pull from your Docker Hub repo:
     ```bash
     docker pull <user_name>/simple-express-server:latest
     ```

## Conclusion
This lesson demonstrates the full workflow of building, containerizing, and publishing an Express.js server with Docker. You can reuse this setup for your own applications or extend the server with more features before pushing to Docker Hub.

Feel free to modify the server, Dockerfile, or image settings to suit your learning goals!
