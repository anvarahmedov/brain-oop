-- Create Task table for the Task class
CREATE TABLE IF NOT EXISTS Task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status TEXT NOT NULL,
    brain_id INTEGER,
    FOREIGN KEY (brain_id) REFERENCES Brain(id) ON DELETE CASCADE
);

-- Example: Insert a task into the Task table
INSERT INTO Task (title, status, brain_id)
VALUES ('Complete Brain Model', 'In Progress', 1);
