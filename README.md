# Azure AI Foundry Test Frontend

Welcome to the Azure AI Foundry test frontend! This project provides a simple interface to experiment with Azure OpenAI models, A2A, MCP servers, and more. It is designed for rapid prototyping and testing of Azure AI capabilities.

## Features
- Streamed responses from Azure OpenAI models
- Metadata display (model, response time, token usage)
- Ready-to-use with [devcontainers](https://containers.dev/)
- Multilingual support (English/Spanish)

## Getting Started

### 1. Requirements
- [Docker](https://www.docker.com/) installed on your machine
- [Visual Studio Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### 2. Using Devcontainers
This project is fully compatible with devcontainers. Simply open the project folder in VS Code and select **"Reopen in Container"** when prompted. The development environment will be set up automatically, including all dependencies (Python, Node.js, Azure CLI, etc.).

### 3. Environment Variables
Sensitive configuration is managed via environment variables. A template file named `.fakeenv` is provided. Before running the project, you must:

1. Rename `.fakeenv` to `.env`:
   ```bash
   mv .fakeenv .env
   ```
2. Edit the `.env` file and fill in your actual Azure OpenAI endpoint and API key values:
   ```env
   AZURE_OPENAI_ENDPOINT=https://<your-endpoint>
   AZURE_OPENAI_API_KEY=<your-api-key>
   AZURE_OPENAI_DEPLOYMENT_NAME=model-router
   AZURE_OPENAI_API_VERSION=2024-12-01-preview
   ```

### 4. Install Python Dependencies
If not already installed by the devcontainer, you can install the required Python packages with:
```bash
pip install -r requirements.txt
```

### 5. Running the Project
To start the Chainlit app, run:
```bash
chainlit run main.py
```

Then, open the provided local URL in your browser to access the frontend.

## Project Structure
- `main.py` - Main application logic (Chainlit + Azure OpenAI integration)
- `chainlit.md` - Project introduction (Spanish)
- `chainlit.en.md` - Project introduction (English)
- `.fakeenv` - Example environment variables (rename to `.env`)
- `requirements.txt` - Python dependencies
- `public/` - Static assets (e.g., logo)

## Notes
- This project is for testing and demonstration purposes. Do not commit real API keys.
- The devcontainer includes all necessary tools for development and testing.

## License
MIT
