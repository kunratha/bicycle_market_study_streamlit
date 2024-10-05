import streamlit as st
import plotly.express as px
import pandas as pd


# Function to create pie chart and return summarized data used in the chart with dynamic colors
def create_pie_chart_and_extract_data(
    salebicyles_df, column_name, title, bg_option="Default"
):
    # Set colors based on the background option
    if bg_option == "Dark Color":
        text_color = "#FFFFFF"  # White text for dark background
        color_sequence = px.colors.qualitative.Pastel  # Lighter colors for contrast
    elif bg_option == "Light Color":
        text_color = "#000000"  # Black text for light background
        color_sequence = px.colors.qualitative.Bold  # Bold colors for light background
    elif bg_option == "Daltonien":
        text_color = "#000000"  # Set text color to black for Daltonien-friendly
        color_sequence = px.colors.qualitative.Safe  # Colorblind-friendly palette
    else:  # Default
        text_color = (
            "#ffffff"  # Black text for default background (assuming light background)
        )
        color_sequence = px.colors.qualitative.Set1  # Default color palette

    # Create the pie chart
    pie_chart = px.pie(
        salebicyles_df,
        names=column_name,
        title=title,
        color_discrete_sequence=color_sequence,
    )
    pie_chart.update_traces(textposition="inside", textinfo="percent+label")
    pie_chart.update_layout(
        autosize=False,
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False,
        height=400,
        font=dict(color=text_color),  # Dynamic text color
        plot_bgcolor="rgba(0,0,0,0)",  # Transparent background for the chart
        paper_bgcolor="rgba(0,0,0,0)",  # Transparent paper background
        title_font=dict(color=text_color),  # Ensure title color changes dynamically too
    )

    # Extract data: count and percentages for each group in the pie chart
    grouped_data = (
        salebicyles_df.groupby(column_name, observed=False)
        .size()
        .reset_index(name="Count")
    )
    grouped_data["Percentage"] = (
        100 * grouped_data["Count"] / grouped_data["Count"].sum()
    )

    return pie_chart, grouped_data


# Line chart function for order quantity by year
def create_line_chart_order_quantity_by_year(
    salebicyles_df, year_column, order_quantity_column, title, bg_option="Default"
):
    # Set colors based on the background option
    if bg_option == "Dark Color":
        text_color = "#FFFFFF"  # White text for dark background
        color_sequence = px.colors.qualitative.Pastel  # Lighter colors for contrast
    elif bg_option == "Light Color":
        text_color = "#000000"  # Black text for light background
        color_sequence = px.colors.qualitative.Bold  # Bold colors for light background
    elif bg_option == "Daltonien":
        text_color = "#000000"  # Set text color to black for Daltonien-friendly
        color_sequence = px.colors.qualitative.Safe  # Colorblind-friendly palette
    else:  # Default
        text_color = "#FFFFFF"  # Default white text
        color_sequence = px.colors.qualitative.Set1  # Default color palette

    # Grouping the data by year and summing the Order_Quantity for each year
    grouped_data = (
        salebicyles_df.groupby(year_column, observed=False)[order_quantity_column]
        .sum()
        .reset_index()
    )

    # Create a line chart
    line_chart = px.line(
        grouped_data,
        x=year_column,
        y=order_quantity_column,
        title=title,
        color_discrete_sequence=color_sequence,
        labels={year_column: "Year", order_quantity_column: "Total Order Quantity"},
    )

    # Update layout of the line chart
    line_chart.update_traces(mode="lines+markers")
    line_chart.update_layout(
        autosize=False,
        margin=dict(l=20, r=20, t=50, b=20),
        title=dict(
            text=title,
            font=dict(color=text_color, size=20),  # Dynamic title color
        ),
        xaxis=dict(
            title="Year",
            tickfont=dict(color=text_color),  # X-axis tick color
            titlefont=dict(color=text_color),  # X-axis title color
        ),
        yaxis=dict(
            title="Total Order Quantity",
            tickfont=dict(color=text_color),  # Y-axis tick color
            titlefont=dict(color=text_color),  # Y-axis title color
        ),
        height=500,  # Adjust height for better visibility
        font=dict(color=text_color),  # Dynamic text color for the rest
        plot_bgcolor="rgba(0,0,0,0)",  # Transparent background
        paper_bgcolor="rgba(0,0,0,0)",  # Transparent paper background
    )

    return line_chart, grouped_data


