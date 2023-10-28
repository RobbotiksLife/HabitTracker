# Habit Tracker ReadMe

## Introduction

The Python terminal Habit Tracker is a command-line application designed to help you keep track of your daily habits and monitor your progress. It consists of five Python files: "recurrence.py," "habit.py," "habitTracker.py," "habitTrackerApp.py," and "main.py." Each of these files serves a specific purpose within the application.

## File Descriptions

### 1. `recurrence.py`

This file contains the definition of recurrence types and a class for handling recurrence.

- `RecurrenceType`: An enumeration representing different recurrence types, including DAILY, WEEKLY, MONTHLY, and YEARLY.

- `Recurrence`: A class that defines a recurrence with a specific type and interval. It provides methods to calculate the next occurrence based on the last one.

### 2. `habit.py`

In this file, you'll find classes related to habits and their history.

- `HabitCompletionHistoryPoint`: A class representing a completion point for a habit on a specific date.

- `Habit`: A class that defines a habit with a name, description, first deadline, recurrence, and completion history. It includes methods for completing a habit, calculating the longest streak, and displaying habit information.

### 3. `habitTracker.py`

This file contains the `HabitTracker` class responsible for managing a list of habits. It also provides methods to add, list, and manipulate habits.

### 4. `habitTrackerApp.py`

This file defines the `HabitTrackerApp` class, which is a command-line application for interacting with the habit tracker. It includes methods for creating, listing, and managing habits, as well as saving and loading habits from a file.

## Getting Started

To use the Habit Tracker, you can run the `main.py` script. This script creates an instance of the `HabitTrackerApp` class with some predefined habits. You can customize these habits or add your own by following the prompts in the command-line interface.

## Usage

1. Run the `main.py` script to start the Habit Tracker application.

2. Choose from various options in the menu, such as creating habits, listing habits, listing habits by recurrence, and more.

3. Follow the prompts to input habit details and manage your habits.

4. You can also save and load your habits from a file for persistence.

## Example Predefined Habits

The `main.py` script provides some example predefined habits, including "Daily Exercise," "Weekly Reading," "Meditation," "Healthy Eating," and "Language Learning." These habits have different recurrences and completion histories, which can serve as a reference for creating your own habits.

## Notes

- Make sure you have Python installed on your system.

- The application stores habits in a pickle file by default ("tasks.pickle"). You can choose a custom file path when saving or loading habits.

- Be cautious when modifying the code, especially if you're new to Python programming. Incorrect changes may break the functionality.

- The application is designed for educational purposes and personal use. Feel free to adapt and expand it to meet your specific needs.

## Author

This Habit Tracker application was created as a sample Python project and provided with code examples by Volodymyr Bezpalko.

## Disclaimer

This is not a production-ready application. Use it at your own discretion and feel free to improve it or customize it to better suit your requirements.

Enjoy tracking and building healthy habits with the Habit Tracker!