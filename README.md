# Monthly Sales Analysis Project

##  Project Overview

A comprehensive data analysis project that processes and analyzes monthly sales data for four products over an entire year using Python and data analysis tools. The project aims to extract valuable business insights and visualize data in easily understandable formats.

---

##  Table of Contents

- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Requirements](#requirements)
- [Installation and Setup](#installation-and-setup)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Expected Results](#expected-results)
- [License](#license)

---

##  Key Features

- **Random Data Generation**: Creates realistic sales data for four products
- **Comprehensive Statistical Calculations**: 
  - Monthly total sales
  - Average sales per month
  - Month-over-month growth rate
  - Classification by quarterly periods
- **Advanced Analysis**:
  - Identification of best product, best month, and best quarter
  - Summary tables (Pivot Tables)
- **Multiple Data Visualizations**:
  - Line charts
  - Stacked bar charts
  - Heatmaps
  - Boxplots for distribution analysis

---

##  Technologies Used

| Technology | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.8+ | Primary programming language |
| **NumPy** | 1.21+ | Random number generation |
| **Pandas** | 1.3+ | Data processing and manipulation |
| **Matplotlib** | 3.4+ | Basic data visualization |
| **Seaborn** | 0.11+ | Advanced data visualization |

---

##  Requirements

Before starting, ensure you have:
- **Python 3.8** or higher
- **Anaconda** (recommended but optional)
- **Git** for cloning the repository

---

##  Installation and Setup

### Step 1: Clone the Repository
git clone https://github.com/YourUsername/project_sales_baloul_thileli.git
cd project_sales_baloul_thileli

### Step 2: Create a Virtual Environment (Conda)
conda create --name sales_project_env python=3.11
conda activate sales_project_env

### Step 3: Install Required Libraries
pip install pandas numpy matplotlib seaborn

Or using conda:
conda install pandas numpy matplotlib seaborn


### Step 4: Run the Project
Open Jupyter Notebook:
jupyter notebook

Then open `notebook.ipynb` and run all cells in order.

---

##  Project Structure
project_sales_baloul_thileli/

├── notebook.ipynb # Jupyter notebook with all analysis steps
├── utils.py # Utility functions module (data generation)
├── README.md # This file
└── data/
    ├── initial.csv # Raw data (12 months × 4 products)
    ├── final.csv # Processed data with additional metrics
    ├── output.csv # Summary tables (Pivot Tables)
    ├── output_avg_quarterly.csv # Average sales by quarter
    └── output_total_quarterly.csv # Total sales by quarter


---

##  Usage

### Phase 1: Data Generation
Random sales data is generated for 4 products over 12 months and saved to `data/initial.csv`.

### Phase 2: Data Processing
New metrics are added including:
- `Total_Sales`: Sum of monthly sales
- `Average_Sales`: Average of monthly sales
- `Month_over_Month_Growth`: Monthly growth percentage
- `Quarter`: Classification by quarter period

### Phase 3: Creating Summary Tables
Calculates average and total sales by quarters and products.

### Phase 4: Extracting Key Results
- **Best Month**: Month with highest total sales
- **Best Product**: Product with highest annual sales
- **Best Quarter**: Quarter with highest total sales

### Phase 5: Data Visualizations
- Line chart showing sales trend for each product
- Stacked bar chart of monthly sales
- Heatmap of monthly sales
- Distribution boxplots for each product

### Phase 6: Conclusion Questions
Answers to analytical questions about:
- Product with highest sales contribution
- Best performing quarter and possible reasons
- Recommendations for improving next year's sales strategy

---

##  Expected Results

When running the project successfully, you will get:

1. **CSV Files** containing processed data and summaries
2. **Data Visualizations** showing sales patterns and performance
3. **Insights** to help make informed business decisions

**Example Output:**
Best month: 2025-05-01, Total sales: 285 units
Best product: Product_A, Total sales: 950 units
Best quarter: Q2, Total sales: 850 units

---

##  Usage Examples

### Run a specific part of the code:
import pandas as pd
df = pd.read_csv('data/final.csv')
print(df.head())

### Get quick statistics:

---

##  Contributing

If you want to contribute to improve the project:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Work on your improvements
4. Commit your changes (`git commit -m "Add improvements"`)
5. Push to the branch (`git push origin feature/improvement`)
6. Open a Pull Request

---

##  License

This project is licensed under the MIT License - see the LICENSE file for details.

---

##  Support and Help

If you encounter any issues or have questions:
- Open an Issue in the repository
- Send an email to: [baloulthileli@gmail.com]
- Check the Documentation in the project folder

---

##  Acknowledgments

- Thanks to **Pandas, NumPy, Matplotlib, and Seaborn** for being powerful and user-friendly libraries
- This project was created as part of a data analysis training initiative

---

**Last Updated:** 2025-11-24

