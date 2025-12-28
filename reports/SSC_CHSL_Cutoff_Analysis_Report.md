# A Five-Year Post-wise and Category-wise Analysis of SSC CHSL Cut-Offs (2019–2023)

**Author:** Shashwat Samarth  
**Project Type:** Data Analysis Case Study  
**Tools Used:** Excel, MySQL (Schema), Python, GitHub  
**Status:** In Progress  

---

## Abstract

The Staff Selection Commission Combined Higher Secondary Level (SSC CHSL) examination is one of the largest competitive recruitment examinations in India, with cut-off marks varying significantly across posts and categories. This study presents a five-year longitudinal analysis of SSC CHSL Tier-I cut-off trends from 2019 to 2023, focusing on post-wise and category-wise variations and their relationship with competition density. Official cut-off data was collected from SSC result write-up documents, while candidate participation figures were estimated using secondary sources due to the absence of officially published category-wise appearance data. The dataset was cleaned using spreadsheet tools, structured using a relational database schema, and analyzed using Python. The findings indicate that competition density and post preference are the dominant structural factors influencing cut-off variations, while year-to-year exam difficulty plays a comparatively limited role.

---

## 1. Introduction

The SSC CHSL examination serves as a key recruitment channel for clerical and data entry positions in various government departments, including posts such as Lower Division Clerk/Junior Secretariat Assistant (LDC/JSA), Postal Assistant/Sorting Assistant (PA/SA), and Data Entry Operator (DEO). Each year, the examination attracts a large and diverse pool of candidates, resulting in intense competition and closely observed cut-off trends.

Unlike examinations that declare a single qualifying threshold, SSC CHSL cut-offs differ across posts and reservation categories, reflecting variations in vacancy distribution, candidate preference, and competition intensity. Despite frequent discussion among aspirants, systematic and data-driven analysis of these cut-off variations remains limited.

This study aims to address this gap by conducting a structured, longitudinal analysis of SSC CHSL Tier-I cut-off data over a five-year period. By integrating post-wise and category-wise perspectives with estimated competition density, the study seeks to identify the structural factors that consistently influence cut-off behavior and to demonstrate a reproducible, database-driven approach to examination data analysis.

---

## 2. Objectives of the Study

The primary objectives of this study are as follows:

1. To analyze SSC CHSL Tier-I cut-off trends over a five-year period (2019–2023).
2. To compare cut-off variations across different posts, namely LDC/JSA, PA/SA, and DEO.
3. To examine category-wise differences in cut-off marks across reservation categories.
4. To study the relationship between competition density and cut-off levels.
5. To demonstrate a structured, database-driven approach to analyzing competitive examination data.

---

## 3. Scope of the Study

This study is limited to the SSC CHSL Tier-I examination conducted between 2019 and 2023. The analysis covers three major posts—LDC/JSA, PA/SA, and DEO—and five reservation categories: UR, OBC, SC, ST, and EWS.

The study focuses on identifying relative trends and structural patterns in cut-off behavior rather than evaluating policy effectiveness or reservation outcomes. Factors such as shift-wise normalization, regional variation, and individual candidate performance are outside the scope of this analysis.

---

## 4. Data Sources and Collection

The data used in this study was collected from both primary and secondary sources to ensure accuracy, completeness, and transparency.

### 4.1 Primary Data Sources

Official cut-off marks for SSC CHSL Tier-I examinations were obtained from result and write-up documents published on the official website of the Staff Selection Commission (SSC). These documents provide post-wise and category-wise cut-off details and were treated as the authoritative source for cut-off data across all five years of analysis (2019–2023).

### 4.2 Secondary Data Sources

Secondary sources, including reputed examination preparation portals and publicly available reports, were used to cross-verify cut-off values and to obtain contextual information regarding candidate participation. These sources were used only for data structuring and validation purposes and not as primary authorities.

### 4.3 Candidate Participation Data

The SSC does not officially publish category-wise candidate appearance data. Therefore, candidate participation figures used in this study were estimated using a combination of total applicant statistics, reservation proportions, and publicly available exam analytics. All such figures are explicitly treated as estimates and are used solely to analyze relative competition density rather than absolute participation counts.

---

## 5. Data Preparation and Storage