# Function to create line chart for Profit, Cost, Revenue over years with dynamic background colors
def create_profit_cost_revenue_line_chart(sales_df, title, bg_option="Default"):
    # Set dynamic background colors based on selected bg_option
    if bg_option == "Dark Color":
        plot_bg_color = "rgba(0, 0, 0, 0)"  # Dark plot background
        paper_bg_color = "rgba(0, 0, 0, 0)"  # Dark paper background
        text_color = "#FFFFFF"  # White text color
        grid_color = "rgba(255, 255, 255, 0.1)"  # Light grid for dark background
    elif bg_option == "Light Color":
        plot_bg_color = "rgba(240, 240, 240, 0.9)"  # Light gray plot background
        paper_bg_color = "rgba(240, 240, 240, 0.9)"  # Light gray paper background
        text_color = "#333333"  # Dark text color
        grid_color = "rgba(0, 0, 0, 0.1)"  # Dark grid lines for light background
    elif bg_option == "Daltonien":
        plot_bg_color = "rgba(200, 200, 200, 0.9)"  # Neutral plot background
        paper_bg_color = "rgba(200, 200, 200, 0.9)"  # Neutral paper background
        text_color = "#555555"  # Neutral text color
        grid_color = "rgba(0, 0, 0, 0.1)"  # Dark grid lines for neutral background
    else:
        # Default background option
        plot_bg_color = "rgba(0, 0, 0, 0)"  # Default black background
        paper_bg_color = "rgba(0, 0, 0, 0)"  # Default white paper background
        text_color = "#FFFFFF"  # Default white text color
        grid_color = "rgba(255, 255, 255, 0.2)"  # Default light grid lines

    # Group data by Year and aggregate Profit, Cost, Revenue
    grouped_data = (
        sales_df.groupby("Year", observed=False)
        .agg({"Profit": "sum", "Cost": "sum", "Revenue": "sum"})
        .reset_index()
    )

    # Create the line chart for Profit, Cost, and Revenue
    line_chart = px.line(
        grouped_data, x="Year", y=["Profit", "Cost", "Revenue"], title=title
    )

    # Update the layout of the line chart with dynamic colors from the condition
    line_chart.update_layout(
        autosize=True,
        margin=dict(l=20, r=20, t=50, b=20),
        height=500,  # Adjust height for better visibility
        font=dict(color=text_color),  # Dynamic text color
        plot_bgcolor="rgba(0, 0, 0, 0)",  # Dynamic plot background color
        paper_bgcolor="rgba(0, 0, 0, 0)",  # Dynamic paper background color
        xaxis=dict(
            showgrid=True,
            gridcolor=grid_color,  # X-axis grid color
            title=dict(text="Year", font=dict(color=text_color)),  # X-axis title color
            tickfont=dict(color=text_color),  # X-axis tick color
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor=grid_color,  # Y-axis grid color
            title=dict(
                text="Values", font=dict(color=text_color)  # Y-axis title color
            ),
            tickfont=dict(color=text_color),  # Y-axis tick color
        ),
        legend=dict(
            title=dict(
                text="Metrics", font=dict(color=text_color)  # Legend title color
            ),
            font=dict(color=text_color),  # Legend text color
        ),
        title=dict(
            text=title, font=dict(color=text_color, size=20)  # Title color and size
        ),
    )

    return line_chart


