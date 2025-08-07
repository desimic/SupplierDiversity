import json

# Simulated SB/DVBE vendor data (mockup)
VENDORS = [
    {"name": "Patriot Logistics", "cert_type": "DVBE", "services": ["Transportation", "Logistics"], "region": "Central Coast"},
    {"name": "GreenTech Supplies", "cert_type": "SB", "services": ["Paper", "Office Supplies"], "region": "Southern California"},
    {"name": "Sierra Networks", "cert_type": "SB", "services": ["IT Hardware", "Networking"], "region": "Northern California"},
    {"name": "Veteran Mechanical", "cert_type": "DVBE", "services": ["HVAC", "Plumbing"], "region": "Central Coast"}
]

def search_vendors(service_keyword, region_filter=None):
    results = []
    for vendor in VENDORS:
        if service_keyword.lower() in " ".join(vendor["services"]).lower():
            if region_filter is None or vendor["region"] == region_filter:
                results.append(vendor)
    return results

if __name__ == "__main__":
    keyword = input("Enter service keyword: ")
    region = input("Enter region filter (optional): ") or None
    matches = search_vendors(keyword, region)
    print(f"\n✅ {len(matches)} vendor(s) found matching '{keyword}' in region '{region or 'All'}':\n")
    print(json.dumps(matches, indent=2))