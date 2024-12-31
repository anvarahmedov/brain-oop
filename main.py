import logging
from brain import Brain
from task import Task

# Example Usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

    brain1 = Brain()
    brain2 = Brain()

    # Example task creation and usage
    task1 = Task("Complete Project", "Incomplete", brain1.id)
    brain1.add_task(task1)

    # Routine setting
    brain1.routine_manager.set_routine(task1, brain1.id, "Monday", 10)

    # Friendship example
    brain1.be_friends_with(brain2, status=True)
    print(brain1.is_friends_with(brain2))  # Output: True

