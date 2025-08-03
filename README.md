
# CloudWalk Operational Intelligence — Financial KPIs Analysis Project  

This project consolidates and analyzes transactional financial data to extract valuable business insights, enabling strategic decision-making focused on key performance indicators (KPIs) such as Total Payment Volume (TPV), average ticket size, installment behavior, anticipation methods, and segmentation by product, entity, and payment method.




## 🔑 Scripts and Functionality

Scripts and Functionality
1. join_transactions_checkout.py
- Consolidates transaction and checkout datasets, aligning them by hour (time).
- Standardizes and cleans time-related columns for integrated analysis.
- Produces transactions_checkout_unified.csv for subsequent use.

2. kpi_analysis.py
- Loads and normalizes core operational datasets.
- Joins datasets on strategic keys such as day, entity, product, payment method, price tier, etc.
- Consolidates financial metrics by summing transaction volumes and counts.
- Outputs transactions_consolidated.csv, the foundational dataset for KPI analysis.

3. preprocess_metrics.py
- Enhances the consolidated dataset by creating key derived metrics:
Average ticket size, Transactions per merchant, Average amount per merchant, Average amount per installment, Flags for transactions above average ticket, Temporal indicators (weekday, month-year) for seasonal analysis, Outputs transactions_preprocessed.csv, ready for dashboard visualization.



## 🧪 Workflow execution

Make the code work, run the command below:

```bash
python scripts/join_transactions_checkout.py
python scripts/kpi_analysis.py
python scripts/preprocess_metrics.py
```

After running these scripts, import output/transactions_preprocessed.csv into Power BI to build dashboards, visualizations, and generate insights addressing the business questions.

## ⭐ Extras

Executive Report.pdf -> Report with key insights and ideal for understanding dashboards and key KPIs

CloudWalk_Operational_Intelligence.pbix -> Original editable file developed in Power BI Desktop. It contains connections to data, DAX measures, and interactive dashboards.


## 👋 Contact & Support
For questions, suggestions, or contributions, please contact :

- [Heloísa Zanati - GitHub](https://github.com/Heloisa-Z)
- Email: zanatihelo@gmail.com


