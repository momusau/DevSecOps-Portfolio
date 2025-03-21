# Secure CI/CD Pipeline

## Overview
This project demonstrates a **secure CI/CD pipeline** that integrates:
* Static Analysis (SAST) - CodeQL
* Container Security - Trivy
* Infrastructure Scanning - Checkov

The purpose of this project is to demostrate, in a very small simple scale, how a team might incorporate some security best practices into their development/deployment cycles. This allows for a security-first approach to development and allows the user(s) to be notified early in their development of potential security risks that may come up during a more formal security investigation such as a Pentest.

This repository will run and deploy a python app to Amazon EKS; the assumption is that the cluster is already up and running and the secrets have been created in GitHub Actions.

## Tech Stack
- GitHub Actions
- AWS
- Docker, Kubernetes

## How to Use
1. Clone this repository:
   ```sh
   git clone https://github.com/momusau/DevSecOps-Portfolio.git
2. To run the test application locally:
   ```
   docker-compose up
   ```