After collection, the raw data was organized and cleaned using spreadsheet software to ensure consistency, accuracy, and compatibility with further analysis. Column names were standardized, categorical values were normalized, and incomplete or inconsistent entries were removed. The cleaned dataset was first preserved as a raw Excel file to maintain an immutable source of truth.

For analytical readiness, a separate analysis-oriented dataset was created and exported in CSV format. This CSV file served as the primary input for both database design and Python-based analysis.

To enable structured storage and reproducibility, a relational database schema was designed using MySQL. The schema captures examination year, post, category, cut-off marks, and estimated candidate participation in a normalized tabular format. Although the database was not executed as part of this study, the schema and import logic were documented and version-controlled to demonstrate a production-ready data pipeline.

---

## 6. Methodology

The study follows a structured, multi-stage methodology designed to ensure transparency and reproducibility. First, official SSC documents were reviewed to extract post-wise and category-wise cut-off data for each year. The extracted data was manually validated and cleaned using spreadsheet tools.

Next, the cleaned data was structured into a relational format consistent with SQL database design principles. This structure enabled efficient grouping, aggregation, and trend analysis across multiple dimensions such as year, post, and category.

Finally, the dataset was analyzed using Python, leveraging data analysis and visualization libraries to compute summary statistics and generate trend-based insights. All scripts, schemas, and datasets were maintained under version control using GitHub to ensure traceability and incremental development.

---

## 7. Data Analysis and Results

The analysis reveals distinct and consistent patterns across posts and categories over the five-year period.

Post-wise analysis shows that the Data Entry Operator (DEO) post consistently records the highest cut-off marks. This trend can be attributed to a combination of lower vacancy counts, higher skill requirements, and stronger candidate preference. The Postal Assistant/Sorting Assistant (PA/SA) post exhibits moderate cut-off levels, while the Lower Division Clerk/Junior Secretariat Assistant (LDC/JSA) post shows comparatively lower cut-offs due to higher vacancy availability despite larger candidate participation.

Category-wise analysis indicates that unreserved and OBC categories generally record higher cut-offs across all posts, reflecting higher competition density. Reserved categories such as SC and ST consistently show lower cut-off thresholds, aligning with comparatively lower participation levels.

A combined analysis of candidate participation and cut-off marks demonstrates a positive relationship between competition density and cut-off levels, suggesting that relative crowd size plays a significant role in determining qualifying thresholds.

---

## 8. Findings and Discussion

The findings of this study highlight that SSC CHSL cut-off variations are largely structural rather than random. Post preference and vacancy distribution emerge as dominant determinants of cut-off levels. Posts with fewer vacancies and higher demand consistently maintain higher cut-offs across years.

Similarly, category-wise cut-off differences align closely with estimated competition density rather than year-specific exam difficulty. While minor year-to-year fluctuations are observed, the overall hierarchy of cut-offs remains stable across the five-year timeline.

These findings support the view that cut-off behavior in large-scale competitive examinations is primarily influenced by participation dynamics and structural constraints rather than short-term examination factors alone.

---

## 9. Limitations

This study is subject to certain limitations. Category-wise candidate participation data is not officially published by the SSC and therefore had to be estimated using secondary sources and proportional assumptions. While care was taken to ensure reasonable estimates, absolute accuracy cannot be guaranteed.

Additionally, the study does not account for shift-wise normalization, regional variation, or changes in examination pattern beyond Tier-I. These factors may influence individual-year cut-offs but are beyond the defined scope of this analysis.

---

## 10. Conclusion

This five-year post-wise and category-wise analysis of SSC CHSL Tier-I cut-offs demonstrates that competition density and post preference are the most influential factors governing cut-off variation. Despite changes in exam conditions across years, structural patterns remain consistent, reinforcing the role of participation dynamics and vacancy distribution in shaping cut-off outcomes.

The study also illustrates the effectiveness of a structured, database-driven approach to analyzing competitive examination data. The methodology and analytical framework presented here can be extended to other examinations and datasets to support evidence-based understanding of recruitment trends.

---

## References

1. Staff Selection Commission. Official SSC CHSL Result and Write-Up Documents (2019–2023). https://ssc.gov.in  
2. CareerPower. SSC CHSL Cut-Off Analysis and Exam Trends.  
3. Testbook. SSC CHSL Examination Data and Insights.  
4. Public news reports and exam analytics related to SSC CHSL participation.

