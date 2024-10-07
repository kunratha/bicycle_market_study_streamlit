# Bicycle Market Analytics Dashboard

## Overview

This project is a **Bicycle Market Analytics Dashboard** built with **Streamlit** and **Plotly** for visualizing key insights into bicycle sales data. The dashboard allows users to explore various metrics such as total revenue, units sold, and profit margins, and provides dynamic data visualizations through pie charts, line charts, and KPIs (Key Performance Indicators). It also includes filters for customizing the data displayed.

## Features

- **Interactive Data Filtering**: Filter data by country, state, year, product category, and sub-category.
- **KPI Metrics**: Displays total revenue, units sold, profit margin, and more with dynamically styled key performance indicators.
- **Data Visualizations**: Visualize sales data through pie charts, bar charts, and line charts for revenue, order quantities, and profit trends over time.
- **Choropleth Map**: Visualize sales distributions by country or state with color-coded choropleth maps.
- **Pivot Table**: Expandable pivot table for a more detailed breakdown of sales data.
- **Background Themes**: Change the dashboard's appearance with multiple background themes, including Daltonien (colorblind-friendly) mode.

## Technologies

- **Python**
- **Streamlit**
- **Plotly**
- **Pandas**
- **CSS** for custom styling

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kunratha/bicycle_market_study_streamlit.git

2. **Navigate to the project directory**:
   cd bicycle_market_study_streamlit
3. **Create and activate a virtual environment**:
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
4. **Install dependencies**:
   pip install -r requirements.txt
5. **Run the Streamlit app**:
   streamlit run app.py
   
## Usage

    1. The dashboard provides filters on the left sidebar to allow users to select specific countries, states, years, product categories, and subcategories.
    2. KPIs at the top of the page give an overview of the total number of countries, states, revenue, and profit margins.
    3. Visualizations such as line charts, pie charts, and bar charts present trends in sales data by year, month, product category, and more.
    4. Change the background theme of the dashboard with the "Background" selector in the sidebar.

## Project Structure
├── app.py                      # Main Streamlit app
├── sidebar_section.py           # Sidebar filters and background options
├── kpi_section.py               # KPI calculation and display
├── chart_section.py             # Visualization functions (bar, pie, line charts)
├── style_css.py                 # Custom CSS for background themes
├── data/                        # Data directory for sales data
│   └── sales_bicycles.csv       # Sample dataset for analysis
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation

## Dataset
The dataset used in this project contains sales information for bicycles, including:

    Country
    State
    Year
    Product Category
    Revenue
    Profit
    Order Quantity

The CSV file sales_bicycles.csv is located in the data/ folder.

## Future Improvements
    . Add more advanced machine learning models for sales predictions.
    . Implement user authentication for personalized dashboard views.
    . Extend data filtering with more granular metrics like customer demographics.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

