
📘 Assignment‑1: Automated CI/CD Pipeline
ACEest Fitness & Gym

📌 Overview
This project demonstrates the design and implementation of a complete automated CI/CD pipeline for the ACEest Fitness & Gym application using modern DevOps practices.
The original Aceestver‑1.1 desktop (Tkinter) application has been successfully migrated to a Flask‑based web application, containerized using Docker, and integrated with GitHub Actions and Jenkins to ensure code quality, consistency, and automated delivery.

🎯 Objective
The objective of this assignment is to provide hands‑on experience with:

Version Control using Git/GitHub
Flask web application development
Unit testing with Pytest
Containerization using Docker
CI automation via GitHub Actions
BUILD & quality gate using Jenkins


🧱 Project Structure
aceest_flask_assignment1_1/
│
├── run.py                     # Application entry point
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker image definition
├── Jenkinsfile                # Jenkins pipeline configuration
│
├── app/
│   ├── __init__.py            # Flask app factory
│   └── routes.py              # Web routes & logic
│
├── templates/
│   └── index.html             # UI (same behavior as Aceestver‑1.1)
│
├── static/
│   └── style.css              # Dark ACEest theme
│
├── tests/
│   └── test_app.py            # Pytest unit tests
│
└── .github/
    └── workflows/
        └── main.yml           # GitHub Actions CI pipeline


💻 Application Description

A simple Flask web application replicating the UI behavior of Aceestver‑1.1
Allows users to select a fitness program:

Fat Loss (FL)
Muscle Gain (MG)
Beginner (BG)


Displays the corresponding program summary dynamically on the web page
Implements the Flask Application Factory pattern for scalability and testability


🚀 Local Setup & Execution
✅ Prerequisites

Python 3.10+
pip
Docker (for containerized run)


▶ Run Locally (Without Docker)
pip install -r requirements.txt
python run.py
``
Open your browser at:
http://localhost:5000


✅ Unit Testing with Pytest
The application logic and routes are verified using Pytest.
pytest
A passing test suite confirms the integrity of the Flask application before entering the build stage.

🐳 Containerization with Docker
The application is packaged into a portable Docker image.
🔹 Build the Docker Image
docker build -t aceest-fitness
🔹 Run the Container
Shelldocker run -p 5000:5000 aceest-fitnessShow more lines
Access the app at:
http://localhost:5000


🔁 CI Pipeline – GitHub Actions
A fully automated CI pipeline is configured in:
.github/workflows/main.yml

✅ Triggered On:

Every push
Every pull_request

✅ CI Stages:

Checkout source code
Set up Python environment
Install dependencies
Run Pytest unit tests
Build Docker image

This ensures that only tested code progresses further.

⚙ Jenkins BUILD & Quality Gate
Jenkins is used as a secondary verification layer (BUILD server).
✅ Jenkins Pipeline Features:

Pulls source code from GitHub
Creates a Python virtual environment (PEP‑668 compliant)
Installs dependencies
Runs Pytest
Builds Docker image

The pipeline definition is stored in:
Jenkinsfile


🔐 Version Control Strategy

GitHub used as the central repository
Industry‑standard commit messages followed:

feat: new features
test: test cases
ci: pipeline changes
docker: container updates


Branching model:

main → stable branch
develop → integration branch
feature branches for development




🎓 Key Learnings & Outcomes

Migrated a desktop GUI app (Tkinter) to a web‑based Flask app
Implemented test‑driven validation
Achieved environment consistency via Docker
Designed a robust CI/CD workflow
Applied industry‑grade DevOps practices



👤 Author
Name: Abhijat Dwivedi 2024ht66529
Course / Subject: DevOps 
Assignment: Assignment‑1 – CI/CD Implementation