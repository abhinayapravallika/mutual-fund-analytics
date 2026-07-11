import os
import requests
import pandas as pd

schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841,
    "UTI_Flexi_Cap": 120716,
    "Mirae_Asset_Large_Cap": 118834,
    "DSP_Top100_Equity": 118825,
    "ABSL_Frontline_Equity": 119533
}

# Ensure the output directory exists
os.makedirs("data/raw", exist_ok=True)

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    
    try:
        # Added a 10-second timeout to handle slow networks gracefully
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Check if "data" key actually exists in the API response
        if "data" in data and len(data["data"]) > 0:
            df = pd.DataFrame(data["data"])
            
            # CRITICAL FIX: Add identifier columns so the data isn't anonymous
            df["scheme_code"] = code
            df["scheme_name"] = name
            
            # Reorder columns to look clean: code, name, date, nav
            df = df[["scheme_code", "scheme_name", "date", "nav"]]
            
            filename = f"data/raw/{name}.csv"
            df.to_csv(filename, index=False)
            print(f"✅ Saved {name} ({df.shape[0]} rows)")
        else:
            print(f"⚠️ No data found for {name}")
            
    except Exception as e:
        print(f"❌ Failed to fetch {name}: {e}")