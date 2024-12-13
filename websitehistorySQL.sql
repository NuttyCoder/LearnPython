-- Create the database
CREATE DATABASE IF NOT EXISTS InternetHistoryDB;
USE InternetHistoryDB;

-- Create the table
CREATE TABLE IF NOT EXISTS BrowsingHistory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    website_address VARCHAR(255) NOT NULL,
    device VARCHAR(100) NOT NULL,
    time_of_day TIME NOT NULL,
    date_of_visit DATE NOT NULL
);

-- Insert sample data
INSERT INTO BrowsingHistory (website_address, device, time_of_day, date_of_visit)
VALUES 
('https://www.example.com', 'Laptop', '14:30:00', '2024-12-13'),
('https://www.anotherexample.com', 'Smartphone', '09:15:00', '2024-12-14'),
('https://www.mysite.com', 'Tablet', '21:45:00', '2024-12-15');

-- Query the data
SELECT * FROM BrowsingHistory;
