-- This file is for creating all tables
-- Final Project for CMPSC 174A
-- Yiting Ju & Runsheng Song Nov.22

use projects;

-- Create Table Employees
CREATE TABLE Employees(
    id			integer,
    age			integer,
    salary		TEXT NOT NULL,
    PRIMARY KEY(id)
);
