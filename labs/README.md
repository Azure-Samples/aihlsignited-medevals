## **🧪 Azure AI Evaluation Labs**

These hands‑on labs guide you through building an end‑to‑end evaluation pipeline on Azure AI Foundry—from using built‑in metrics to deploying custom evaluators, enforcing schemas, and integrating everything into CI/CD.

### **🛠️ Lab Modules Overview**

Complete the labs in sequence for a streamlined learning path.

#### **🧪 Lab 01: Foundry Basics + Custom Evaluations**
- **[🧾 Notebook – Foundry Basics + Custom Evaluations](01-foundry-basics-custom-evaluations.ipynb)**  
  You will:  
  - Authenticate and initialize an Azure AI Foundry project  
  - Ingest sample data and tag it for grouping  
  - Run built‑in metrics (relevance, coherence, etc.)  
  - Explore the evaluator interface and author holistic scoring logic  
  - Integrate open‑source packages (EvalAI, PromptEval)  
  - Package and upload your custom evaluator to Foundry  

#### **🧪 Lab 02: Search Evaluations (Upload & Analyze)**
- **[🧾 Notebook – Search Evaluations (Upload & Analyze)](02-search-evaluations-upload-analyze.ipynb)**  
  You will:  
  - Prepare query–document datasets for search evaluation  
  - Execute built‑in and custom search metrics (precision, recall, NDCG)  
  - Visualize precision/recall curves and metric distributions  
  - Register search evaluators in Azure AI Foundry  

#### **🧪 Lab 03: Repeatable Evaluations & CI/CD**
- **[🧾 Notebook – Repeatable Evaluations & CI/CD](03-repeatable-evaluations-ci-cd.ipynb)**  
  You will:  
  - Define JSON/YAML schemas for evaluation runs  
  - Build deterministic pipelines that load and validate configs  
  - Wrap metrics in PyTest for baseline assertions  
  - Add GitHub Actions to catch metric drift in CI/CD  

### **🚀 What’s Next?**

Once you’ve completed the labs, head over to the [**🏥 Use Cases**](../usecases/README.md) section to see how these foundational concepts are applied in real-world healthcare workflows.

Happy evaluating! 🎉
