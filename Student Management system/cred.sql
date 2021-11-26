use testdb;

create table cred(
        UID INT AUTO_INCREMENT PRIMARY KEY,
        username varchar(255),
        password varchar(14)
);

INSERT INTO cred(UID, username, password) values
(22010201, 'prajwal', 'prajwal@12345');

INSERT INTO cred(UID, username, password) values
('pushpak', 'pushpak@12345'),
('soham', 'soham@12345'),
('rushi', 'rushi@12345'),
('saiprasad', 'saiprsaad@12345');
