import streamlit as st
from style_css import inject_background_css


# Function to handle sidebar filters and return filtered dataframe
def sidebar_filters(salebicyles_df):
    st.sidebar.header("Filters")

    # Dropdown to switch background images
    bg_options = ["Background Image", "Dark Color", "Light Color", "Daltonien"]
    selected_bg = st.sidebar.selectbox("Select Background", bg_options)

    # Save the selected background option in session state
    st.session_state["background_option"] = selected_bg

    # Inject the selected background based on user choice
    inject_background_css(selected_bg)

    # Handle cases where data is not yet available (before file upload)
    if salebicyles_df is None:
        countries = []
        states = []
        years = []
        categories = []
        subcategories = []
    else:
        # Populate dropdowns with data if file is uploaded
        countries = salebicyles_df["Country"].unique().tolist()
        countries.insert(0, "Select All")

    # Multi-select dropdown for Countries
    selected_countries = st.sidebar.multiselect(
        "Select Countries", options=countries, disabled=salebicyles_df is None
    )

    if "Select All" in selected_countries or len(selected_countries) == 0:
        selected_countries = countries[1:] if salebicyles_df is not None else []

    # Filter the dataframe by the selected countries
    if salebicyles_df is not None:
        filtered_df = salebicyles_df[salebicyles_df["Country"].isin(selected_countries)]
    else:
        filtered_df = None

    # Now dynamically filter states based on selected countries
    if filtered_df is not None and not filtered_df.empty:
        states = filtered_df["State"].unique().tolist()
        states.insert(0, "Select All")
    else:
        states = []

    # Multi-select dropdown for states (only show states from the selected countries)
    selected_states = st.sidebar.multiselect(
        "Select States",
        options=states,
        disabled=salebicyles_df is None or not selected_countries,
    )

    if "Select All" in selected_states or len(selected_states) == 0:
        selected_states = states[1:] if salebicyles_df is not None else []

    # Further filter the dataframe by the selected states
    if filtered_df is not None:
        filtered_df = (
            filtered_df[filtered_df["State"].isin(selected_states)]
            if filtered_df is not None
            else None
        )

    # Now dynamically filter years based on the selected countries and states
    if filtered_df is not None and not filtered_df.empty:
        years = filtered_df["Year"].unique().tolist()
        years.insert(0, "Select All")
    else:
        years = []

    # Multi-select dropdown for years (only show years from the selected countries and states)
    selected_years = st.sidebar.multiselect(
        "Select Years",
        options=years,
        disabled=salebicyles_df is None or not selected_states,
    )

    if "Select All" in selected_years or len(selected_years) == 0:
        selected_years = years[1:] if salebicyles_df is not None else []

    # Further filter the dataframe by the selected years
    if filtered_df is not None:
        filtered_df = (
            filtered_df[filtered_df["Year"].isin(selected_years)]
            if filtered_df is not None
            else None
        )

    # Now dynamically filter Product Categories based on selected countries, states, and years
    if filtered_df is not None and not filtered_df.empty:
        categories = filtered_df["Product_Category"].unique().tolist()
        categories.insert(0, "Select All")
    else:
        categories = []

    # Multi-select dropdown for Product Categories
    selected_categories = st.sidebar.multiselect(
        "Select Product Categories",
        options=categories,
        disabled=salebicyles_df is None or not selected_years,
    )

    if "Select All" in selected_categories or len(selected_categories) == 0:
        selected_categories = categories[1:] if salebicyles_df is not None else []

    # Further filter the dataframe by the selected categories
    if filtered_df is not None:
        filtered_df = (
            filtered_df[filtered_df["Product_Category"].isin(selected_categories)]
            if filtered_df is not None
            else None
        )

    # Now dynamically filter Sub Categories based on selected Product Categories
    if filtered_df is not None and not filtered_df.empty:
        subcategories = filtered_df["Sub_Category"].unique().tolist()
        subcategories.insert(0, "Select All")
    else:
        subcategories = []

    # Multi-select dropdown for Sub Categories
    selected_subcategories = st.sidebar.multiselect(
        "Select Sub Categories",
        options=subcategories,
        disabled=salebicyles_df is None or not selected_categories,
    )

    if "Select All" in selected_subcategories or len(selected_subcategories) == 0:
        selected_subcategories = subcategories[1:] if salebicyles_df is not None else []

    # Further filter the dataframe by the selected subcategories
    if filtered_df is not None:
        filtered_df = (
            filtered_df[filtered_df["Sub_Category"].isin(selected_subcategories)]
            if filtered_df is not None
            else None
        )

    return filtered_df, selected_countries
