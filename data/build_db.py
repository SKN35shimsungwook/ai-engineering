"""Merge per-batch source CSVs into one sources.csv and load them into a SQLite DB.

Usage:
    python data/build_db.py

Reads every data/sources_*.csv (one per research batch), concatenates them,
writes the merged result to data/sources.csv, and loads it into data/sources.db
(table: sources) for the Streamlit app's "source DB" browser.
"""

from __future__ import annotations

import glob
import os
import sqlite3

import pandas as pd

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
MERGED_CSV = os.path.join(DATA_DIR, "sources.csv")
DB_PATH = os.path.join(DATA_DIR, "sources.db")

COLUMNS = [
    "chapter_num",
    "chapter_name",
    "slide_file",
    "source_title",
    "source_url",
    "source_type",
    "key_point",
]


def main() -> None:
    batch_files = sorted(glob.glob(os.path.join(DATA_DIR, "sources_*.csv")))
    if not batch_files:
        raise SystemExit(f"No data/sources_*.csv batch files found in {DATA_DIR}")

    frames = []
    for path in batch_files:
        df = pd.read_csv(path, dtype=str).fillna("")
        missing = [c for c in COLUMNS if c not in df.columns]
        if missing:
            raise SystemExit(f"{path} is missing columns: {missing}")
        frames.append(df[COLUMNS])

    merged = pd.concat(frames, ignore_index=True)
    merged.drop_duplicates(inplace=True)
    merged.insert(0, "id", range(1, len(merged) + 1))
    merged["chapter_num"] = merged["chapter_num"].astype(str).str.zfill(2)

    merged.to_csv(MERGED_CSV, index=False, encoding="utf-8-sig")

    with sqlite3.connect(DB_PATH) as conn:
        merged.to_sql("sources", conn, if_exists="replace", index=False)
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_sources_chapter ON sources(chapter_num)"
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_sources_type ON sources(source_type)"
        )

    print(f"Merged {len(batch_files)} batch file(s) -> {len(merged)} rows")
    print(f"Wrote {MERGED_CSV}")
    print(f"Wrote {DB_PATH}")


if __name__ == "__main__":
    main()
