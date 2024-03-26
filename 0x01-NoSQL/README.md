0x01-NoSQL

This project is a collection of scripts and functions for working with MongoDB in the context of managing databases and collections, primarily focusing on performing various operations using Python and the PyMongo library. Below is an overview of the project structure and the tasks it covers.

Requirements
MongoDB Command File
MongoDB version 4.2 is required.
All files should be interpreted/compiled on Ubuntu 18.04 LTS.
Files should end with a new line.
The first line of all files should be a comment: // my comment.
A README.md file at the root of the project directory is mandatory.
Python Scripts
Python version 3.7 is required.
PyMongo version 3.10 should be used.
All files should end with a new line.
The first line of all Python files should be exactly #!/usr/bin/env python3.
A README.md file at the root of the project directory is mandatory.
Code should follow the pycodestyle style (version 2.5.*).
Documentation should be provided for all modules and functions.
Code execution should be protected when imported using if __name__ == "__main__":.
Installation
MongoDB Installation on Ubuntu 18.04
Follow these steps to install MongoDB 4.2 on Ubuntu 18.04:

$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
After installation, start the MongoDB service:

$ sudo service mongod start
Python Dependencies
Install PyMongo:

$ pip3 install pymongo
Project Structure
The project directory structure is organized as follows:

README.md: This file providing an overview of the project.
0-list_databases: Script to list all databases in MongoDB.
1-use_or_create_database: Script to create or use the database my_db.
2-insert: Script to insert a document in the collection school.
3-all: Script to list all documents in the collection school.
4-match: Script to list all documents with name="Holberton school" in the collection school.
5-count: Script to display the number of documents in the collection school.
6-update: Script to add a new attribute to documents with name="Holberton school" in the collection school.
7-delete: Script to delete all documents with name="Holberton school" in the collection school.
8-all.py: Python module containing a function to list all documents in a collection.
9-insert_school.py: Python module containing a function to insert a new document in a collection based on keyword arguments.
10-update_topics.py: Python module containing a function to change all topics of a school document based on the name.
11-schools_by_topic.py: Python module containing a function to return the list of schools having a specific topic.
12-log_stats.py: Python script providing stats about Nginx logs stored in MongoDB.
100-find: Script to list all documents with name starting by "Holberton" in the collection school.
101-students.py: Python module containing a function to return all students sorted by average score.
102-log_stats.py: Enhanced version of 12-log_stats.py, providing additional stats about the most present IPs in the Nginx logs.

Each script or function serves a specific purpose and can be executed or imported as needed. Consult individual script or function documentation for usage details.

This project is part of the curriculum for the ALX Software Engineering program. All scripts and functions are authored by ALX School students.

For detailed instructions and examples of usage, refer to the individual script or function files.

GitHub Repository: alx-backend-storage

Directory: 0x01-NoSQL
