# RAG AZURE HTTP QDRANT 🧑‍💻

<p align="center">
  <img width="976" alt="azure" src="https://github.com/user-attachments/assets/cbe4b7d9-e940-4e84-bbac-834fd17acbf8">
</p>

This repository contains a full Q&A pipeline using LangChain framework, Qdrant as vector database and Azure Function with HttpTrigger. The data used are research papers that can be loaded into the vector database, and the Azure Functions processes the request using the retrieval and generation logic. Therefore it can use any other research paper from Arxiv.

The main steps taken to build the RAG pipeline can be summarized as follows:

* **Data Ingestion**: load data from https://arxiv.org

* **Indexing**: RecursiveCharacterTextSplitter for indexing in chunks

* **Vector Store**: Qdrant inserting metadata

* **QA Chain Retrieval**: RetrievalQA

* **Azure Function**: Process the request with HttpTrigger
  
Feel free to ⭐ and clone this repo 😉

## Tech Stack

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenAI](https://img.shields.io/badge/OpenAI-74aa9c?style=for-the-badge&logo=openai&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=white)
![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

## Project Structure

The project has been structured with the following files:

- `.env_sample`: sample environmental variables
- `Makefile`: install requirements, formating, linting, and clean up
- `pyproject.toml`: linting and formatting using ruff
- `requirements.txt:` project requirements
- `create_vector_store.py:` script to create the collection in Qdrant
- `function_app.py:` Azure function app
- `rag_app.py:` RAG Logic
- `host.json:` metadata file with configuration options for the function app for deployment
- `local.settings.json`: metadata file with configuration options for the function app locally
- `deploy.sh:` script to create and publish the function


## Project Set Up

The Python version used for this project is Python 3.10. You can follow along the medium article.

1. Clone the repo (or download it as a zip file):

   ```bash
   git clone https://github.com/benitomartin/rag-azure-http.git
   ```

2. Create the virtual environment named `main-env` using Conda with Python version 3.10:

   ```bash
   conda create -n main-env python=3.10
   conda activate main-env
   ```
   
3. Execute the `Makefile` script and install the project dependencies included in the requirements.txt:

    ```bash
    pip install -r requirements.txt

    or
 
    make install
    ```

4. Create **Azure Account** and install **Azure CLI** and **Functions Core Tools**.

5. Test the function locally

  ```bash
   func start
  ```

  ```bash
   curl -X POST "http://localhost:7071/api/req" \
      -H "Content-Type: application/json" \
      -d '{"query": "positional encoding"}'
   ```

<p align="center">
  <img width="976" alt="azure" src="https://github.com/user-attachments/assets/f6c6bdee-327b-4397-9c18-69b2fa86e000">
</p>

6. Create and publish the App: Make sure the `.env` file is complete and run the `deploy.sh` script  

   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```

   ```bash
   curl -X POST https://app-rag-function.azurewebsites.net/api/req \
      -H "Content-Type: application/json" \
      -d '{"query": "Positional Encoding"}'
   ```

<p align="center">
  <img width="976" alt="azure" src="https://github.com/user-attachments/assets/096c9cbd-b51a-4e5c-b681-207b3c8657fe">
</p>
