# Project Management CLI Tool

## Overview
This is a Python command line interface (CLI) application for managing users, projects, and tasks.  
It allows administrators to create users, assign projects to users, and manage tasks within projects.

The system uses object relationships and file persistence to simulate a real project management workflow.

---

## Features

- Add new users with name and email
- List all users
- Add projects to specific users
- List projects for a user
- Add tasks to projects
- Mark tasks as completed
- Persistent storage using JSON files

---

## Project Structure

project-cli/
│
├── main.py
├── requirements.txt
│
├── data/
│   └── data.json

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repository-link>
cd project-cli