import redis
from typing import List, Dict, Any
import json
# Refactored parser - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored pipeline - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored scheduler - 2026-03-11
# Refactored middleware - 2026-03-11
# Refactored scraper - 2026-03-11
# Refactored parser - 2026-03-11
# Refactored queue - 2026-03-11
# Refactored parser - 2026-03-11

class TaskQueue:
    """Manages the queue of URLs to be scraped using Redis."""

    def __init__(self, host='localhost', port=6379, db=0):
        self.r = redis.Redis(host=host, port=port, db=db)

    def add_task(self, task: Dict[str, Any]):
        """Add a new task to the queue."""
        self.r.lpush('task_queue', json.dumps(task))

    def get_task(self) -> Dict[str, Any] | None:
        """Get a task from the queue."""
        task = self.r.rpop('task_queue')
        if task:
            return json.loads(task)
        return None

    def task_done(self, task: Dict[str, Any]):
        """Mark a task as done."""
        # In a real system, we might move it to a "completed" set
        # or log it somewhere. For now, we just print.
        print(f"Task completed: {task.get('url')}")

    def queue_size(self) -> int:
        """Return the number of tasks in the queue."""
        return self.r.llen('task_queue')

if __name__ == "__main__":
    # Example usage
    queue = TaskQueue()
    
    # Add some tasks
    queue.add_task({'url': 'https://example.com/page1', 'retries': 0})
    queue.add_task({'url': 'https://example.com/page2', 'retries': 0})

    print(f"Queue size: {queue.queue_size()}")

    # Get a task
    current_task = queue.get_task()
    if current_task:
        print(f"Processing task: {current_task.get('url')}")
        # ... process the task ...
        queue.task_done(current_task)

    print(f"Queue size after processing: {queue.queue_size()}")
