# 📧 OpenEnv Email Assistant

An AI-powered email assistant built using the OpenEnv framework.  
This project simulates real-world email tasks like sorting, replying, and prioritizing emails.

---

## 🚀 Features

- 📥 Email classification (spam, important, normal)
- ⚡ Priority detection
- 🤖 Auto-reply generation
- 🗂️ Email organization (folders/labels)
- 📊 Reward-based evaluation (OpenEnv)

---

## 🧠 About OpenEnv

This project follows the OpenEnv specification:
- `Observation` → Current email state
- `Action` → Agent decision (reply, classify, ignore)
- `Reward` → Based on correctness of action

---

## 🛠️ Tech Stack

- Python
- Pydantic
- OpenAI / LLM
- FastAPI (optional)
- OpenEnv Interface

---

## 📦 Installation

```bash
git clone https://github.com/your-username/openenv-email-assistant.git
cd openenv-email-assistant
pip install -r requirements.txt