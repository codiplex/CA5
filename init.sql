-- Create a table called students in the mydb database
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    rollnumber VARCHAR(255)
);

-- Insert name and roll numbers into the student table
INSERT INTO students (name, rollnumber) VALUES ('John', '1');
INSERT INTO students (name, rollnumber) VALUES ('Doe', '2');
INSERT INTO students (name, rollnumber) VALUES ('Jane', '3');
INSERT INTO students (name, rollnumber) VALUES ('Doe', '4');
INSERT INTO students (name, rollnumber) VALUES ('John', '5');

-- Select all rows from the students table
SELECT * FROM students;
