# Delivery Service Simulator

## Overview
This project simulates a package delivery service, implementing an efficient routing system for trucks to deliver packages across various locations. It includes features such as package tracking, status updates, and a user interface for querying package statuses.

## Features
- Package loading and routing for multiple trucks
- Distance calculation between delivery locations
- Real-time package status tracking
- User interface for checking package statuses
- Time-based status queries
- Total mileage calculation for trucks

## Files
- `main.py`: The main script that initializes and runs the simulation
- `package.py`: Defines the Package class
- `truck.py`: Defines the Truck class
- `user_interface.py`: Implements the user interface for interacting with the system
- `distance_matrix.py`: Contains the distance matrix and functions for distance calculations
- `cleaned_package_file.csv`: CSV file containing package data

## Setup
1. Ensure you have Python 3.x installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory.

## Usage
To run the simulation: run "python main.py"

This will start the simulation and load the user interface. From there, you can:

1. Check the status of a specific package
2. View the status of all packages
3. Check the status of all packages at a specific time
4. View truck status and total mileage

## Data Structures
- HashMap: Used for efficient package lookup
- Lists: Used for storing packages and managing truck loads

## Algorithms
- Nearest Neighbor: Used for determining the next package to deliver

## Future Improvements
- Implement more sophisticated routing algorithms
- Add support for dynamic package additions during runtime
- Enhance the user interface with graphical elements
