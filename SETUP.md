# Development Setup Guide

This guide provides step-by-step instructions for setting up the Django AI Agent project for development.

## Prerequisites

- **Python 3.10+**
- **pip** (Python package manager)
- **Git**
- **Virtual Environment** (recommended: `venv` or `conda`)

## Step 1: Clone the Repository

```bash
git clone https://github.com/your-organization/django-ai-agent.git
cd django-ai-agent
```

## Step 2: Create and Activate Virtual Environment

### Using Python venv

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### Using conda

```bash
conda create -n django-ai python=3.10
conda activate django-ai
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Configure Environment Variables

Copy the example environment file and configure with your API keys:

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```
# Django Settings
SECRET_KEY=your-secure-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# LLM Configuration
OPENAI_API_KEY=sk-your-openai-api-key

# Third-party APIs
TMDB_API_KEY=your-tmdb-api-key
PERMIT_API_KEY=your-permit-io-api-key
PERMIT_PDP_URL=https://cloudpdp.api.permit.io
```

### Getting API Keys

**OpenAI API:**
- Visit https://platform.openai.com/api-keys
- Create a new API key in your account

**TMDB API:**
- Register at https://www.themoviedb.org/settings/api
- Generate an API key

**Permit.io:**
- Sign up at https://permit.io
- Create a workspace and get your API key

## Step 5: Initialize Django Database

```bash
cd src

# Apply migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Return to project root
cd ..
```

## Step 6: Verify Installation

Run the Django development server:

```bash
cd src
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
```

Visit http://127.0.0.1:8000/admin to verify the setup.

## Step 7: Explore with Jupyter Notebooks

The project includes interactive notebooks for learning and experimentation:

```bash
# From project root
jupyter notebook
```

Navigate to `notebook/` and start with:
1. `1-hello.ipynb` - Basic introduction
2. `6-hello-world-ai-agent.ipynb` - First AI agent
3. `8-agent-crud.ipynb` - Document operations with agents

## Project Structure

```
django-ai-agent/
├── src/
│   ├── manage.py              # Django management
│   ├── cfehome/               # Django project configuration
│   ├── documents/             # Documents app
│   ├── ai/                    # AI agent system
│   │   ├── agents.py          # Agent definitions
│   │   ├── llms.py            # LLM configuration
│   │   ├── supervisors.py     # Supervisor agents
│   │   └── tools/             # LangChain tools
│   ├── tmdb/                  # TMDB API client
│   └── mypermit/              # Permit.io integration
├── notebook/                  # Jupyter prototyping environment
├── requirements.txt           # Python dependencies
├── .env.example               # Environment configuration template
└── README.md                  # Project documentation
```

## Common Commands

### Database Management

```bash
# Run migrations
python manage.py migrate

# Create migration for changes
python manage.py makemigrations

# Revert migrations
python manage.py migrate documents zero
```

### Development

```bash
# Start development server
python manage.py runserver

# Django shell
python manage.py shell

# Create superuser
python manage.py createsuperuser
```

### Jupyter Notebooks

```bash
# Start Jupyter
jupyter notebook

# List running Jupyter instances
jupyter notebook list
```

## Troubleshooting

### Missing API Keys

If you see `OPENAI_API_KEY not found`, ensure your `.env` file is properly configured in the `src/` directory.

### Database Errors

If you encounter migration errors:
```bash
# Reset database (be careful in production!)
rm src/db.sqlite3
python manage.py migrate
```

### Virtual Environment Issues

Ensure you're using the correct Python:
```bash
# Check active Python
which python
python --version

# Verify pip uses correct environment
pip --version
```

## Next Steps

1. Read [README.md](README.md) for project overview
2. Explore the notebooks in `notebook/` folder
3. Review the agent implementation in `src/ai/agents.py`
4. Check [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines

## Support

For issues and questions:
1. Check existing issues on GitHub
2. Create a new issue with detailed description
3. Include error messages and environment details
