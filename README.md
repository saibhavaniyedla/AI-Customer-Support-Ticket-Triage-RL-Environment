# 🤖 AI Customer Support Ticket Triage RL Environment

## 📌 Overview

This project is a Reinforcement Learning (RL) based simulation environment that automates customer support ticket triage. An intelligent agent learns to classify and route support tickets into correct categories such as refund, technical issue, account problem, etc. The agent improves over time by interacting with the environment and receiving rewards for correct decisions and penalties for incorrect ones.

The goal is to demonstrate how reinforcement learning can be applied to real-world customer support systems to improve accuracy, efficiency, and automation.

---

## 🧠 How It Works

- A customer support ticket is generated with an issue description  
- The RL agent observes the ticket (state)  
- The agent selects an action (category/department)  
- The environment evaluates the action  
- Reward is given:
  - ✅ Correct triage → +1 reward  
  - ❌ Incorrect triage → -1 penalty  
- The agent learns from feedback and improves over time  

---

## 🚀 Execution Process

### 🔹 Step 1: Clone the Repository
```bash
git clone https://github.com/saibhavaniyedla/AI-Customer-Support-Ticket-Triage-RL-Environment.git
cd AI-Customer-Support-Ticket-Triage-RL-Environment

## 🚀 Execution Process

### 🔹 Step 2: Create Virtual Environment
Create an isolated Python environment to manage dependencies.

```bash
python -m venv venv

## 🚀 Execution Process

### 🔹 Step 3: Activate Virtual Environment

Windows

venv\Scripts\activate

### 🔹 Step 4: Install Dependencies

Install all required libraries using requirements file.

pip install -r requirements.txt

### 🔹 Step 5: Run FastAPI Server

Start the backend server using Uvicorn.

uvicorn app:app --reload

After successful execution, you will see:

Uvicorn running on http://127.0.0.1:8000


### 🔹 Step 6: Open API Documentation

Open your browser and go to:

http://127.0.0.1:8000/docs

This opens the Swagger UI where you can test APIs.

### 🔹 Step 7: Test the API

Endpoint:

POST /act

Request Example:

{
  "ticket_id": 1,
  "action": "refund"
}

Response Example (Correct):

{
  "reward": 1,
  "correct": true,
  "message": "Correct triage!"
}

Response Example (Incorrect):

{
  "reward": -1,
  "correct": false,
  "message": "Incorrect triage!"
}

---

# ⚙️ Tech Stack
1. Python 🐍
2. FastAPI ⚡
3. Pydantic
4. Reinforcement Learning (Custom Environment)
5. Uvicorn
