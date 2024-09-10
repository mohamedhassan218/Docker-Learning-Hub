import redis
from flask import Flask, request, jsonify

app = Flask(__name__)
cache = redis.Redis(host="redis", port=6379)


@app.route("/")
def home():
    return "Task Queue System - Add tasks to be processed"


@app.route("/add_task", methods=["POST"])
def add_task():
    task_data = request.json.get("task", "default_task")
    cache.rpush("task_queue", task_data)
    return f"Task '{task_data}' added to the queue.\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
