# SQL - Introduction

## What’s a Database?

A database is a structured collection of data that is organized in a way that facilitates efficient retrieval, management, and updating of information.

## What’s a Relational Database?

A relational database organizes data into tables with rows and columns, establishing relationships between the tables. It follows the principles of the relational model, providing a powerful and flexible way to manage data.

## What Does SQL Stand For?

SQL stands for Structured Query Language. It is a domain-specific language used to manage and manipulate relational databases. SQL provides a standardized way to interact with databases, making it a crucial skill for developers and data professionals.

## What’s MySQL?

MySQL is an open-source relational database management system (RDBMS) that uses SQL. It is widely used for web applications and provides a robust and scalable solution for managing databases.

## How to Create a Database in MySQL

CREATE DATABASE database_name;
This SQL command creates a new database with the specified name.

## What Does DDL and DML Stand For?

- DDL (Data Definition Language): It deals with the structure of the database, defining and modifying schema objects like tables and indexes.
Examples:
CREATE TABLE table_name (column1 datatype, column2 datatype, ...);

- DML (Data Manipulation Language): It involves managing data stored in the database, such as inserting, updating, or deleting records.
Examples:
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);

- How to CREATE or ALTER a Table

Creating a new table:
CREATE TABLE table_name (column1 datatype, column2 datatype, ...);

Altering a table (adding a new column):
ALTER TABLE table_name ADD column_name datatype;

## How to SELECT Data from a Table

SELECT column1, column2, ... FROM table_name WHERE condition;
This query retrieves specific columns from a table based on a specified condition.

## How to INSERT, UPDATE, or DELETE Data

Inserting data into a table:
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);

Updating data in a table:
UPDATE table_name SET column1 = value1 WHERE condition;

Deleting data from a table:
DELETE FROM table_name WHERE condition;

## What Are Subqueries?

A subquery is a query nested inside another query. It allows you to perform complex operations and retrieve data based on the results of another query.

## How to Use MySQL Functions

MySQL provides a variety of functions for data manipulation and computation. Examples include:

- 'COUNT()': Count the number of rows in a result set.
- 'SUM()': Calculate the sum of values in a column.
- 'AVG()': Calculate the average of values in a column.

Example:
SELECT COUNT(*) FROM table_name;

Explore MySQL documentation for a comprehensive list of functions and their uses.
