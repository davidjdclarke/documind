# DocuMind
DocuMind is a platform for the development and delivery of LLM based ai applications. 

# Getting Started
## Installation
### Prerequisites
- Python 3.9
- Pip

### Installing
Cloning the repository
```bash
git clone https://github.com/davidjdclarke/documind
```

Setting up the virtual environment and installing the dependencies
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the application
```bash
streamlit run app.py
```

## Openai api key setup
Visit: https://platform.openai.com/ and create an account.

Export api key as an environment variable: to a `.env` file in the root of the project.
```bash .env
OPENAI_API_KEY = '<your-api-key-here>'
```
