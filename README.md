# ACEest Fitness – Assignment‑1

## Overview
Aceest Flask implementation with full CI/CD automation.

## Run Locally
```bash
pip install -r requirements.txt
python run.py
```

## Test
```bash
pytest
```

## Docker
```bash
docker build -t aceest-fitness
docker run -p 5000:5000 aceest-fitness
```

## CI/CD
- GitHub Actions: test + docker build
- Jenkins: venv → pytest → docker build


👤 Author
Name: Abhijat Dwivedi 2024ht66529
Course / Subject: DevOps 
Assignment: Assignment‑1 – CI/CD Implementation