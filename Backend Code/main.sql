CREATE TABLE Registration (
 ID INT PRIMARY KEY AUTO_INCREMENT,
 Name VARCHAR(50) NOT NULL,
 Email VARCHAR(100) UNIQUE NOT NULL,
 DateOfBirth DATE,
 PhoneNumber VARCHAR(15) UNIQUE,
 RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)