# Line chart for the sale evolution over the year with correct month ordering and dynamic colors
def create_line_chart_by_month_year(
    sales_df, x_column, y_columns, title, bg_option="Default"
):
    # Set colors and background based on the background option
    if bg_option == "Dark Color":
        text_color = "#FFFFFF"  # White text for dark background
        color_sequence = px.colors.qualitative.Pastel  # Lighter colors for contrast
        background_color = "rgba(34, 34, 34, 1)"  # Dark background
        grid_color = "rgba(255, 255, 255, 0.3)"  # Light grid for dark background
    elif bg_option == "Light Color":
        text_color = "black"  # Black text for light background
        color_sequence = px.colors.qualitative.Bold  # Bold colors for light background
        background_color = "rgba(240, 240, 240, 1)"  # Light background
        grid_color = "rgba(0, 0, 0, 0.3)"  # Dark grid for light background
    elif bg_option == "Daltonien":
        text_color = "black"  # Black text for Daltonien-friendly mode
        color_sequence = px.colors.qualitative.Safe  # Colorblind-friendly palette
        background_color = "rgba(255, 228, 196, 1)"  # Colorblind-friendly background
        grid_color = "rgba(0, 0, 0, 0.3)"  # Dark grid for Daltonien-friendly mode
    else:  # Default
        text_color = "#FFFFFF"  # White text for default mode
        color_sequence = px.colors.qualitative.Set1  # Default color palette
        grid_color = "rgba(255, 255, 255, 0.3)"  # Light grid for default mode

    # Ensure the x_column (Month) is in the correct order (January to December)
    month_order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    # Convert the x_column (Month) to a categorical type with the correct order
    sales_df[x_column] = pd.Categorical(
        sales_df[x_column], categories=month_order, ordered=True
    )

    # Group the data by Month and aggregate values for Profit, Cost, and Revenue
    monthly_sales_df = (
        sales_df.groupby(x_column, observed=False)[y_columns].sum().reset_index()
    )

    # Create the line chart
    line_chart = px.line(
        monthly_sales_df,
        x=x_column,
        y=y_columns,
        title=title,
        color_discrete_sequence=color_sequence,
    )

    # Update layout of the line chart
    line_chart.update_layout(
        autosize=False,
        margin=dict(l=20, r=20, t=50, b=20),
        height=500,  # Adjust height for better visibility
        font=dict(color=text_color),  # Dynamic text color
        plot_bgcolor="rgba(0, 0, 0, 0)",  # Transparent plot background
        paper_bgcolor="rgba(0, 0, 0, 0)",  # Transparent paper background
        xaxis=dict(
            categoryorder="array",
            categoryarray=month_order,  # Ensure correct month order
            title=dict(text="Month", font=dict(color=text_color)),  # X-axis title color
            tickfont=dict(color=text_color),  # X-axis tick color
            # showgrid=True,
            # gridcolor=grid_color,  # X-axis grid color
            # gridwidth=1,  # Grid line width
        ),
        yaxis=dict(
            title=dict(
                text="Values", font=dict(color=text_color)  # Y-axis title color
            ),
            tickfont=dict(color=text_color),  # Y-axis tick color
            showgrid=True,  # Display grid lines
            gridcolor=grid_color,  # Y-axis grid color with opacity
            gridwidth=1,  # Set grid line width
        ),
        legend=dict(
            title=dict(
                text="Metrics", font=dict(color=text_color)  # Legend title color
            ),
            font=dict(color=text_color),  # Legend text color
        ),
        title=dict(
            text=title, font=dict(color=text_color, size=20)  # Title color and size
        ),
    )

    return line_chart


def display_pivot_table_with_expander(sales_df, index, columns, values, aggfunc="sum"):
    # Create the pivot table
    pivot_df = pd.pivot_table(
        sales_df,
        index=index,
        columns=columns,
        values=values,
        aggfunc=aggfunc,
        fill_value=0,
        observed=False,
    )

    # Custom CSS for table styling
    table_style = """
    <style>
    .custom-table {
        border-collapse: collapse;
        width: 100%;
    }
    .custom-table th, .custom-table td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: center;
    }
    .custom-table th {
        background-color: rgba(34, 34, 34, 0.9); /* Adjust for dark theme */
        color: white;
    }
    .custom-table td {
        background-color: rgba(240, 240, 240, 0.9); /* Adjust for light theme */
        color: black;
    }
    </style>
    """

    # Use an expander to hide the pivot table until the user clicks to view it
    with st.expander("Expand to View Pivot Table"):
        st.markdown("### Pivot Table")
        # Inject CSS
        st.markdown(table_style, unsafe_allow_html=True)
        # Convert the pivot table to HTML and display it
        st.markdown(pivot_df.to_html(classes="custom-table"), unsafe_allow_html=True)


