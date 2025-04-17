-- Create the database with the primary file
CREATE DATABASE quiz_app
ON
PRIMARY (
    NAME = 'quiz_app_data', 
    FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\quiz_app_data.mdf', 
    SIZE = 10MB, 
    MAXSIZE = 100MB, 
    FILEGROWTH = 5MB
)

-- Add the log file

 LOG on (
    NAME = 'quiz_app_log', 
    FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\quiz_app_log.ldf', 
    SIZE = 5MB, 
    MAXSIZE = 50MB, 
    FILEGROWTH = 5MB
);

-- Add a secondary file
ALTER DATABASE quiz_app
ADD FILE (
    NAME = 'quiz_app_data2',
    FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\quiz_app_data2.ndf',
    SIZE = 10MB,
    MAXSIZE = 100MB,
    FILEGROWTH = 5MB
);
use quiz_app