from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
RAW = BASE_DIR / "data" / "raw"
CLEAN = BASE_DIR / "data" / "clean"
CLEAN.mkdir(parents=True, exist_ok=True)

t1 = pd.read_csv(RAW / "t1.csv")

