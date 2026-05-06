# E-commerce Schema Evolution Pipeline

## Lab Objective
Build a pipeline that handles changing product schema over time. Automatically detects new columns, merges schemas without breaking the pipeline, and ensures backward compatibility.

## Tech Stack
- **Language**: Python
- **Libraries**: Pandas
- **LLM Assistance**: Groq (Llama 3.1 8b)

## Project Structure
- `src/`: Source code for the pipeline and utilities.
- `data/`: Sample datasets for Day 1, 2, and 3.
- `documentation/`: Project logs and archive.

## How to Run
1. Ensure `pandas` and `python-dotenv` are installed.
2. Run the pipeline script: `python src/pipeline.py`
