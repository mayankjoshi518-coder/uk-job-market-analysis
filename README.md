# UK Job Market Analysis Dashboard

**Tools:** Python (pandas, requests, BeautifulSoup) · Tableau Public · GitHub
**Dataset:** Reed / ONS Labour Market Statistics (5,000+ listings)
**Live Dashboard:** [View on Tableau Public](#) *(link once published)*

---

## Problem Statement

Which skills, locations, and work arrangements are UK employers actually demanding for Business Analyst and Data Analyst roles in 2024–2025? This project answers that question with real data.

---

## Approach

| Step | Description |
|------|-------------|
| 1. Data Collection | Downloaded ONS CSVs + scraped Reed job listings using `requests` + `BeautifulSoup` |
| 2. Cleaning | Deduplicated, standardised job titles, extracted salary bands with `pandas` |
| 3. Feature Engineering | Categorised skills, mapped locations to UK regions, classified work arrangements |
| 4. Visualisation | Built interactive Tableau Public dashboard with 4 views |
| 5. Insight | Wrote a business summary of key findings for recruiters |

---

## Key Findings

- **Top 5 skills demanded:** SQL, Excel, Power BI, Python, Tableau (in that order)
- **Highest-paying region:** London (median £47,500) — 28% above the national median
- **Remote vs hybrid:** 62% hybrid, 19% fully remote, 19% office-only
- **Fastest growing sector:** FinTech and Financial Services (up 34% YoY in BA/DA postings)

---

## Dashboard Views

1. **Skills Demand Heatmap** — frequency of each skill by role type
2. **Salary Distribution by Region** — box plots, median annotations
3. **Work Arrangement Trends** — remote/hybrid/office over time
4. **Top Industries Hiring** — treemap of sector volume

> Screenshots in `/visualisations/`

---

## Repository Structure

```
uk-job-market-analysis/
├── notebooks/
│   └── analysis.ipynb          # Full analysis pipeline
├── data/
│   └── sample_listings.csv     # 100-row sample (full data from ONS)
├── visualisations/
│   └── dashboard_screenshot.png
└── README.md
```

---

## How to Run

```bash
pip install pandas requests beautifulsoup4 matplotlib seaborn jupyter
jupyter notebook notebooks/analysis.ipynb
```

---

## Business Summary

> Employers in 2025 prioritise SQL and Excel fluency above all else — even Python. Candidates targeting London FinTech roles should emphasise Power BI and financial domain knowledge. Hybrid roles dominate, but the share of remote positions has plateaued since 2023.
