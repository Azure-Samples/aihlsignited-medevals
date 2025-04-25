## **🧪 Azure AI Evaluation Labs**

Welcome to the **Azure AI Evaluation Labs**! These hands‑on exercises walk you through building a robust, end‑to‑end evaluation pipeline on Azure AI Foundry—from leveraging built‑in metrics to authoring custom evaluators, enforcing schemas, and integrating into CI/CD.  

---

### **🛠️ Lab Modules Overview**

Each lab builds on the last, focusing exclusively on evaluation processes. Complete them in order for a seamless learning path.

#### **🧪 Lab 01: AI Foundry Basics (Pre‑built Evaluations)**
- **[🧾 Notebook – AI Foundry Basics (Pre‑built Evaluations)](01-foundry-prebuilt-evaluations.ipynb)**  
  In this lab you’ll:
  - Authenticate and initialize an Azure AI Foundry project  
  - Ingest sample data and apply metadata tags for grouping  
  - Run built‑in evaluation metrics (e.g., relevance, coherence)  
  - Visualize metric distributions and derive insights  

#### **🧪 Lab 02: Custom Evaluations (Build & Deploy)**
- **[🧾 Notebook – Custom Evaluations (Build & Deploy)](02-custom-evaluations-build-deploy.ipynb)**  
  In this lab you’ll:
  - Explore the Foundry Evaluator interface  
  - Implement holistic scoring logic (e.g., clinical‑accuracy)  
  - Integrate open‑source evaluation packages (EvalAI, PromptEval)  
  - Package and upload your custom evaluator to AI Foundry  

#### **🧪 Lab 03: Search Evaluations (Upload & Analyze)**
- **[🧾 Notebook – Search Evaluations (Upload & Analyze)](03-search-evaluations-upload-analyze.ipynb)**  
  In this lab you’ll:
  - Prepare query–document datasets for search evaluation  
  - Execute built‑in and custom search metrics (precision, recall)  
  - Visualize precision/recall and NDCG curves  
  - Register your search evaluators in Azure AI Foundry  

#### **🧪 Lab 04: Repeatable Evaluations & CI/CD**
- **[🧾 Notebook – Repeatable Evaluations & CI/CD](lab-03-repeatable-evaluations-ci-cd.ipynb)**  
  In this lab you’ll:
  - Define a JSON/YAML schema for evaluation runs  
  - Build a deterministic pipeline that loads and validates configs  
  - Wrap your metrics in PyTest tests for baseline assertions  
  - Configure GitHub Actions to catch metric drift in CI/CD  

---

### **📚 Additional Notes**

- 💡 **Modular & Sequential**: Each lab is designed to be run in order, but can also stand alone for targeted learning.  
- ⚙️ **Prerequisites**: Check the top of each notebook for environment setup, Azure resource requirements, and Python package installs.  
- 📖 **Further Reading**: Refer to the Azure AI Foundry docs for deeper dives into evaluator APIs and deployment patterns.

---

### **🚀 What’s Next?**

After completing these labs, you’ll have a production‑ready evaluation suite. Consider extending this work to:
- Automate periodic regression testing of your AI models  
- Integrate with dashboards for real‑time metric monitoring  
- Expand use case tutorials to other clinical taxonomy standards  

Happy evaluating! 🎉  