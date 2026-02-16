# AI620: Fundamentals of Data Engineering Assignment 1

**Student Name:** Syed Obaidullah Hassan Chishti
**Student ID:** 25280049

# Data Engineering ELT Pipeline

A data extraction, loading, and transformation (ELT) pipeline for processing AI job market and trends data.

## Prerequisites

- Python 3.11 or higher

## Installation and Setup

### 1. Create a Python Environment

Create a virtual environment with Python 3.11+:

```bash
python -m venv venv
```

Activate the virtual environment:

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### 2. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

### 3. Configure API Credentials

Set up your Kaggle API token in the `.env` file:

1. Create a `.env` file in the project root
2. Add your Kaggle API token:

```
KAGGLE_API_TOKEN=<YOUR_KAGGLE_API_TOKEN>
```

To obtain a Kaggle API token:
- Visit [Kaggle Settings](https://www.kaggle.com/settings)
- Scroll to "API" section
- Click "Generate New Token" to get the API Key

## Running the Extraction Pipeline

Execute the pipeline to extract and process data:

```bash
python run_extraction_pipeline.py
```

This will:
- Extract data from configured sources
- Process and transform the data
- Store results in the `data/processed` directory

## Running the Transformation Pipeline
The transformation code is in transformation_pipeline.ipynb with every cell defined.
It works on two datasets, API AI Data, and Kaggle AI Data.
It contains complete pipelines for:
- Data Quality Assessment
- Transformation and Cleaning
- Exploratory Analysis and Visualization
The cleaned data is saved in /data/cleaned.

## Project Structure

```
data-engineering-elt-pipeline/
├── src/
│   ├── extract/          # Data extraction modules
│   ├── process/          # Data processing modules
├── data/
│   ├── raw/             # Raw extracted data
│   └── processed/       # Processed data
│   └── cleaned/         # Cleaned data
├── config.py            # Configuration settings
├── paths.py             # Path definitions
├── run_extraction_pipeline.py      # Main pipeline execution script
├── transformation_pipeline.ipynb      # Transformation pipeline notebook
└── requirements.txt     # Python dependencies
```

## Output
- Raw data is saved in `data/raw/<date>/`. 
- Processed data is saved in `data/processed/` in both CSV and JSON formats.
- Transformed/Cleaned data is saved in `data/cleaned/`. 
