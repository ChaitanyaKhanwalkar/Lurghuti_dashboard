
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Lurghuti Watershed Dashboard", layout="wide")

watershed_name = "LURGHUTI"
total_area = 1027.29
fund_received = 14766369
fund_spent = 13950313
fund_percent = 94.47

st.title("🌿 Madhya Pradesh Watershed Planner")
st.subheader(f"Watershed: {watershed_name}")

colf1, colf2, colf3 = st.columns([1,1,1])
colf1.selectbox("📍 Watershed", ["LURGHUTI"], index=0)
colf2.selectbox("📅 Quarter", ["Q1", "Q2", "Q3", "Q4"], index=3)
colf3.selectbox("📆 Financial Year", ["2023-24", "2024-25"], index=0)

col1, col2, col3, col4 = st.columns(4)
col1.metric("📐 Total Area", f"{total_area} ha")
col2.metric("💰 Fund Received", f"₹{fund_received:,}")
col3.metric("💸 Fund Spent", f"₹{fund_spent:,}")
col4.metric("📊 Fund Utilized", f"{fund_percent}%")

st.markdown("### 💧 Hydrological Indicators")
colh1, colh2, colh3 = st.columns(3)
colh1.metric("Avg. Rainfall", "1243 mm")
colh2.metric("Recharge Potential", "61% (Moderate)")
colh3.metric("Soil Moisture Index", "48%")
soil_chart = px.line(x=[1,2,3,4,5], y=[42, 46, 49, 45, 48], labels={"x": "Quarter", "y": "Soil Moisture %"})
colh3.plotly_chart(soil_chart, use_container_width=True)

st.markdown("### 🛠️ Intervention Tracker")
st.markdown("_(Static numbers – replace with real intervention data later)_")
colt1, colt2 = st.columns(2)
with colt1:
    st.progress(0.75, "Check Dams (75%)")
    st.progress(0.85, "Farm Bunds (85%)")
with colt2:
    st.progress(0.53, "Percolation Pits (53%)")
    st.progress(0.82, "Plantation (82%)")

st.markdown("### 🗣️ Community Feedback & Participation")
st.checkbox("Community Meetings Conducted", value=True)
st.checkbox("PRI Representatives Consulted", value=True)
st.checkbox("Comments Available", value=True)

colmap, colx = st.columns([2,1])
with colmap:
    st.markdown("### 🗺️ GIS Map View")
    st.image(
    "lurghuti_map.png",
    caption="Recharge/Discharge Zones (placeholder)",
    use_container_width=True
)



with colx:
    st.markdown("### 📤 Export QPR Report")
    st.button("Download Dashboard Snapshot")
    st.button("Download GeoJSON Layer")

st.markdown("---")
st.caption("Dashboard generated using Streamlit | Data: QPR Lurghuti Watershed 2023-24")
