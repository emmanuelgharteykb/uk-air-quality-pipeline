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
- [x] Day 3: Workflow automation with GitHub Actions.
- [x] Day 4: Live Power BI dashboard development.

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

## 🛠 Technical Skills Demonstrated (Day 3)

### 🤖 Workflow Orchestration & CI/CD
* **GitHub Actions Implementation:** Engineered a production-grade YAML workflow to automate the ETL pipeline. The system is configured to trigger on a `cron` schedule (Daily at 09:00 UTC) and via `workflow_dispatch` for manual testing.
* **Linux Runner Configuration:** Orchestrated the automated provisioning of ephemeral Ubuntu environments, ensuring Python dependency parity between local development and cloud execution.
* **Automated Dependency Management:** Optimized `requirements.txt` to a lean, production-ready state, reducing build times and eliminating system-level conflicts (e.g., resolving `bcc` kernel headers errors).

### 🔐 Enterprise-Grade Secret Management
* **Encrypted Vault Integration:** Transitioned sensitive credentials (GCP Service Account Keys, API Keys, and Project IDs) from local `.env` files to **GitHub Encrypted Secrets**.
* **Runtime Secret Injection:** Developed the pipeline logic to dynamically reconstruct the `gcp-key.json` authentication file at runtime, ensuring no credentials persist in the repository history.
* **Workflow Scoping:** Managed granular Personal Access Token (PAT) permissions, specifically implementing the `workflow` scope to maintain secure version control over CI/CD configurations.

### 📈 System Monitoring & Reliability
* **Stateless Execution:** Designed the script to be entirely "stateless," allowing the automation to fail or succeed without corrupting the historical data stored in BigQuery.
* **Build Status Monitoring:** Utilized GitHub Action logs as a centralized debugging console, providing full traceability of network requests and cloud write operations.
* **Data Continuity:** Successfully verified "hands-off" data ingestion, observing real-time fluctuations in urban $NO_2$ and $PM_{2.5}$ levels captured automatically by the "Robot."

## 🛠 Technical Skills Demonstrated (Day 4)

### 📊 Business Intelligence & Data Visualization
* **Cloud-Native BI Integration:** Orchestrated a live connection between Google BigQuery and Looker Studio using the `uk_aqi_logs` table, enabling real-time data streaming from the cloud warehouse to the visualization layer.
* **Metric Engineering:** Developed calculated fields and custom aggregations, such as Average AQI, to transform raw telemetry into high-level KPI scorecards for executive reporting.
* **Time-Series Analysis:** Engineered multi-city trend charts to monitor fluctuations in $PM_{2.5}$ and $NO_2$ levels, providing longitudinal insights into urban pollution patterns.
* **Interactive Data Storytelling:** Implemented dynamic tooltips and breakdown dimensions by city, allowing stakeholders to drill down into specific data points for London, Birmingham, Manchester, and Glasgow.

### ⚙️ Data Modeling & System Validation
* **Temporal Data Granularity:** Optimized time-series charts by configuring the timestamp dimension to group data by "Date," effectively transforming discrete API "pings" into continuous trend lines.
* **Automated Data Continuity:** Verified system reliability by observing successful data fetching and dashboard updates over a 48-hour "hands-off" period, confirming the stability of the GitHub Actions orchestration.
* **Schema Alignment:** Synchronized the Looker Studio data schema with BigQuery fields (AQI, City, $NO_2$, $PM_{2.5}$, and Timestamp) to ensure 100% data integrity throughout the visualization process.
