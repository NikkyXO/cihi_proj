# Ontario Emergency Department Performance — CIHI NACRS

Question: How long do patients spend in the ED in Ontario compared with the rest of Canada, and what is driving visits?

## Data source
- CIHI, NACRS Emergency Department Visits and Lengths of Stay
- Main file used: `data/raw/nacrs-ed-2025-2026.xlsx`
  - April 1, 2025 to March 31, 2026, final data, September 2026 release
  - Total: 15,628,870 unscheduled ED visits in participating provinces/territories
  - Down from more than 16.1 million in 2024-2025
  - Comparison file kept: `data/raw/nacrs-ed-2024-2025.xlsx`
- Page: https://www.cihi.ca/en/nacrs-emergency-department-visits-and-lengths-of-stay
- Coverage note: complete coverage (>95%) in Quebec, Ontario, Saskatchewan, Alberta and Yukon; 72% in P.E.I., 75% in Manitoba and B.C.; 87% in Canada overall. Not all facilities in P.E.I., Manitoba, Saskatchewan and B.C. are in NACRS.

## Files
- Table 1: ED visits and length of stay by province/territory and CTAS group. 25 rows, 11 columns.
- Table 2: ED visits by month, age and sex. 372 rows, 8 columns.
- Table 3: Top 10 main problems, visits, 90th percentile length of stay, admitted share. 19 rows, 5 columns.

## Ontario, 2025-2026, Table 1
- Total visits: 6,606,941
- CTAS I-III discharged: 3,925,489, median 3.7 hours, 90th percentile 8.2 hours
- CTAS IV-V discharged: 1,266,822, median 2.3 hours, 90th percentile 5.7 hours
- Admitted: 769,932, median 13.5 hours, 90th percentile 38.3 hours
- Canada total, admitted: median 15.5 hours, 90th percentile 46.5 hours

## Plan
1. Clean and prepare with Python (pandas)
2. Analyze with Python (Ontario vs Canada, admitted vs discharged, monthly and age patterns, top diagnoses)
3. Report with Python (charts + one-page findings memo)

## How to run
```bash
python3 scripts/01_clean.py
```
Outputs cleaned CSVs to `data/clean/`.
