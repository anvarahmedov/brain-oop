-- Create the brains table
CREATE TABLE IF NOT EXISTS brains (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    features TEXT
);

-- Create the features table
CREATE TABLE IF NOT EXISTS features (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brain_id INTEGER,
    feature TEXT,
    FOREIGN KEY (brain_id) REFERENCES brains(id)
);

-- Create the memories table
CREATE TABLE IF NOT EXISTS memories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brain_id INTEGER,
    memory TEXT,
    FOREIGN KEY (brain_id) REFERENCES brains(id)
);

-- Create the emotions table
CREATE TABLE IF NOT EXISTS emotions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brain_id INTEGER,
    emotion TEXT,
    FOREIGN KEY (brain_id) REFERENCES brains(id)
);

-- Create the personalities table
CREATE TABLE IF NOT EXISTS personalities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brain_id INTEGER,
    personality_trait TEXT,
    FOREIGN KEY (brain_id) REFERENCES brains(id)
);

-- Create the friends table (many-to-many relationship)
CREATE TABLE IF NOT EXISTS friends (
    brain1_id INTEGER,
    brain2_id INTEGER,
    PRIMARY KEY (brain1_id, brain2_id),
    FOREIGN KEY (brain1_id) REFERENCES brains(id),
    FOREIGN KEY (brain2_id) REFERENCES brains(id)
);

-- Create the tasks table
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brain_id INTEGER,
    title TEXT,
    status TEXT,
    FOREIGN KEY (brain_id) REFERENCES brains(id)
);
