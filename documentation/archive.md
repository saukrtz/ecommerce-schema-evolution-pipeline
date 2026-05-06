# Project Archive: Schema Evolution Pipeline

## Iteration 1: Project Initialization
- **Action**: Setup project structure, `.gitignore`, `.env`, and `README.md`.
- **Status**: Completed.
- **Problems Faced**: Permission issues with direct Python execution via terminal.
- **Optimizations**: Created datasets manually using `write_to_file` to bypass terminal execution blocks.


## Iteration 3: Traditional Approach (Step 1)
- **Action**: Created `src/step1_traditional.py` to demonstrate the problem of schema mismatch.
- **Status**: Completed.
- **Observations**: Day 1 records lack the 'brand' column, resulting in NaNs after a simple concat.
- **Problems Faced**: None in script creation.

## Iteration 5: Full Pipeline Implementation (Steps 5-7)
- **Action**: Created `src/pipeline.py` to merge all 3 days, handle missing values for `brand` and `discount`, and export the final dataset.
- **Status**: Completed.
- **Optimizations**: Used a dictionary for `fillna` to handle multiple columns efficiently.

## Iteration 6: PySpark Concept (Step 8)
- **Action**: Created `src/pyspark_concept.py` to document the industry-standard `mergeSchema` approach.
- **Status**: Completed (Conceptual).

## Iteration 8: Lab Exercises (Advanced Scenarios)
- **Action**: Created `src/exercises.py` with assistance from **Llama 3.1 8b**.
- **Scenarios Handled**:
    1. **Column Addition**: Added `rating` and imputed missing values for historical records.
    2. **Column Removal**: Safely handled files missing the `price` column.
    3. **Type Change**: Implemented data cleaning for string-based prices (e.g., "$10") to ensure numeric consistency across the pipeline.
- **Status**: Completed.
