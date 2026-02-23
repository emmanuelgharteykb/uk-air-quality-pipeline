# UK Air Quality Data Pipeline (ESG Analytics)

## 📌 Project Overview
This project is an automated **End-to-End Data Pipeline** designed to monitor and analyze environmental impact across major UK cities (London, Birmingham, Glasgow, and Manchester). 

By transitioning from static datasets to a **live-streaming architecture**, this project demonstrates how to build a scalable monitoring system that provides actionable insights into urban pollution levels ($NO_2$, $PM_{2.5}$, and $O_3$).

## 🛠️ Tech Stack
* **Extraction:** Python (Requests, Pandas)
* **API:** OpenWeatherMap Air Pollution API
* **Orchestration:** GitHub Actions (CI/CD for Data)
* **Storage/Cloud:** Google BigQuery (Data Warehouse)
* **Visualization:** Power BI

## 🚀 Key Features
* **Automated Extraction:** A scheduled Python script fetches real-time Air Quality Index (AQI) metrics daily.
* **Cloud Integration:** Data is cleaned and pushed directly to a BigQuery table, creating a historical record of pollution trends.
* **Infrastructure as Code:** Uses GitHub Actions to automate the workflow, removing the need for manual data handling.
* **ESG Focused:** Built with Sustainability and Governance reporting in mind.

## 📈 Roadmap
- [x] Day 1: API Integration and local Python extraction.
- [ ] Day 2: Cloud Database (BigQuery) setup and schema design.
- [ ] Day 3: Workflow automation with GitHub Actions.
- [ ] Day 4: Live Power BI dashboard development.

## 🛠 Technical Skills Demonstrated (Day 1)

### 🛰️ Data Engineering & ETL
* **REST API Integration:** Engineered an extraction layer using Python `requests` to consume live JSON payloads from OpenWeatherMap.
* **Data Transformation:** Leveraged `pandas` to normalize nested JSON objects into structured DataFrames, ensuring data integrity for downstream analytics.
* **ESG Analytics:** Targeted specific environmental metrics ($PM_{2.5}$, $NO_2$, $O_3$) to align with corporate Sustainability and Governance reporting standards.

### ⚙️ DevOps & System Architecture
* **Environment Isolation:** Implemented Python Virtual Environments (`venv`) to manage dependencies and adhere to PEP 668 (externally-managed environments) standards.
* **Security Best Practices:** Utilized `python-dotenv` for secrets management, ensuring API credentials remain decoupled from the source code.
* **Version Control:** Employed a professional Git Flow, utilizing feature branches and Pull Requests to manage the codebase.
* **Dependency Management:** Generated `requirements.txt` to ensure 100% reproducibility across different development environments.
