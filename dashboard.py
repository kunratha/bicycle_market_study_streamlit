import streamlit as st
import pandas as pd

# Set the page configuration for title and wide layout
st.set_page_config(page_title="Velo Market", layout="wide")

# from title_section import display_title
from sidebar_section import sidebar_filters
from kpi_section import (
    display_total_countries_kpi,
    display_states_kpi,
    display_Year_kpi,
    display_total_revenue_kpi,
    display_total_units_sold_kpi,
    display_avg_profit_margin_kpi,
)
from chart_section import (
    create_pie_chart_and_extract_data,
    create_line_chart_order_quantity_by_year,
    create_profit_cost_revenue_line_chart,
    create_choropleth_map,
    create_line_chart_by_month_year,
    display_pivot_table_with_expander,
    create_most_profitable_bar_chart,
    plot_revenue_by_state,
)

st.markdown(
    """
        <style>
        div.block-container {
            padding-top: 30px;  /* Adjust this to move the entire content up */
            margin-top: 30px;
        }
        </style>
        <h1 style='text-align: center; font-size: 40px; text-shadow: 2px 2px 5px black; color: white;'>Bicycle Market Study Case <br> KUN RATHA KEAN</h1>
        """,
    unsafe_allow_html=True,
)


# Function to load and cache the data
@st.cache_data
def load_data(file_path):
    """
    This function loads the data from the specified CSV file
    and caches it so it won't be reloaded unless the file changes.
    """
    try:
        # Load the CSV data into a DataFrame
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        st.error(f"Error: The file at {file_path} was not found.")
        return None


# Streamlit Dashboard
def velo_dashboard():

    # Path to the CSV file on your local filesystem
    file_path = "C:/wildcode_school_courses/RCNP_exam_certification/velo_analytics_dashboard/velo_app/data/sales_bicycles.csv"  # Specify the full path to your CSV file here

    # Load the data using the cache
    salebicyles_df = load_data(file_path)

    # Check if data is successfully loaded
    if salebicyles_df is None:
        return

    # Sidebar Filters (displayed even before the file is uploaded)
    filtered_df, selected_countries = sidebar_filters(salebicyles_df)

    # Ensure a single Country is selected for the map (you can modify this depending on how you handle multiple Country selections)
    if len(selected_countries) == 1:
        selected_Country = selected_countries[0]
    else:
        selected_Country = None  # Handle multiple countries or "Select All" scenario

    # Check if the DataFrame has data
    if filtered_df is not None:
        # Display Filtered Velo Data Table
        with st.expander("Expand to view Filtered Velo Data"):
            st.header("Filtered Velo Data")
            st.dataframe(filtered_df)

        # Row 1: Two Columns with Pie Charts and Expanders for the data
        col1, col2, col3 = st.columns([2, 7, 3])

        # Column 1: Pie Chart for Velo Distribution by Country
        with col1:
            bg_option = st.session_state.get("background_option", "Default")

            # Display total countries KPI
            display_total_countries_kpi(salebicyles_df, bg_option=bg_option)

            # Display total states KPI and states for the selected Country if any
            display_states_kpi(salebicyles_df, selected_Country, bg_option=bg_option)

            # Display Year KPI
            display_Year_kpi(filtered_df, selected_Country, bg_option=bg_option)

        # Column 2: Map for Velo Distribution by Region in Selected Country
        with col2:
            custom_title = "Sales Distribution by Country"

            # Get the background option from the session state (or elsewhere)
            bg_option = st.session_state.get("background_option", "Default")

            # Call the create_choropleth_map function with the title and bg_option arguments
            fig_map = create_choropleth_map(
                filtered_df, selected_Country, title=custom_title, bg_option=bg_option
            )

            # Display the map in Streamlit
            st.plotly_chart(fig_map, use_container_width=True)

        # Column 3: Pie Chart for Velo Distribution by Year
        with col3:
            bg_option = st.session_state.get("background_option", "Default")
            pie_chart1, Country_data = create_pie_chart_and_extract_data(
                filtered_df,
                "Country",
                "Velo Sale Distribution by Country",
                bg_option=bg_option,
            )
            st.plotly_chart(pie_chart1, use_container_width=True)

        # Row 2: KPIs Section for revenue, units, profit, customers
        col1, col2, col3 = st.columns(3)

        with col1:
            display_total_revenue_kpi(filtered_df)

        with col2:
            display_total_units_sold_kpi(filtered_df)

        with col3:
            display_avg_profit_margin_kpi(filtered_df)

        # Row 3: line charts
        col1, col2 = st.columns([2, 5])

        with col1:
            bg_option = st.session_state.get("background_option", "Default")
            line_chart, year_data = create_line_chart_order_quantity_by_year(
                filtered_df,
                "Year",
                "Order_Quantity",
                "Order Quantity by Year",
                bg_option=bg_option,
            )
            st.plotly_chart(line_chart, use_container_width=True)

        with col2:
            bg_option = st.session_state.get("background_option", "Default")
            profit_cost_revenue_chart = create_profit_cost_revenue_line_chart(
                filtered_df,
                "Profit, Cost, and Revenue by Year",
                bg_option=bg_option,
            )
            st.plotly_chart(profit_cost_revenue_chart, use_container_width=True)

        # Line chart for Profit, Cost, and Revenue by Month
        line_chart = create_line_chart_by_month_year(
            filtered_df,
            "Month",
            ["Profit", "Cost", "Revenue"],
            "Monthly Sales Trends",
            bg_option=bg_option,
        )
        st.plotly_chart(line_chart, use_container_width=True)

        # Call the pivot table function
        display_pivot_table_with_expander(
            filtered_df,
            index=["Product_Category"],
            columns=["Month"],
            values="Revenue",
            aggfunc="sum",
        )

        # Row 4: Full-width bar chart
        col1, col2 = st.columns([2, 5])
        with col1:
            bg_option = st.session_state.get("background_option", "Default")
            bar_chart, top_products_data = create_most_profitable_bar_chart(
                filtered_df,
                column="Product_Category",
                title="Most Profitable Product Categories",
                orientation="h",
                bg_option=bg_option,
            )
            st.plotly_chart(bar_chart, use_container_width=True)
        with col2:
            bg_option = st.session_state.get("background_option", "Default")
            bar_chart, top_subcategory_data = create_most_profitable_bar_chart(
                filtered_df,
                column="Sub_Category",
                title="Most Profitable Sub Categories",
                orientation="h",
                bg_option=bg_option,
            )
            st.plotly_chart(bar_chart, use_container_width=True)

        # Plot revenue by state for the selected country
        if selected_Country:
            bg_option = st.session_state.get(
                "background_option", "Default"
            )  # Fetch background option
            plot_revenue_by_state(filtered_df, selected_Country, bg_option=bg_option)

        # Row 5: pie chart
        col1, col2 = st.columns(2)
        with col1:
            bg_option = st.session_state.get("background_option", "Default")
            pie_chart, age_group_data = create_pie_chart_and_extract_data(
                filtered_df,
                column_name="Age_Group",
                title="Sales by Age Group",
                bg_option=bg_option,
            )
            st.plotly_chart(pie_chart, use_container_width=True)
        with col2:
            bg_option = st.session_state.get("background_option", "Default")
            pie_chart, age_group_data = create_pie_chart_and_extract_data(
                filtered_df,
                column_name="Customer_Gender",
                title="Sales by Customer Gender",
                bg_option=bg_option,
            )
            st.plotly_chart(pie_chart, use_container_width=True)

    else:
        st.write(
            "Please ensure the CSV file path is correct to see the dashboard content."
        )


if __name__ == "__main__":
    velo_dashboard()
