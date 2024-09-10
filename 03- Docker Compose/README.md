# Docker Compose

## Overview

This project demonstrates a simple **Task Queue System** using Docker Compose with **Flask** and **Redis**. The system is composed of two main components:

- **Flask Application**: This acts as the task producer, allowing users to submit tasks that will be added to a queue.
- **Worker Service**: This service acts as the task consumer, fetching tasks from the Redis queue and processing them.

Redis serves as the **message broker**, managing the task queue between the producer (Flask app) and the consumer (worker service).

### Key Concepts

- **Producer-Consumer Pattern**: In this system, the Flask app produces tasks by adding them to a Redis queue, while a separate worker process consumes and processes the tasks. This decoupling ensures scalability and efficient task handling.
- **Redis as a Message Broker**: Redis is used here to store and manage the task queue. Tasks are pushed to the queue and later consumed and processed by a background worker.
- **Docker Compose**: Docker Compose orchestrates the services involved—setting up the Flask app, Redis server, and the worker service—all in separate containers.

---

## Architecture

### Components:
1. **Flask Application (Producer)**: 
   - Listens for incoming task requests.
   - Adds tasks to the Redis queue for processing.

2. **Redis (Message Broker)**:
   - Stores the tasks in a queue (list) and allows them to be fetched in a first-in, first-out (FIFO) manner.

3. **Worker (Consumer)**:
   - Continuously listens to the Redis queue, picks up tasks, and processes them asynchronously.

---

## How It Works

1 Build and Start Services

To run the project, ensure that you have Docker and Docker Compose installed on your system. Then run the following command:

```bash
docker-compose up --build
```

This will:
- Build the Flask application image.
- Start the Flask application, Redis, and worker service in their respective containers.

### 3. Interacting with the System

Once the services are running, you can interact with the task queue system using postman or any API testing tool.

---

## Conclusion

This system provides a simple yet powerful demonstration of how to use **Docker Compose** to orchestrate multiple services (Flask, Redis, Worker) and implement a **producer-consumer** architecture using Redis as the message broker.

With this setup, tasks can be submitted asynchronously and processed by a dedicated worker service, allowing for better scalability and responsiveness.