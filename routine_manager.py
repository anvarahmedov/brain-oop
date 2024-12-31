import logging


class RoutineManager:
    def __init__(self):
        self.routine = {}  # Store routine tasks for each weekday/hour

    def set_routine(self, task, brain_id, weekday, hour):
         # Using setdefault to handle routine and weekday initialization
        self.routine.setdefault(brain_id, {}).setdefault(weekday.lower(), {})[hour] = task
        logging.info(f"Routine set: {task.get_title()} on {weekday} at {hour}:00 for Brain ID {brain_id}")

    def get_routine(self, weekday, hour):
        task = self.routine.get(weekday.lower(), {}).get(hour, None)  # Safe access
        if task:
            logging.info(f"Retrieved task: {task.get_title()} on {weekday} at {hour}:00")
        else:
            logging.warning(f"No task found on {weekday} at {hour}:00")
        return task
