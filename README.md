# Healthcare Data Engineering Project

## Overview

This project is a data engineering pipeline built using Apache Airflow, Apache Kafka, and Apache Spark. It demonstrates how to ingest, process, and analyze healthcare data in real-time.

## Project Structure

```
project-root/
│
├── dags/                      # Airflow DAGs folder
│   ├── healthcare_pipeline.py # Airflow DAG definition file
│   └── ...
│
├── spark/                     # Spark scripts folder
│   ├── process_healthcare_data.py # Spark script for data processing
│   └── ...
│
├── docker-compose.yml         # Docker Compose configuration file
└── requirements.txt           # Python dependencies
```

## Setup Instructions

1. **Clone the Repository:**

   ```sh
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Start the Services:**

   ```sh
   docker-compose up -d
   ```

4. **Initialize the Database:**

   ```sh
   docker-compose exec airflow airflow db init
   ```

5. **Access Airflow UI:**
   Open a web browser and navigate to `http://localhost:8080` to access the Airflow UI.

6. **Run the Pipeline:**

   - Start the Airflow scheduler:
     ```sh
     docker-compose exec airflow airflow scheduler
     ```
   - Trigger the DAG `healthcare_pipeline` from the Airflow UI.

7. **Monitor Spark Jobs:**
   Spark jobs can be monitored through the Spark UI. By default, it should be accessible at `http://localhost:4040`.

## Contributors

- Sathwik Reddy Dontham (sdontham@asu.edu)
