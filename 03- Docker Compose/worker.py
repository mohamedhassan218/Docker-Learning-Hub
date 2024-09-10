import redis
import time

r = redis.Redis(host="redis", port=6379)


def process_task(task):
    print(f"Processing task: {task}")
    time.sleep(2)  # Simulate some work


while True:
    task = r.lpop("task_queue")
    if task:
        process_task(task.decode("utf-8"))
    else:
        print("No tasks in the queue, waiting...")
    time.sleep(1)
