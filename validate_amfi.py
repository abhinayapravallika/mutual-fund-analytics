import os
import pandas as pd

def validate_codes():
    print("🔍 Starting AMFI Code Validation...")
    
    master_path = "data/raw/01_fund_master.csv"
    history_path = "data/raw/02_nav_history.csv"
    
    if not os.path.exists(master_path) or not os.path.exists(history_path):
        print("❌ Error: Missing required CSV files in data/raw/")
        return

    master_df = pd.read_csv(master_path)
    history_df = pd.read_csv(history_path)
    master_col = 'amfi_code'
    history_col = 'scheme_code' if 'scheme_code' in history_df.columns else 'amfi_code'
    
    if master_col not in master_df.columns:
        print(f"❌ Error: Could not find '{master_col}' in 01_fund_master.csv")
        print(f"Available columns: {list(master_df.columns)}")
        return
        
    if history_col not in history_df.columns:
        print(f"❌ Error: Could not find code column in 02_nav_history.csv")
        print(f"Available columns: {list(history_df.columns)}")
        return

    print(f"✅ Matching Master column ['{master_col}'] 🔄 History column ['{history_col}']")

    master_codes = set(master_df[master_col].dropna().unique())
    history_codes = set(history_df[history_col].dropna().unique())
    
    missing_in_history = master_codes - history_codes
    
    print("\n" + "=" * 50)
    print("📊 DATA QUALITY SUMMARY")
    print("=" * 50)
    print(f"Total Unique Schemes in Master : {len(master_codes)}")
    print(f"Total Unique Schemes in History: {len(history_codes)}")
    
    if len(missing_in_history) == 0:
        print("🟢 Success: Every code in fund_master exists in nav_history.")
    else:
        print(f"⚠️  Alert: {len(missing_in_history)} codes from fund_master are missing in nav_history.")
        print(f"📋 Sample missing codes: {list(missing_in_history)[:5]}")
    print("=" * 50)

if __name__ == "__main__":
    validate_codes()