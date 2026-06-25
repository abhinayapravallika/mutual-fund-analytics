import os
import pandas as pd
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
DATA_DIR = "data/raw"

def inspect_datasets():
    print("=" * 60)
    print("🚀 Day 1: Starting Local Data Ingestion & Inspection")
    print("=" * 60 + "\n")
    
    for file_name in CSV_FILES:
        file_path = os.path.join(DATA_DIR, file_name)
        if not os.path.exists(file_path):
            print(f"❌ Error: {file_name} not found in '{DATA_DIR}/'. Skipping...")
            print("-" * 50)
            continue
            
        print(f"📖 Inspecting: {file_name}")
        try:
            df = pd.read_csv(file_path)
            print(f"   🔹 Dimensions (Rows, Columns): {df.shape}")
            print("   🔹 Data Types:")
            for col, dtype in df.dtypes.items():
                print(f"      - {col}: {dtype}")
            print("   🔹 Sample Data (Head):")
            print(df.head(3)) 
            missing_count = df.isnull().sum().sum()
            if missing_count > 0:
                print(f"   ⚠️ Alert: Found {missing_count} total missing values in this file.")
                
        except Exception as e:
            print(f"   ❌ Failed to process file due to error: {e}")
            
        print("-" * 60 + "\n")
def explore_fund_master():
    fund_master_path = os.path.join(DATA_DIR, "01_fund_master.csv")
    if os.path.exists(fund_master_path):
        try:
            df = pd.read_csv(fund_master_path)
            print("\n" + "=" * 60)
            print("🔍 Day 1: Fund Master Exploration")
            print("=" * 60)
            for col in ['fund_house', 'category', 'sub_category', 'risk_grade']:
                if col in df.columns:
                    print(f"\n🔹 Unique values in '{col}' (Top 10):")
                    print(df[col].unique()[:10])
                else:
                    print(f"\n⚠️ Column '{col}' not found in 01_fund_master.csv")
            print("\n" + "=" * 60 + "\n")
        except Exception as e:
            print(f"❌ Failed to explore fund master due to error: {e}")


if __name__ == "__main__":
    inspect_datasets() 
    
    explore_fund_master()
