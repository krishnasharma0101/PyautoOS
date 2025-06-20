import logging
from typing import List, Any, Optional

logger = logging.getLogger("pyautoos.tasks")

class Tasks:
    """
    Task chaining, LLM prompt compatibility, and simple automation tasks.
    """
    def __init__(self):
        self.chain = []

    def run_task(self, task: str) -> Any:
        """Run a task by string description (stub for LLM integration)."""
        logger.info(f"Running task: {task}")
        # Placeholder: In future, parse and execute task using LLM
        return f"Executed: {task}"

    def run(self, tasks: List[str]) -> List[Any]:
        """Run a chain of tasks (by description)."""
        results = []
        for task in tasks:
            result = self.run_task(task)
            results.append(result)
        logger.info(f"Ran {len(tasks)} tasks.")
        return results

    def add(self, task: str) -> 'Tasks':
        """Add a task to the chain."""
        self.chain.append(task)
        return self

    def execute(self) -> List[Any]:
        """Execute the chained tasks."""
        results = self.run(self.chain)
        self.chain = []
        return results 