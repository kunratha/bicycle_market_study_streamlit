import streamlit as st


# Function to calculate and display the total number of countries with dynamic background
def display_total_countries_kpi(salebicyles_df, bg_option="Default"):
    total_countries = salebicyles_df["Country"].nunique()

    # Define background and text colors based on the selected background option
    if bg_option == "Background Image":
        kpi_bg_color = "rgba(34, 34, 34, 0.8)"
        kpi_value_color = "blue"
        kpi_label_color = "#ffffff"  # White text for label
    elif bg_option == "Dark Color":
        kpi_bg_color = "rgba(42, 52, 57, 0.85)"
        kpi_value_color = "blue"  # White text for dark background
        kpi_label_color = "#ffffff"  # White text for label
    elif bg_option == "Light Color":
        kpi_bg_color = "rgba(200, 200, 200, 0.9)"
        kpi_value_color = "#007bff"  # Blue text for light background
        kpi_label_color = "#333333"  # Darker text color for label
    elif bg_option == "Daltonien":
        kpi_bg_color = "rgba(200, 200, 200, 0.9)"
        kpi_value_color = "#ff7f0e"  # Orange text for Daltonien visibility
        kpi_label_color = "#555555"  # Grey text for label in Daltonien mode
    else:
        # Default background and text colors
        kpi_bg_color = "rgba(0, 123, 255, 0.2)"  # Blueish background
        kpi_value_color = "#007bff"  # Default blue for value
        kpi_label_color = "#333333"  # Default dark text for label

    kpi_style = f"""
    <style>
    div[data-testid="stMarkdownContainer"] > div {{
        background-color: {kpi_bg_color};
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 5px;
        color: {kpi_label_color};  /* Label color */
    }}
    div[data-testid="stMarkdownContainer"] > div .kpi-value {{
        font-size: 25px;
        color: {kpi_value_color};  /* Value color */
    }}
    </style>
    """

    # Insert KPI with background
    st.markdown(kpi_style, unsafe_allow_html=True)
    st.markdown(
        f"""
    <div class="kpi-box">
        <div>Total Countries</div>
        <div class="kpi-value">{total_countries}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def display_states_kpi(salebicyles_df, selected_Country=None, bg_option="Default"):
    if selected_Country:
        total_states = salebicyles_df[salebicyles_df["Country"] == selected_Country][
            "State"
        ].nunique()
        kpi_label = f"Total states in {selected_Country}"
    else:
        total_states = salebicyles_df["State"].nunique()
        kpi_label = "Total states"

    # Define background and text colors based on the selected background option
    if bg_option == "Background Image":
        kpi_bg_color = "rgba(34, 34, 34, 0.8)"
        kpi_value_color = "blue"
        kpi_label_color = "#ffffff"  # Light grey text
    if bg_option == "Dark Color":
        kpi_bg_color = "rgba(34, 34, 34, 0.8)"
        kpi_value_color = "blue"  # White text for dark background
        kpi_label_color = "#ffffff"  # Light grey text
    elif bg_option == "Light Color":
        kpi_bg_color = "rgba(240, 240, 240, 0.9)"
        kpi_value_color = "#007bff"  # Blue text for light background
        kpi_label_color = "#333333"  # Darker text color
    elif bg_option == "Daltonien":
        kpi_bg_color = "rgba(200, 200, 200, 0.9)"
        kpi_value_color = "#ff7f0e"  # Orange text for neutral visibility
        kpi_label_color = "#555555"  # Neutral grey text
    else:
        # Default background and text colors
        kpi_bg_color = "rgba(0, 128, 128, 0.2)"
        kpi_value_color = "#007bff"
        kpi_label_color = "#333333"

    kpi_style = f"""
    <style>
    .kpi-box {{
        background-color: {kpi_bg_color};
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 5px;
        color: {kpi_label_color};  /* Label color */
    }}
    .kpi-value {{
        font-size: 25px;
        color: {kpi_value_color};  /* Value color */
    }}
    </style>
    """

    # Insert KPI with background
    st.markdown(kpi_style, unsafe_allow_html=True)
    st.markdown(
        f"""
    <div class="kpi-box">
        <div>{kpi_label}</div>
        <div class="kpi-value">{total_states}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# Function to create a KPI for the number of years by Country with adaptive background
def display_Year_kpi(salebicyles_df, selected_Country=None, bg_option="Default"):
    # Define background and text colors based on the selected background option
    if bg_option == "Dark Color":
        kpi_bg_color = "rgba(45, 45, 45, 0.85)"  # Dark grey with a hint of opacity
        kpi_value_color = "#007bff"  # White text for dark background
        kpi_label_color = "#ffffff"  # White text
    elif bg_option == "Light Color":
        kpi_bg_color = "rgba(240, 240, 240, 0.9)"
        kpi_value_color = "#007bff"  # Blue text for light background
        kpi_label_color = "#333333"  # Darker text color
    elif bg_option == "Daltonien":
        kpi_bg_color = "rgba(200, 200, 200, 0.9)"
        kpi_value_color = "#ff7f0e"  # Orange text for neutral visibility
        kpi_label_color = "#555555"  # Neutral grey text
    else:
        # Default background and text colors
        kpi_bg_color = "rgba(0, 123, 255, 0.2)"  # Blueish background
        kpi_value_color = "#007bff"
        kpi_label_color = "#333333"

    # Custom CSS for the KPI box with dynamic background and text color
    kpi_style = f"""
    <style>
    .kpi-box {{
        background-color: {kpi_bg_color};  /* Dynamic background color */
        padding: 10px;  /* Adjust padding */
        border-radius: 8px;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 5px;  /* Adjust margin-bottom */
        color: {kpi_label_color};  /* Label color */
    }}
    .kpi-value {{
        font-size: 25px;
        color: {kpi_value_color};  /* Value color */
    }}
    </style>
    """

    # Insert the CSS into Streamlit
    st.markdown(kpi_style, unsafe_allow_html=True)

    if selected_Country:
        # Grouping the data by Country and counting unique years for the selected Country
        kpi_data = (
            salebicyles_df[salebicyles_df["Country"] == selected_Country]
            .groupby("Country", observed=False)["Year"]
            .nunique()
            .reset_index()
        )
        kpi_data.columns = ["Country", "Number of years"]

        # Display the KPI for the selected Country with background
        for _, row in kpi_data.iterrows():
            st.markdown(
                f"""
            <div class="kpi-box">
                <div>Total years in {row["Country"]}</div>
                <div class="kpi-value">{row["Number of years"]}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
    else:
        # Display total years across all countries when no Country is selected
        total_years = salebicyles_df["Year"].nunique()
        st.markdown(
            f"""
        <div class="kpi-box">
            <div>Total years</div>
            <div class="kpi-value">{total_years}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )


# Function to display Total Revenue KPI
def display_total_revenue_kpi(salebicyles_df, bg_option="Default"):
    # Calculate total revenue
    total_revenue = salebicyles_df["Revenue"].sum()

    # Set background and text colors based on the selected background option
    if bg_option == "Dark Color":
        kpi_bg_color = "rgba(45, 45, 45, 0.85)"
        kpi_value_color = "#ffffff"
        kpi_label_color = "#ffffff"
    elif bg_option == "Light Color":
        kpi_bg_color = "rgba(240, 240, 240, 0.9)"
        kpi_value_color = "#007bff"
        kpi_label_color = "#333333"
    elif bg_option == "Daltonien":
        kpi_bg_color = "rgba(200, 200, 200, 0.9)"
        kpi_value_color = "#ff7f0e"
        kpi_label_color = "#555555"
    else:
        kpi_bg_color = "rgba(0, 123, 255, 0.2)"
        kpi_value_color = "#007bff"
        kpi_label_color = "#333333"

    # Display the KPI
    kpi_style = f"""
    <style>
    .kpi-box {{
        background-color: {kpi_bg_color};
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 5px;
        color: {kpi_label_color};
    }}
    .kpi-value {{
        font-size: 25px;
        color: {kpi_value_color};
    }}
    </style>
    """

    st.markdown(kpi_style, unsafe_allow_html=True)
    st.markdown(
        f"""
    <div class="kpi-box">
        <div>Total Revenue</div>
        <div class="kpi-value">${total_revenue:,.2f}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# Function to display Total Units Sold KPI
def display_total_units_sold_kpi(salebicyles_df, bg_option="Default"):
    # Calculate total units sold
    total_units_sold = salebicyles_df["Order_Quantity"].sum()

    # Set background and text colors based on the selected background option
    if bg_option == "Dark Color":
        kpi_bg_color = "rgba(45, 45, 45, 0.85)"
        kpi_value_color = "#ffffff"
        kpi_label_color = "#ffffff"
    elif bg_option == "Light Color":
        kpi_bg_color = "rgba(240, 240, 240, 0.9)"
        kpi_value_color = "#007bff"
        kpi_label_color = "#333333"
    elif bg_option == "Daltonien":
        kpi_bg_color = "rgba(200, 200, 200, 0.9)"
        kpi_value_color = "#ff7f0e"
        kpi_label_color = "#555555"
    else:
        kpi_bg_color = "rgba(0, 123, 255, 0.2)"
        kpi_value_color = "#007bff"
        kpi_label_color = "#333333"

    # Display the KPI
    kpi_style = f"""
    <style>
    .kpi-box {{
        background-color: {kpi_bg_color};
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 5px;
        color: {kpi_label_color};
    }}
    .kpi-value {{
        font-size: 25px;
        color: {kpi_value_color};
    }}
    </style>
    """

    st.markdown(kpi_style, unsafe_allow_html=True)
    st.markdown(
        f"""
    <div class="kpi-box">
        <div>Total Units Sold</div>
        <div class="kpi-value">{total_units_sold:,}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# Function to display Average Profit Margin KPI
def display_avg_profit_margin_kpi(salebicyles_df, bg_option="Default"):
    # Calculate average profit margin (Profit/Revenue)
    salebicyles_df["Profit_Margin"] = (
        salebicyles_df["Profit"] / salebicyles_df["Revenue"]
    )
    avg_profit_margin = salebicyles_df["Profit_Margin"].mean() * 100

    # Set background and text colors based on the selected background option
    if bg_option == "Dark Color":
        kpi_bg_color = "rgba(45, 45, 45, 0.85)"
        kpi_value_color = "#ffffff"
        kpi_label_color = "#ffffff"
    elif bg_option == "Light Color":
        kpi_bg_color = "rgba(240, 240, 240, 0.9)"
        kpi_value_color = "#007bff"
        kpi_label_color = "#333333"
    elif bg_option == "Daltonien":
        kpi_bg_color = "rgba(200, 200, 200, 0.9)"
        kpi_value_color = "#ff7f0e"
        kpi_label_color = "#555555"
    else:
        kpi_bg_color = "rgba(0, 123, 255, 0.2)"
        kpi_value_color = "#007bff"
        kpi_label_color = "#333333"

    # Display the KPI
    kpi_style = f"""
    <style>
    .kpi-box {{
        background-color: {kpi_bg_color};
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 5px;
        color: {kpi_label_color};
    }}
    .kpi-value {{
        font-size: 25px;
        color: {kpi_value_color};
    }}
    </style>
    """

    st.markdown(kpi_style, unsafe_allow_html=True)
    st.markdown(
        f"""
    <div class="kpi-box">
        <div>Average Profit Margin</div>
        <div class="kpi-value">{avg_profit_margin:.2f}%</div>
    </div>
    """,
        unsafe_allow_html=True,
    )
