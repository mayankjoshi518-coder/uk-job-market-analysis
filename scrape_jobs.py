"""
scrape_jobs.py — UK BA/DA job market scraping and analysis pipeline
Scrapes job listings, cleans data, and produces summary statistics.
Author: Mayank Joshi
"""

import pandas as pd
import numpy as np
import re
from collections import Counter


# ── Data Loading ──────────────────────────────────────────────

def load_scraped_data(filepath: str = "uk_jobs_data.csv") -> pd.DataFrame:
      """Load previously scraped job listings CSV."""
      df = pd.read_csv(filepath)
      print(f"Loaded {len(df):,} job listings")
      return df


# ── Data Cleaning ─────────────────────────────────────────────

def clean_salary(salary_str: str) -> float:
      """Extract numeric salary from string like '£35,000 - £45,000'."""
      if pd.isna(salary_str):
                return np.nan
            numbers = re.findall(r"[\d,]+", str(salary_str))
    numbers = [int(n.replace(",", "")) for n in numbers if int(n.replace(",", "")) > 1000]
    if not numbers:
              return np.nan
          return np.mean(numbers)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
      """Standardise columns, parse salaries, and drop duplicates."""
    df = df.copy()
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    if "salary" in df.columns:
              df["salary_numeric"] = df["salary"].apply(clean_salary)

    if "location" in df.columns:
              df["region"] = df["location"].str.extract(r"(London|Manchester|Birmingham|Leeds|Bristol|Edinburgh|Glasgow|Cardiff|Remote)", expand=False)
              df["region"] = df["region"].fillna("Other")

    if "work_type" in df.columns:
              df["work_type"] = df["work_type"].str.strip().str.title()

    df.drop_duplicates(subset=["title", "company"], keep="first", inplace=True)
    print(f"Cleaned dataset: {len(df):,} unique listings")
    return df


# ── Skill Extraction ──────────────────────────────────────────

SKILL_KEYWORDS = [
      "python", "sql", "excel", "tableau", "power bi", "r",
      "pandas", "numpy", "scikit-learn", "machine learning",
      "data visualisation", "statistics", "agile", "scrum",
      "jira", "confluence", "git", "aws", "azure", "gcp",
      "looker", "dbt", "spark", "airflow", "etl",
]


def extract_skills(df: pd.DataFrame, text_col: str = "description") -> pd.DataFrame:
      """Count skill mentions across all job descriptions."""
    if text_col not in df.columns:
              print(f"Column '{text_col}' not found — skipping skill extraction.")
              return pd.DataFrame()

    skill_counts = Counter()
    for desc in df[text_col].dropna():
              desc_lower = desc.lower()
              for skill in SKILL_KEYWORDS:
                            if skill in desc_lower:
                                              skill_counts[skill] += 1

                    skills_df = pd.DataFrame(
                              skill_counts.most_common(),
                              columns=["skill", "mentions"]
                    )
    skills_df["pct_of_listings"] = (skills_df["mentions"] / len(df) * 100).round(1)
    return skills_df


# ── Summary Statistics ────────────────────────────────────────

def salary_summary(df: pd.DataFrame) -> pd.DataFrame:
      """Median salary by region."""
    if "salary_numeric" not in df.columns or "region" not in df.columns:
              return pd.DataFrame()
    summary = (
              df.groupby("region")["salary_numeric"]
              .agg(["median", "mean", "count"])
              .round(0)
              .sort_values("median", ascending=False)
              .reset_index()
    )
    summary.columns = ["Region", "Median Salary", "Mean Salary", "Listings"]
    return summary


def work_type_breakdown(df: pd.DataFrame) -> pd.DataFrame:
      """Distribution of remote / hybrid / office."""
    if "work_type" not in df.columns:
              return pd.DataFrame()
    breakdown = df["work_type"].value_counts(normalize=True).mul(100).round(1)
    return breakdown.reset_index().rename(columns={"index": "Work Type", "work_type": "Percentage"})


# ── Main Pipeline ─────────────────────────────────────────────

def main():
      df = load_scraped_data()
    df = clean_data(df)

    print("\n--- Top Skills ---")
    skills = extract_skills(df)
    if not skills.empty:
              print(skills.head(15).to_string(index=False))

    print("\n--- Salary by Region ---")
    salaries = salary_summary(df)
    if not salaries.empty:
              print(salaries.to_string(index=False))

    print("\n--- Work Type Breakdown ---")
    work = work_type_breakdown(df)
    if not work.empty:
              print(work.to_string(index=False))

    print("\nDone.")


if __name__ == "__main__":
      main()