# Bar plot for revenue by state or region of a selected country
def plot_revenue_by_state(sales_df, selected_country, bg_option="Default"):
    if selected_country:
        # Filter the data for the selected country
        filtered_df = sales_df[sales_df["Country"] == selected_country]

        # Group by State and calculate total revenue
        revenue_by_state = (
            filtered_df.groupby("State", observed=False)["Revenue"].sum().reset_index()
        )

        # Sort by revenue in descending order
        revenue_by_state = revenue_by_state.sort_values(by="Revenue", ascending=False)

        # Set colors and background based on the background option
        if bg_option == "Dark Color":
            text_color = "#FFFFFF"  # White text for dark background
            # grid_color = "rgba(255, 255, 255, 0.2)"  # White grid lines with 20% opacity
            background_color = "rgba(34, 34, 34, 1)"  # Dark background
        elif bg_option == "Light Color":
            text_color = "#000000"  # Black text for light background
            # grid_color = "rgba(0, 0, 0, 0.1)"  # Black grid lines with 10% opacity
            background_color = "rgba(240, 240, 240, 1)"  # Light background
        elif bg_option == "Daltonien":
            text_color = "#000000"  # Black text for Daltonien-friendly mode
            # grid_color = "rgba(0, 0, 0, 0.1)"  # Black grid lines with 10% opacity
            background_color = (
                "rgba(255, 228, 196, 1)"  # Colorblind-friendly background
            )
        else:  # Default
            text_color = "#FFFFFF"  # Default white text
            # grid_color = "rgba(0, 0, 0, 0.1)"  # Default grid color
            background_color = "rgba(255, 255, 255, 1)"  # Default white background

        # Plot the bar chart
        fig = px.bar(
            revenue_by_state,
            x="State",
            y="Revenue",
            title=f"Revenue by State in {selected_country}",
            labels={"Revenue": "Total Revenue", "State": "State"},
            text="Revenue",
        )

        # Update layout with custom grid color and opacity
        fig.update_layout(
            autosize=True,
            margin=dict(l=20, r=20, t=50, b=20),
            height=500,
            font=dict(color=text_color),  # Dynamic text color
            plot_bgcolor="rgba(0, 0, 0, 0)",  # Transparent plot background
            paper_bgcolor="rgba(0, 0, 0, 0)",  # Transparent paper background
            xaxis=dict(
                # showgrid=True,  # Enable grid lines
                # gridcolor=grid_color,  # Set grid color with opacity
                # gridwidth=1,  # Set grid width
                tickfont=dict(color=text_color),  # X-axis text color
            ),
            yaxis=dict(
                # showgrid=True,  # Enable grid lines
                # gridcolor=grid_color,  # Set grid color with opacity
                # gridwidth=1,  # Set grid width
                tickfont=dict(color=text_color),  # Y-axis text color
            ),
            title=dict(
                text=f"Revenue by State in {selected_country}",
                font=dict(color=text_color),  # Title color
            ),
        )

        # Display the chart in Streamlit
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("Please select a country to see the revenue by state.")


# Function to create a bar chart for most profitable items based on a selected column
def create_most_profitable_bar_chart(
    salebicyles_df,
    column,
    title="Most Profitable Items",
    bg_option="Background Image",
    orientation="v",
):
    # Set colors based on the background option
    if bg_option == "Dark Color":
        text_color = "#ffffff"  # White text for dark background
        color_sequence = px.colors.qualitative.Pastel  # Lighter colors for contrast
        grid_color = "rgba(255, 255, 255, 0.2)"  # White grid with 20% opacity
        axis_color = "#ffffff"  # White axis color for dark background
    elif bg_option == "Light Color":
        text_color = "#000000"  # Black text for light background
        color_sequence = px.colors.qualitative.Bold  # Bold colors for light background
        grid_color = "rgba(0, 0, 0, 0.1)"  # Black grid with 10% opacity
        axis_color = "#000000"  # Black axis color for light background
    elif bg_option == "Daltonien":
        text_color = "#000000"  # Set text color to black for Daltonien-friendly
        color_sequence = px.colors.qualitative.Safe  # Colorblind-friendly palette
        grid_color = "rgba(0, 0, 0, 0.1)"  # Black grid with 10% opacity
        axis_color = "#000000"  # Black axis color for Daltonien mode
    else:  # Default
        text_color = "#ffffff"  # Neutral white text
        color_sequence = px.colors.qualitative.Set1  # Default color palette
        grid_color = "rgba(0, 0, 0, 0.1)"  # Default black grid lines
        axis_color = "#ffffff"  # Default axis color for dark background

    # Group the data by the selected column and aggregate by sum of Profit
    grouped_data = (
        salebicyles_df.groupby(column, observed=False)["Profit"].sum().reset_index()
    )

    # Select the top 20 entries by profit
    top_20_data = grouped_data.nlargest(20, "Profit")

    # Create the bar chart using the top 20 entries
    bar_chart = px.bar(
        top_20_data,
        x=column if orientation == "v" else "Profit",
        y="Profit" if orientation == "v" else column,
        orientation=orientation,  # Set orientation dynamically
        title=title,
        color_discrete_sequence=color_sequence,
        labels={column: "Category", "Profit": "Total Profit"},
    )

    # Add percentage to the grouped data
    total_profit = grouped_data["Profit"].sum()
    top_20_data["Percentage"] = 100 * top_20_data["Profit"] / total_profit

    # Update layout of the bar chart with grid color, axis colors, and opacity
    bar_chart.update_traces(texttemplate="%{x}", textposition="outside")
    bar_chart.update_layout(
        autosize=False,
        margin=dict(l=20, r=20, t=50, b=20),
        height=500,  # Adjust height for better visibility
        font=dict(color=text_color),  # Dynamic text color
        plot_bgcolor="rgba(0,0,0,0)",  # Transparent background
        paper_bgcolor="rgba(0,0,0,0)",  # Transparent paper background
        xaxis=dict(
            # showgrid=True,  # Show grid
            # gridcolor=grid_color,  # Dynamic grid color
            # gridwidth=1,  # Grid width
            tickfont=dict(color=axis_color),  # X-axis tick color
            title=dict(
                text="Category", font=dict(color=axis_color)
            ),  # X-axis title color
        ),
        yaxis=dict(
            # showgrid=True,  # Show grid
            # gridcolor=grid_color,  # Dynamic grid color
            # gridwidth=1,  # Grid width
            tickfont=dict(color=axis_color),  # Y-axis tick color
            title=dict(
                text="Profit", font=dict(color=axis_color)
            ),  # Y-axis title color
            categoryorder="total ascending",  # Ensure the largest category is at the top
        ),
        title=dict(text=title, font=dict(color=text_color)),  # Title color
    )

    return bar_chart, top_20_data


