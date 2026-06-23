import os
import pandas as pd

# The 10 files listed in your Bluestock Mutual Fund Capstone Project
CSV_FILES = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

# Path to where your raw data sits
DATA_DIR = "data/raw"

def inspect_datasets():
    print("=" * 60)
    print("🚀 Day 1: Starting Local Data Ingestion & Inspection")
    print("=" * 60 + "\n")
    
    for file_name in CSV_FILES:
        file_path = os.path.join(DATA_DIR, file_name)
        
        # Check if the file actually exists in the directory
        if not os.path.exists(file_path):
            print(f"❌ Error: {file_name} not found in '{DATA_DIR}/'. Skipping...")
            print("-" * 50)
            continue
            
        print(f"📖 Inspecting: {file_name}")
        try:
            # Load the CSV
            df = pd.read_csv(file_path)
            
            # 1. Print Shape
            print(f"   🔹 Dimensions (Rows, Columns): {df.shape}")
            
            # 2. Print Data Types
            print("   🔹 Data Types:")
            for col, dtype in df.dtypes.items():
                print(f"      - {col}: {dtype}")
                
            # 3. Print First Few Rows
            print("   🔹 Sample Data (Head):")
            print(df.head(3))  # Clean display of top 3 records
            
            # Quick check for obviously empty cells
            missing_count = df.isnull().sum().sum()
            if missing_count > 0:
                print(f"   ⚠️ Alert: Found {missing_count} total missing values in this file.")
                
        except Exception as e:
            print(f"   ❌ Failed to process file due to error: {e}")
            
        print("-" * 60 + "\n")

if __name__ == "__main__":
    inspect_datasets()