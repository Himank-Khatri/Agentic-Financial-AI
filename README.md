# Multi-Agent Financial AI System with Phi Framework

## Overview

A multi-agent AI system using the phi framework that integrates web search and financial analysis capabilities to process and deliver information effectively. The system uses OpenAI's Groq model and various tools for web search and financial data analysis.

## Installation

### Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Install dependencies:

```bash
pip install -r requirements.txt
```

### Set environment variables:

Create a `.env` file with the following:

```makefile
GROQ_API_KEY=your_groq_api_key
PHI_API_KEY=your_phi_api_key
```

## Usage

### Run the application:

```bash
python playground.py
```

Access the playground app in your browser to interact with agents.

## Agents

### Web Search Agent

* **Role:** Searches the web for information.
* **Features:** Includes timestamps and sources in responses.

### Financial Agent

* **Role:** Processes financial data and provides analysis.
* **Features:** Uses tables and markdown formatting.

### Multi-AI Agent

* **Role:** Combines functionalities of Web Search and Financial agents.
* **Features:** Ensures up-to-date and accurate data.

# Screenshot
![image](https://github.com/user-attachments/assets/73edd032-524d-4d62-a7e4-80f65c8d2d9e)


## 