# Function to create a choropleth map based on Country statistics with dynamic colors
def create_choropleth_map(
    salebicyles_df, selected_country=None, title="Map Title", bg_option="Default"
):
    # Set colors based on the background option
    if bg_option == "Dark Color":
        color_sequence = (
            px.colors.sequential.Plasma_r
        )  # Reversed Plasma for better contrast on dark
        text_color = "#ffffff"  # White text for dark background
    elif bg_option == "Light Color":
        color_sequence = px.colors.sequential.Viridis  # Vibrant for light background
        text_color = "#000000"  # Black text for light background
    elif bg_option == "Daltonien":
        color_sequence = (
            px.colors.sequential.Viridis
        )  # Use Viridis for colorblind-friendly palette
        text_color = "#000000"  # Set text color to black for Daltonien-friendly
    else:  # Default
        color_sequence = px.colors.sequential.Plasma  # Default sequential palette
        text_color = "#ffffff"  # Default white text

    # Grouping the data by Country and calculating required statistics
    if selected_country:
        # Filter the data to only the selected Country
        salebicyles_df = salebicyles_df[salebicyles_df["Country"] == selected_country]

    country_stats = (
        salebicyles_df.groupby("Country", observed=False)
        .agg(count=("Country", "size"))
        .reset_index()
    )

    # Creating the choropleth map with a predefined aspect ratio and height
    fig_map = px.choropleth(
        country_stats,
        locations="Country",
        locationmode="country names",  # Correct case for locationmode
        color="count",
        hover_name="Country",
        color_continuous_scale=color_sequence,
        title=title,  # Dynamic title
        height=400,  # Set a fixed height for the map
    )

    # Adjust latitude and longitude range for global display
    lat_range = [-60, 90]  # Latitude range to cover the globe
    lon_range = [-180, 180]  # Longitude range

    if selected_country:
        # Optionally, adjust lat/lon ranges if specific countries or states need a zoomed-in view
        if selected_country == "France":
            lat_range = [31, 61]  # Example: France's latitude range
            lon_range = [-5, 15]  # Example: France's longitude range

    # Update layout of the map and color bar
    fig_map.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type="equirectangular",
            lataxis_range=lat_range,
            lonaxis_range=lon_range,
        ),
        coloraxis_colorbar=dict(
            title="Number of Sales",
            thicknessmode="pixels",
            thickness=15,
            lenmode="fraction",
            len=0.7,
            xpad=40,
        ),
        font=dict(size=18, color=text_color),  # Dynamic text color for titles/labels
        title=dict(
            text=title,  # Dynamic title
            font=dict(color=text_color),  # Dynamic title color
        ),
        margin=dict(l=10, r=10, t=50, b=10),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )

    return fig_map
