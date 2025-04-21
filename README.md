Summary of Changes
Original Rows: 2,240
Cleaned Rows: 2,216 (24 rows dropped due to missing Income)
Columns: 29
Key Fixes:
Missing Data: Removed 24 rows with null Income.
Duplicates: None found.
Standardization:
Education and Marital_Status values were cleaned and normalized.
Rare labels like "YOLO" or "Absurd" were grouped under "Single".
Date Format:
Converted Dt_Customer to proper datetime format.
Column Names:
Cleaned and converted to snake_case.
Data Types:
Ensured income is float, year_birth is int.
