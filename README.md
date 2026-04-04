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
**Important** : For Jenkins trigger from GitHub Actions workflow, Please check the IP address of Jenkins server, using ‘ifconfig’ on Linux machine. Note it down and go to GitHub Actions tab on remote repository and update the JENKINS_URL secrets following Settings --> Secrets & variables --> Actions --> Update/Edit Repository Secret (JEN-KINS_URL). This is required because currently, we do not have external Jenkins server URL link or having a server which is up and running on same IP/static IP. We are using Jenkins in-stance available on BITS Pilani aws virtual Desktop allocated for current subject which has a limited uptime and dynamically changes IP whenever re-started.
## CI/CD
- GitHub Actions: test + docker build
- Jenkins: venv → pytest → docker build


👤 Author
Name: Abhijat Dwivedi 2024ht66529
Course / Subject: DevOps 
Assignment: Assignment‑1 – CI/CD Implementation
