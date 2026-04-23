# Organization-Data-Analysis

## Overview
This project analyzes a dataset of 100 organizations using Python and visualizes insights using Pandas and Matplotlib. It performs data cleaning and creates multiple charts to understand organization age, size, and country distribution.

## Features
The project generates four visualizations:

1. Oldest Organizations
   - Shows the 10 oldest organizations based on founding year
   - Calculates their age

2. Youngest Organizations
   - Shows the 10 most recently founded organizations
   - Calculates their age

3. Top Companies by Employees
   - Displays organizations with the highest number of employees

4. Top Countries by Organization Count
   - Shows countries with the most organizations in the dataset

All charts are displayed in a 2x2 subplot layout.

## Technologies Used
- Python
- Pandas
- Matplotlib

## How to Run

1. Install dependencies:
   pip install pandas
   pip install matplotlib

3. Make sure the dataset file is in the same folder:
   organizations-100.csv

4. Run the script:
   python organizations_analysis.py

## Output
A single window opens displaying four bar charts:
- Oldest organizations
- Youngest organizations
- Top companies by employees
- Top countries by organization count
