from asyncio import Task
import logging
import sqlite3

from routine_manager import RoutineManager

from asyncio import Task


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

    def initialize_db(self):
        """Create the database tables if they do not exist"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS brains (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            features TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS features (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brain_id INTEGER,
            feature TEXT,
            FOREIGN KEY (brain_id) REFERENCES brains(id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brain_id INTEGER,
            memory TEXT,
            FOREIGN KEY (brain_id) REFERENCES brains(id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS emotions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brain_id INTEGER,
            emotion TEXT,
            FOREIGN KEY (brain_id) REFERENCES brains(id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS personalities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brain_id INTEGER,
            personality_trait TEXT,
            FOREIGN KEY (brain_id) REFERENCES brains(id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS friends (
            brain1_id INTEGER,
            brain2_id INTEGER,
            PRIMARY KEY (brain1_id, brain2_id),
            FOREIGN KEY (brain1_id) REFERENCES brains(id),
            FOREIGN KEY (brain2_id) REFERENCES brains(id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brain_id INTEGER,
            title TEXT,
            status TEXT,
            FOREIGN KEY (brain_id) REFERENCES brains(id)
        );
        """)

        conn.commit()
        conn.close()

    # Save the brain's data to the database
    def save_to_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Insert the brain's features as a JSON string
        cursor.execute("INSERT INTO brains (features) VALUES (?)", (str(self.features),))
        self.id = cursor.lastrowid  # Update the brain's id after insertion

        # Save the features
        for feature in self.features:
            cursor.execute("INSERT INTO features (brain_id, feature) VALUES (?, ?)", (self.id, feature))

        # Save the memories
        for memory in self.memories:
            cursor.execute("INSERT INTO memories (brain_id, memory) VALUES (?, ?)", (self.id, memory))

        # Save the emotions
        for emotion in self.emotions:
            cursor.execute("INSERT INTO emotions (brain_id, emotion) VALUES (?, ?)", (self.id, emotion))

        # Save the personalities
        for personality in self.personality:
            cursor.execute("INSERT INTO personalities (brain_id, personality_trait) VALUES (?, ?)", (self.id, personality))

        # Save the friends (many-to-many relationship)
        for friend in self.friends:
            cursor.execute("INSERT INTO friends (brain1_id, brain2_id) VALUES (?, ?)", (self.id, friend.id))

        # Save the tasks
        for task in self.tasks:
            cursor.execute("INSERT INTO tasks (brain_id, title, status) VALUES (?, ?, ?)", (self.id, task.title, task.status))

        conn.commit()
        conn.close()
        logging.info(f"Brain with id {self.id} saved to the database.")

    # Load brain's data from the database
    def load_from_db(self, brain_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Load brain's features
        cursor.execute("SELECT features FROM brains WHERE id = ?", (brain_id,))
        result = cursor.fetchone()
        if result:
            self.features = eval(result[0])  # Convert string back to list

        # Load brain's memories
        cursor.execute("SELECT memory FROM memories WHERE brain_id = ?", (brain_id,))
        self.memories = [row[0] for row in cursor.fetchall()]

        # Load brain's emotions
        cursor.execute("SELECT emotion FROM emotions WHERE brain_id = ?", (brain_id,))
        self.emotions = [row[0] for row in cursor.fetchall()]

        # Load brain's personality traits
        cursor.execute("SELECT personality_trait FROM personalities WHERE brain_id = ?", (brain_id,))
        self.personality = [row[0] for row in cursor.fetchall()]

        # Load brain's friends
        cursor.execute("SELECT brain2_id FROM friends WHERE brain1_id = ?", (brain_id,))
        self.friends = [row[0] for row in cursor.fetchall()]

        # Load brain's tasks
        cursor.execute("SELECT title, status FROM tasks WHERE brain_id = ?", (brain_id,))
        self.tasks = [Task(title=row[0], status=row[1]) for row in cursor.fetchall()]

        conn.close()
        logging.info(f"Brain with id {brain_id} loaded from the database.")
