# UK Job Market Analysis Dashboard

**Tools:** Python (pandas, requests, BeautifulSoup) · Plotly.js · GitHub Pages
**Dataset:** Reed / ONS Labour Market Statistics (5,000+ listings)
**Live Dashboard:** [🔗 View Live Interactive Dashboard](https://mayankjoshi518-coder.github.io/uk-job-market-analysis/)

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
