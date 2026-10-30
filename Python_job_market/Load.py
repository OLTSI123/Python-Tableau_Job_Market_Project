
import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

csv_path = BASE_DIR / "remote_jobs_clean.csv"

db_path = BASE_DIR / "remote_jobs.db"

if not csv_path.exists():
    raise FileNotFoundError(
        f"Dataa ei löydy: {csv_path}. "
        "Aja ensin Extract.py ja Transform.py."
    )

df = pd.read_csv(csv_path)

with sqlite3.connect(db_path) as conn:
    df.to_sql(
        name="remote_jobs",
        con=conn,
        if_exists="replace",
        index=False
    )

print(f"Tietokantaan tallennettuja rivejä: {len(df)}")
print(f"Tietokanta: {db_path}")
