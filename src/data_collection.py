"""Download macroeconomic data from the World Bank API."""
from pathlib import Path

import pandas as pd
import wbgapi as wb

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "raw" / "macro_data.csv"

CFA = ["BFA", "CIV", "SEN", "MLI", "BEN"]
FLOATING = ["NGA", "GHA", "KEN", "ZAF"]
INDICATORS = {
    "FP.CPI.TOTL.ZG": "inflation",
    "NY.GDP.MKTP.KD.ZG": "gdp_growth",
}


def download() -> pd.DataFrame:
    """Return a country-year panel with inflation and GDP growth."""
    df = wb.data.DataFrame(
        list(INDICATORS.keys()),
        CFA + FLOATING,
        time=range(2000, 2025),
        columns="series",
        numericTimeKeys=True,
    ).reset_index()
    df = df.rename(columns={"economy": "country", "time": "year", **INDICATORS})
    df["group"] = df["country"].apply(lambda c: "CFA" if c in CFA else "Floating")
    return df


if __name__ == "__main__":
    data = download()
    print(data.head())
    print(data.shape)
    print(data.isna().sum())
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(OUTPUT, index=False)
    print(f"Saved: {OUTPUT}")