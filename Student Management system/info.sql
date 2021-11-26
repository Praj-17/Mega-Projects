use testdb;

CREATE TABLE info(
        UID INT PRIMARY KEY,
        Name varchar(255),
        Roll_No int,
        Phone_No int,
        Email varchar(255)
);

INSERT INTO info(UID, Name, Roll_No, Phone_No, Email) VALUES
(22010201, 'Prajwal', 1, 5432132121, 'prajwal45321@gmail.com');

INSERT INTO info(UID, Name, Roll_No, Phone_No, Email) VALUES
('pushpak', 2, 438932542, 'pushpak453621@gmail.com'),
('soham', 3, 5673819283, 'soham65321@gmail.com');
