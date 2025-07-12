import streamlit as st  # Web app framework
import folium  # Interactive maps
from streamlit_folium import st_folium  # Folium integration for Streamlit
from functions import get_location, get_five_starbucks_nearby  # Custom functions

# Page configuration
st.set_page_config(page_title="Nearby Starbucks", layout="wide")

st.title("☕ Nearest Starbucks Branches")

# Get user location
location = get_location()

if location:
    latitude, longitude = location
    st.success(f"Your location has been taken: {latitude}, {longitude}")

    # Create map centered on user location
    m = folium.Map(location=[latitude, longitude], zoom_start=12)

    # Add red marker for user's current location
    folium.Marker(
        location=[latitude, longitude],
        popup="📍 Current Location",
        icon=folium.Icon(color="red")
    ).add_to(m)

    # Search for nearby Starbucks
    with st.spinner("Searching for nearby Starbucks branches..."):
        starbucks_data = get_five_starbucks_nearby()
    
    # Display Starbucks locations if found
    if starbucks_data is not None and not starbucks_data.empty:
        # Add green markers for each Starbucks
        for _, row in starbucks_data.iterrows():
            folium.Marker(
                location=[row["latitude"], row["longitude"]],
                popup=f"☕ {row['name']}",
                icon=folium.Icon(color="green")
            ).add_to(m)

        st.subheader("📋 Nearest Starbucks Branches")
        
        # Select columns to display
        display_columns = []
        available_columns = starbucks_data.columns.tolist()
        
        for col in ["name", "city", "latitude", "longitude", "distance"]:
            if col in available_columns:
                display_columns.append(col)
        
        if display_columns:
            st.dataframe(starbucks_data[display_columns])
        else:
            st.dataframe(starbucks_data)
    else:
        st.warning("No Starbucks branches found nearby.")

    # Display the map
    st_folium(m, width=800, height=600)

else:
    st.error("Could not retrieve your location. Please check your internet connection or try again later.")
