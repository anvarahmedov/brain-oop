# brain-oop
# Brain and Task Management System

## Overview

This system allows the creation and management of "brain" instances, each of which can have various features, memories, emotions, and tasks. Additionally, a routine manager is implemented for scheduling tasks based on specific days and hours. The interaction between different "brain" instances is facilitated through features like friendship and shared traits.

## Classes

### Task
- Represents a task that can be added to a brain's task list.
- Each task has an `id`, `title`, `status`, and a reference to the `brain_id` it is associated with.

**Methods:**
- `__init__(title, status, brain_id)`: Initializes a task with a title, status, and associated brain id.
- `get_title()`: Retrieves the title of the task.
- `get_status()`: Retrieves the status of the task.
- `set_status(status)`: Updates the task status.
- `get_brain_id()`: Retrieves the associated brain id.
- `__repr__()`: String representation of the task.

### RoutineManager
- Manages the routine for each brain, allowing tasks to be scheduled on specific weekdays and hours.

**Methods:**
- `set_routine(task, brain_id, weekday, hour)`: Sets a routine task for a specific brain on a given weekday and hour.
- `get_routine(weekday, hour)`: Retrieves a task scheduled for a specific weekday and hour.

### Brain
- Represents an instance of a "brain" which holds various features, memories, emotions, tasks, and a routine manager.
- Brains can interact with other brains, form friendships, and share common features.

**Methods:**
- `__init__()`: Initializes a brain instance with a unique id and empty lists for features, memories, emotions, tasks, etc.
- `get_features()`: Retrieves the features of the brain.
- `set_features(features)`: Adds features to the brain.
- `get_memories()`: Retrieves the memories of the brain.
- `add_memory(memory)`: Adds a memory to the brain.
- `update_memory(index, memory)`: Updates a memory at a specific index.
- `delete_memory(index)`: Deletes a memory at a specific index.
- `get_emotions()`: Retrieves the emotions of the brain.
- `add_emotion(emotion)`: Adds an emotion to the brain.
- `get_personality()`: Retrieves the personality traits of the brain.
- `add_personality(trait)`: Adds a personality trait to the brain.
- `get_groups()`: Retrieves the groups the brain is part of.
- `join_group(group)`: Adds the brain to a group.
- `leave_group(group)`: Removes the brain from a group.
- `is_friends_with(other_brain)`: Checks if the brain is friends with another brain.
- `be_friends_with(other_brain, status)`: Makes or breaks a friendship with another brain.
- `simulate_interaction(other_brain)`: Simulates an interaction with another brain, based on shared features.
- `get_fav_songs()`: Retrieves the favorite songs of the brain.
- `set_fav_songs(songs)`: Adds new favorite songs to the brain.
- `add_task(task)`: Adds a task to the brain's task list.
- `get_tasks()`: Retrieves all tasks of the brain.

## Logging
The system uses the `logging` module to track and log various operations, such as task creation, memory updates, and brain interactions.

## Example Usage

```python
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
```

## Requirements
- Python 3.x
