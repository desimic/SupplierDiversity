import streamlit as st

VENDORS = [
    {"name": "Patriot Logistics", "cert_type": "DVBE", "services": ["Transportation", "Logistics"], "region": "Central Coast"},
    {"name": "GreenTech Supplies", "cert_type": "SB", "services": ["Paper", "Office Supplies"], "region": "Southern California"},
    {"name": "Sierra Networks", "cert_type": "SB", "services": ["IT Hardware", "Networking"], "region": "Northern California"},
    {"name": "Veteran Mechanical", "cert_type": "DVBE", "services": ["HVAC", "Plumbing"], "region": "Central Coast"}
]

st.title("SB/DVBE Vendor Search Tool")
service = st.text_input("Enter a service keyword", "IT")
region = st.selectbox("Select region (optional)", ["All", "Central Coast", "Southern California", "Northern California"])

results = []
for v in VENDORS:
    if service.lower() in " ".join(v["services"]).lower():
        if region == "All" or v["region"] == region:
            results.append(v)

st.subheader(f"Found {len(results)} vendor(s):")
st.json(results)