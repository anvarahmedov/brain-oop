import logging
from datetime import datetime
import json

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Task:
    _id_counter = 1

    def __init__(self, title, status, brain_id):
        self.id = Task._id_counter
        Task._id_counter += 1
        self.title = title
        self.status = status
        self.brain_id = brain_id
        logging.info(f"Task created: {self.title} with status {self.status}")

    def get_title(self):
        return self.title

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status
        logging.info(f"Task status updated to: {status}")

    def get_brain_id(self):
        return self.brain_id

    def __repr__(self):
        return f"Task({self.title}, {self.status})"


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


class Brain:
    # Class-level variable to track the last assigned id
    _id_counter = 1

    def __init__(self):
        self.id = Brain._id_counter  # Set the current id
        Brain._id_counter += 1  # Increment the id counter for the next Brain instance
        self.features = []
        self.memories = []
        self.emotions = []
        self.personality = []
        self.groups = []
        self.friends = []  # List to store friends
        self.fav_songs = []  # Initialize favorite songs list
        self.tasks = []  # Store tasks related to this brain
        self.routine_manager = RoutineManager()  # Instantiate RoutineManager for this brain
        logging.info(f"Brain instance created with id: {self.id}")

    # Get features
    def get_features(self):
        logging.debug(f"Getting features: {self.features}")
        return self.features

    # Add features
    def set_features(self, features):
        if isinstance(features, list):
            self.features.extend(features)
            logging.info(f"Features added: {features}")
        else:
            raise ValueError("Features should be provided as a list.")

    # Get memories
    def get_memories(self):
        logging.debug(f"Getting memories: {self.memories}")
        return self.memories

    # Add memory
    def add_memory(self, memory):
        self.memories.append(memory)
        logging.info(f"Memory added: {memory}")

    # Update memory
    def update_memory(self, index, memory):
        if 0 <= index < len(self.memories):
            self.memories[index] = memory
            logging.info(f"Memory updated at index {index}: {memory}")
        else:
            raise IndexError("Memory index out of range.")

    # Delete memory
    def delete_memory(self, index):
        if 0 <= index < len(self.memories):
            del self.memories[index]
            logging.info(f"Memory deleted at index {index}")
        else:
            raise IndexError("Memory index out of range.")

    # Get emotions
    def get_emotions(self):
        logging.debug(f"Getting emotions: {self.emotions}")
        return self.emotions

    # Add emotion
    def add_emotion(self, emotion):
        self.emotions.append(emotion)
        logging.info(f"Emotion added: {emotion}")

    # Get personality traits
    def get_personality(self):
        logging.debug(f"Getting personality: {self.personality}")
        return self.personality

    # Add personality trait
    def add_personality(self, trait):
        self.personality.append(trait)
        logging.info(f"Personality trait added: {trait}")

    # Get groups
    def get_groups(self):
        logging.debug(f"Getting groups: {self.groups}")
        return self.groups

    # Join group
    def join_group(self, group):
        self.groups.append(group)
        logging.info(f"Joined group: {group}")

    # Leave group
    def leave_group(self, group):
        if group in self.groups:
            self.groups.remove(group)
            logging.info(f"Left group: {group}")

    # Check friendship
    def is_friends_with(self, other_brain):
        is_friend = other_brain in self.friends
        logging.debug(f"Checking friendship with brain {other_brain.id}: {is_friend}")
        return is_friend

    # Be friends with another brain
    def be_friends_with(self, other_brain, status):
        if status and other_brain not in self.friends:
            self.friends.append(other_brain)
            other_brain.friends.append(self)  # Add reciprocal friendship
            logging.info(f"Made friends with brain {other_brain.id}")
        elif not status and other_brain in self.friends:
            self.friends.remove(other_brain)
            other_brain.friends.remove(self)  # Remove reciprocal friendship
            logging.info(f"Broke friendship with brain {other_brain.id}")


    # Simulate interaction
    def simulate_interaction(self, other_brain):
        shared_features = set(self.features) & set(other_brain.get_features())
        compatibility_score = len(shared_features) * 10  # Each shared feature adds 10 points
        friendship_status = self.is_friends_with(other_brain)
        logging.info(f"Simulated interaction with brain {other_brain.id}: {compatibility_score} compatibility score")
        return {
            "Shared Features": list(shared_features),
            "Compatibility Score": compatibility_score,
            "Friendship Status": friendship_status,
        }

    # Get favorite songs
    def get_fav_songs(self):
        logging.debug(f"Getting favorite songs: {self.fav_songs}")
        return self.fav_songs

    # Add new favorite songs
    def set_fav_songs(self, songs):
        if isinstance(songs, list):
            self.fav_songs.extend(songs)  # Extend the favorite songs list
            logging.info(f"Favorite songs added: {songs}")
        else:
            raise ValueError("Songs should be provided as a list.")

    # Add task
    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)
            logging.info(f"Task added: {task}")
        else:
            raise ValueError("Task should be an instance of the Task class.")

    # Get all tasks
    def get_tasks(self):
        logging.debug(f"Getting tasks: {self.tasks}")
        return self.tasks

# Example Usage
brain1 = Brain()
brain2 = Brain()

# Make friends between brain1 and brain2
brain1.be_friends_with(brain2, status=True)

# Check friendship status
print(brain1.is_friends_with(brain2))  # True
print(brain2.is_friends_with(brain1))  # True

# Break friendship
brain1.be_friends_with(brain2, status=False)

# Check friendship status after breaking the friendship
print(brain1.is_friends_with(brain2))  # False
print(brain2.is_friends_with(brain1))  # False
