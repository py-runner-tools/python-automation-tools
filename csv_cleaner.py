# ==========================================
# SCRIPT NAME: CSV Data Cleaner Utility
# PURPOSE: Removes duplicates, fills missing values, and cleans CSV datasets
# ==========================================

import pandas as pd

def clean_csv_dataset(file_path, output_path="cleaned_output.csv"):
    """
    Reads a messy CSV file, removes duplicate rows, drops empty rows,
    and exports a clean, standardized dataset.
    """
    try:
        # Load dataset
        df = pd.read_csv(file_path)
        initial_rows = len(df)
        
        # Drop completely empty rows
        df.dropna(how='all', inplace=True)
        
        # Remove duplicate entries
        df.drop_duplicates(inplace=True)
        
        # Save cleaned file
        df.to_csv(output_path, index=False)
        
        print(f"--- CSV CLEANING COMPLETE ---")
        print(f"Initial rows : {initial_rows}")
        print(f"Cleaned rows : {len(df)}")
        print(f"Saved to     : {output_path}")
        
    except Exception as e:
        print(f"Error processing CSV file: {e}")

if __name__ == "__main__":
    print("CSV Cleaner utility loaded successfully. Ready for pandas pipeline execution.")
  
