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
OPENAI_API_KEY = '&lt;your-api-key-here&gt;'
```

**ChatGPT**: DocuMind

DocuMind is a comprehensive platform designed for the development, deployment, and delivery of AI applications leveraging the power of large language models (LLMs) such as OpenAI's GPT series. The platform aims to provide a user-friendly interface for integrating AI capabilities into various domains such as content generation, natural language processing, and data analysis.Getting Started

This section will guide you through the process of setting up your environment and running DocuMind on your local machine.InstallationPrerequisites

To get started with DocuMind, ensure that you have the following software installed on your machine:Python 3.9 or higherPip (Python package installer)Installing

Follow these steps to set up DocuMind on your local machine:1. Clone the repository

First, clone the DocuMind repository to your local machine using the following command:bash
```bash
git clone https://github.com/davidjdclarke/documind
```2. Set up a virtual environment

Navigate to the cloned repository and set up a virtual environment to manage dependencies. This ensures that the required packages don't interfere with your system's global Python installation. Use the following commands:bash
```bash
cd documind
python -m venv venv
```3. Activate the virtual environment

Activate the virtual environment using the appropriate command for your operating system:

For Linux and macOS:bash
```bash
source venv/bin/activate
```

For Windows:bash
```bash
venv\Scripts\activate
```
4. Install the required dependencies

With the virtual environment activated, install the necessary packages by running:bash
```bash
pip install -r requirements.txt
```
Running the application

To run the DocuMind application, use the following command:bash
```bash
streamlit run app.py
```

This will launch the application in your default web browser.OpenAI API Key Setup

To enable the AI capabilities of DocuMind, you will need an API key from OpenAI. Follow these steps:1. Create an OpenAI account

Visit https://platform.openai.com/signup and sign up for an account. Once you have created an account and logged in, navigate to the API Keys section in the dashboard.2. Obtain your API key

Copy your API key from the API Keys section.3. Set up the API key as an environment variable

Create a ```.env``` file in the root directory of the DocuMind project (the same directory as ```app.py```). Inside the ```.env``` file, add the following line, replacing ```&lt;your-api-key-here&gt;``` with your OpenAI API key:bash
```bash
OPENAI_API_KEY='&lt;your-api-key-here&gt;'
```

Save the ```.env``` file, and you're ready to go! DocuMind will now have access to the OpenAI API for its AI functionalities.
