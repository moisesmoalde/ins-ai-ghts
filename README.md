# ins-ai-ghts
Web application that implements a Retrieval-Augmented Generation (RAG) backend system to analyse and compare two provided datasets of survey results.
It makes use of a llama3.2 model running locally using **ollama**.

## Overview

This repository is a **monorepo** containing multiple projects (e.g., frontend, backend, services).

This guide outlines the steps to deploy the entire monorepo locally on an **AWS EC2 instance**.

## Prerequisites

Ensure you have the following before starting the deployment:

- **AWS EC2 Instance** (Ubuntu recommended)
- **SSH Access** to the EC2 instance
- **Git** installed on the EC2 instance
- **Python3** and **pip** installed on the EC2 instance
- Security group activated on the EC2 that allows **all TCP** connections (origin 0.0.0.0/0) to ports **3000** and **8000**

## Steps to Deploy

### 1. SSH into the EC2 Instance

Use SSH to access the EC2 instance. Replace `your-key.pem` and `ec2-user@your-instance-ip` with your actual key and instance details.

```bash
ssh -i "your-key.pem" ec2-user@your-instance-ip
```

### 2. Update and install Ollama

```bash
sudo apt update && sudo apt upgrade
curl -fsSL https://ollama.com/install.sh | sh
```

Download the latest llama3.2 model.

```bash
ollama pull llama3.2
```

### 3. Clone the repository and install requirements

Clone the repository:
```bash
git clone https://github.com/moisesmoalde/ins-ai-ghts.git
cd ins-ai-ghts
```

Create a virtual environment, activate it and install requirements:
```bash
python3 -m venv .venv
echo "*" > .venv/.gitignore
```
```bash
source .venv/bin/activate
pip install -r backend/requirements.txt
```

### 4. Launch the backend and frontend

```bash
python3 -m http.server -d frontend 3000
```

In another terminal:
```bash
cd backend
python3 main.py
```

### 5. Open an explorer and connect to your frontend

[http://your-instance-ip:3000]
