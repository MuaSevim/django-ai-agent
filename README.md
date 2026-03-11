# 🤖 AI Agentic Systems: Django, LangGraph & Permit Integration

This repository demonstrates a **production-grade implementation of multi-agent AI systems** integrated within a **Django ecosystem**.

By combining the **data management power of Django**, the **orchestration capabilities of LangGraph**, and **secure guardrails from Permit.io**, the system enables **complex autonomous interactions with local data and third-party APIs**.

The project is designed to illustrate how modern **agentic architectures** can safely interact with application databases and external services.

---

# 🚀 Key Implementation Features

### 🧠 Multi-Agent Supervision

Implements a **Supervisor Agent pattern** that intelligently routes user requests to specialized assistants based on intent.

### 📄 Secure Document Management

A dedicated agent capable of:

* Creating documents
* Listing documents
* Retrieving documents
* Deleting documents

All operations are executed through **standard Django ORM queries**.

### 🎬 Third-Party API Integration

A **Movie Discovery Agent** interacts with **The Movie Database (TMDB)** API to retrieve real-time movie metadata.

### 🛡 Enterprise-Grade Guardrails

Full **Role-Based Access Control (RBAC)** and **Relationship-Based Access Control (ReBAC)** implementation via **Permit.io**, ensuring agents can only access **authorized data and resources**.

### 🔄 Model-Agnostic Architecture

The system allows seamless switching between **different LLM providers** to optimize:

* Performance
* Latency
* Cost

### ⚡ Rapid Prototyping

Integrated **Jupyter notebooks** allow fast experimentation with:

* Agent tools
* Prompt engineering
* Multi-agent workflows

---

# 🛠 Tech Stack

### Backend Framework

* Django ≥ 5.0

### Agent Orchestration

* LangGraph
* LangChain

### Access Control

* Permit.io

### Development Tools

* Jupyter Notebook
* Python-decouple

### Core APIs

* OpenAI API (LLM processing)
* TMDB API (Movie metadata)

---

# 🏗 System Architecture

The system follows a **modular, decoupled architecture** separating AI orchestration from business logic.

```
project-root/
│
├── src/
│   ├── agents/           # Agent definitions (ReAct agents)
│   ├── tools/            # LangChain tools wrapping Python functions
│   ├── orchestration/    # Supervisor agent logic
│   ├── models/           # Django models
│   └── settings/
│
├── notebooks/            # Jupyter prototyping notebooks
│
├── manage.py
│
└── README.md
```

### Architecture Layers

**1️⃣ Data Layer**

* Django Models
* Handles persistent storage for:

  * Documents
  * User relationships
  * Permissions

---

**2️⃣ Tool Layer**

Python functions wrapped as **LangChain tools** that allow agents to execute real operations:

Examples:

* `search_movies()`
* `create_document()`
* `delete_document()`

---

**3️⃣ Agent Layer**

ReAct agents specialized for different domains:

* Document Management Agent
* Movie Discovery Agent

---

**4️⃣ Orchestration Layer**

A **Supervisor Agent** coordinates specialized agents to complete complex user tasks.

Example flow:

```
User Request
     ↓
Supervisor Agent
     ↓
Intent Detection
     ↓
Delegation to Specialized Agent
     ↓
Tool Execution
     ↓
Response
```

---

# 🔧 Setup & Installation

## 1️⃣ Prerequisites

Ensure the following are installed:

* **Python 3.10+**
* **pip**
* **Git**

You will also need API keys for:

* OpenAI
* The Movie Database (TMDB)
* Permit.io

---

# 📥 Installation

Clone the repository and install dependencies.

```bash
git clone https://github.com/your-repo/ai-agentic-django.git
cd ai-agentic-django
pip install -r requirements.txt
```

---

# 🔑 Environment Configuration

Create a `.env` file inside the **src/** directory.

```
src/
 └── .env
```

Example configuration:

```
OPENAI_API_KEY="your_openai_key"
TMDB_API_KEY="your_tmdb_key"
PERMIT_API_KEY="your_permit_key"
```

Environment variables are loaded using **python-decouple**.

---

# 🗄 Database Initialization

The project uses **Django migrations** with a local SQLite database.

Run:

```bash
python manage.py migrate
```

To create an admin user:

```bash
python manage.py createsuperuser
```

Start the Django server:

```bash
python manage.py runserver
```

---

# 📈 Prototyping & Demonstrations

The repository includes curated **Jupyter notebooks** demonstrating system capabilities.

### Agent CRUD Operations

```
notebooks/8-agent-crud.ipynb
```

Demonstrates **document creation, retrieval, updating, and deletion via AI agents**.

---

### Multi-Agent Coordination

```
notebooks/11-multi-agent-supervisor.ipynb
```

Shows how the **Supervisor Agent delegates tasks** between assistants.

---

### Access Control

```
notebooks/12-roles-and-permissions.ipynb
```

Illustrates how **Permit.io enforces RBAC/ReBAC policies** to restrict agent actions.

---

# 📚 Reference

This project builds upon educational material from:

https://github.com/codingforentrepreneurs/django-ai-agent

---

# 📄 License

This project is provided for **educational and research purposes**.

Refer to the repository license for details.
