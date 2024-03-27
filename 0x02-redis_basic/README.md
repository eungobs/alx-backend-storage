# 0x02-redis_basic

## Description
This project implements various functionalities using Redis, a popular in-memory data structure store. It includes tasks such as storing strings to Redis, reading from Redis, incrementing values, storing and retrieving lists, and implementing an expiring web cache and tracker.

## Project Structure
- `exercise.py`: Contains the implementation of the Cache class and related functions.
- `main.py`: Contains test cases for the implemented functionalities.
- `README.md`: Documentation for the project.

## Getting Started
To run the project, make sure you have Python and Redis installed on your system.

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/0x02-redis_basic.git

Install the required Python packages:

pip install -r requirements.txt
Start a Redis server on your local machine. You can download and install Redis from here.

Run the test cases:


python main.py
Implementation Details
The exercise.py file contains the implementation of the Cache class, which provides methods for storing data to Redis, reading data from Redis, incrementing values, and managing lists.
Decorators are used to add additional functionality to the methods of the Cache class, such as counting method calls and storing method inputs and outputs.
Testing
Test cases are provided in main.py to validate the correctness of the implemented functionalities. Each test case checks a specific functionality of the Cache class.

Contributor: Elizabeth Eunice Ndzukule
This project is licensed under the MIT License.
