## Table of Contents

- [Setting Up Azure AI Services](#setting-up-azure-ai-services)
- [Configuration Environment Variables](#configuration-environment-variables)
- [Notebooks Setup](#notebooks-setup)
  - [Setting Up Conda Environment and Configuring VSCode for Jupyter Notebooks](#setting-up-conda-environment-and-configuring-vscode-for-jupyter-notebooks)

## Setting Up Azure AI Services

- **Azure AI Foundry**: Orchestrate experiments, runs and evaluations using Azure AI Foundry. Configure with the `AZURE_AI_FOUNDRY_CONNECTION_STRING` environment variable.
- **Azure OpenAI Service**: To generate embeddings, completions, and chat interactions, we leverage models from Azure OpenAI Service.

## Configuration Environment Variables

Before running this notebook, you must configure certain environment variables. We’ll use a `.env` file in your project root (use `.env.sample` as a template) to keep secrets out of source control.

```env
# Required: Azure AI Foundry
AZURE_AI_FOUNDRY_CONNECTION_STRING=""

# Required: Azure OpenAI Service
AZURE_AOAI_API_KEY=""
AZURE_AOAI_API_ENDPOINT=""
AZURE_AOAI_EMBEDDING_DEPLOYMENT_ID=""
AZURE_AOAI_API_VERSION=""

# Required if interacting with Blob Storage
AZURE_STORAGE_CONNECTION_STRING=""

# Required if applying OCR
AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT=""
AZURE_DOCUMENT_INTELLIGENCE_KEY=""
```

> 📌 **Note**  
> - Don’t commit your `.env` file—add it to your `.gitignore`.  
> - Replace each placeholder with the values from your Azure resources:  
>   - **Azure AI Foundry**: Connection string from your Azure AI Foundry resource.  
>   - **Azure OpenAI Service**: Key, endpoint, deployment ID and API version from your OpenAI resource.  
>   - **Azure Storage**: Connection string from the **Access keys** blade of your Storage account.  
>   - **Document Intelligence**: Endpoint and key from your Document Intelligence (Form Recognizer) resource.

## Create Conda Environment from the Repository

> **Windows**  
> 1. In a terminal, `cd` to the repo root.  
> 2. Run:  
>    ```bash
>    conda env create -f environment.yaml
>    ```  
> 3. Activate:  
>    ```bash
>    conda activate speech-ai-azure-services
>    ```

> **Linux (or WSL)**  
> 1. In a terminal, `cd` to the repo root.  
> 2. Run:  
>    ```bash
>    make create_conda_env
>    ```  
> 3. Activate:  
>    ```bash
>    conda activate speech-ai-azure-services
>    ```

## Configure VSCode for Jupyter Notebooks

1. **Install Extensions**  
>   - Python  
>   - Jupyter  

2. **Select Your Kernel**  
>   - Open the kernel dropdown (top-right of the editor) and pick `speech-ai-azure-services`.

3. **Run the Notebook**  
>   - Click **Run All** or execute cells individually.

Voila—your environment is ready! If you need additional packages, `pip install` them in a notebook cell or terminal, then restart the kernel.