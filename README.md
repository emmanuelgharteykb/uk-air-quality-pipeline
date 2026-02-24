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
- [x] Day 2: Cloud Database (BigQuery) setup and schema design.
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

## 🛠 Technical Skills Demonstrated (Day 2)

### ☁️ Cloud Infrastructure & Data Warehousing
* **Google BigQuery Integration:** Engineered a high-performance "Writer" function to stream live DataFrames directly into a BigQuery table using the `google-cloud-bigquery` library and `pyarrow` engine.
* **Schema Design & Management:** Architected a relational table structure in the cloud to support time-series analysis, enabling the tracking of air quality fluctuations over time.
* **IAM & Security Orchestration:** Configured Google Cloud Service Accounts with granular IAM roles. Managed secure authentication via JSON key files, adhering to the principle of least privilege.


### 🔒 Professional DevOps Hygiene
* **Secrets Management (Level 2):** Expanded the security layer to include Cloud Project IDs and Dataset IDs within `.env`, ensuring the codebase is entirely generic and portable.
* **Environment Protection:** Rigorously maintained `.gitignore` protocols to prevent the accidental exposure of Cloud Service Account keys to public repositories.
* **Error Resilience:** Implemented `try-except` blocks to handle network timeouts and authentication failures, ensuring the pipeline provides clear logs for troubleshooting.

### 📊 Data Integrity & Validation
* **Idempotency & Appending:** Verified that the pipeline successfully appends new observations without duplicating historical data, maintaining a clean "Source of Truth" in the warehouse.
* **Validation Testing:** Performed live "end-to-end" tests, confirming that real-time API value changes (NO2 and PM2.5) were accurately reflected in the BigQuery Preview layer.
