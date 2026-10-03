import sqlite3
 
# Create/connect to database
conn = sqlite3.connect("tution.db")
 
# Create a cursor
cursor = conn.cursor()
 
# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR(20),
        date_of_birth VARCHAR(20),
        age INTEGER,
        gender VARCHAR(10),
        mobile_number INT,
        email_address VARCHAR(20) UNIQUE,
        password VARCHAR(25),
        preferred_language VARCHAR(20),
        school_college_name VARCHAR(50),
        class_grade VARCHAR(10),
        board_curriculum VARCHAR(20),
        academic_year VARCHAR(10),
        tuition_subjects TEXT NOT NULL DEFAULT '[]',
        subject_levels TEXT NOT NULL DEFAULT '{}',
        topics_needing_help TEXT NOT NULL DEFAULT '[]',
        parent_guardian_name VARCHAR(20),
        parent_guardian_relationship VARCHAR(20),
        parent_guardian_mobile_number INT,
        parent_guardian_email_address VARCHAR(20),
        preferred_communication_method VARCHAR(20)
    )
""")

cursor.execute("""
INSERT INTO students (
    full_name,
    date_of_birth,
    age,
    gender,
    mobile_number,
    email_address,
    password,
    preferred_language,
    school_college_name,
    class_grade,
    board_curriculum,
    academic_year,
    tuition_subjects,
    subject_levels,
    topics_needing_help,
    parent_guardian_name,
    parent_guardian_relationship,
    parent_guardian_mobile_number,
    parent_guardian_email_address,
    preferred_communication_method
) VALUES (
    'Arjun Nair',
    '2010-06-15',
    16,
    'Male',
    9876543210,
    'arjun.nair22@gmail.com',
    'Arjun@123',
    'English',
    'Green Valley Public School',
    '10',
    'CBSE',
    '2026-27',
    '["Mathematics", "Physics", "Chemistry"]',
    '{"Mathematics":"Intermediate","Physics":"Beginner","Chemistry":"Intermediate"}',
    '["Quadratic Equations", "Electricity", "Chemical Reactions"]',
    'Suresh Nair',
    'Father',
    9123456789,
    'suresh.nair@gmail.com',
    'WhatsApp'
);
""")
 
# Save changes
conn.commit()
 
# Close connection
conn.close()
 
print("Database created successfully!")  