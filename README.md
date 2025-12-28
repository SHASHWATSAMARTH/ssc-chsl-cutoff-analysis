# SSC CHSL Cut-Off Analysis (2019–2023)

A data-driven case study analyzing post-wise and category-wise SSC CHSL Tier-I cut-off trends over five years (2019–2023).  
The project examines how competition density and post preference influence cut-off behavior using structured data, SQL schema design, and Python-based analysis.

---

## 📌 Project Overview

- **Exam:** SSC CHSL (Tier-I)
- **Years Covered:** 2019–2023
- **Posts Analyzed:** LDC/JSA, PA/SA, DEO
- **Categories:** UR, OBC, SC, ST, EWS
- **Focus:** Cut-off trends vs competition density

---

## 🛠️ Tools & Technologies

- **Excel** – Data collection and cleaning  
- **MySQL (Schema & SQL scripts)** – Structured data design  
- **Python (pandas, matplotlib)** – Analysis and visualization  
- **GitHub** – Version control and documentation  

---

## 📂 Repository Structure

ssc-chsl-cutoff-analysis/
│
├── data/
│ ├── ssc_chsl_analysis_data.xlsx # Cleaned, analysis-ready data
│ └── ssc_chsl_analysis_data.csv # CSV used for analysis
│
├── database/
│ ├── schema.sql # MySQL database schema
│ └── import_data.sql # SQL script for CSV import
│
├── scripts/
│ ├── analysis.py # Summary analysis script
│ └── visualize.py # Visualization script
│
├── report/
│ └── SSC_CHSL_Cutoff_Analysis_Report.md
│
└── README.md
