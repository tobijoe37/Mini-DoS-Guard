 
# Mini DoS Guard

A beginner-friendly Python cybersecurity project that simulates basic Denial-of-Service (DoS) detection and integrates with Windows Firewall.

## Project Overview

Mini DoS Guard monitors simulated network requests and identifies IP addresses that send too many requests within a specified time window.

When suspicious activity is detected, the program attempts to create an inbound blocking rule using Windows Firewall.

## Features

- Tracks requests from individual IP addresses.
- Detects suspicious request patterns using a threshold.
- Integrates with Windows Firewall using Python.
- Logs security events.
- Reports successful and failed firewall actions.

## Technologies Used

- Python
- Windows Command Prompt
- Windows Defender Firewall
- Git and GitHub

## Project Files

- `main.py` - Traffic monitoring and DoS detection.
- `blocker.py` - Windows Firewall integration.
- `logger.py` - Security event logging.
- `test_blocker.py` - Firewall integration test.

## How to Run

1. Install Python.
2. Open Command Prompt as Administrator.
3. Navigate to the project folder.
4. Run:

```cmd
py main.py
```

## Disclaimer

This project uses simulated traffic and reserved documentation IP addresses for testing.

It is an educational demonstration, not a production-grade DoS protection system. Do not use it to block real devices or IP addresses without authorization.

## Author Joseph Mathew

Cybersecurity Learner | Aspiring SOC Analyst
