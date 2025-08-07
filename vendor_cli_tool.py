import json

VENDORS = [
    {"name": "Patriot Logistics", "cert_type": "DVBE", "services": ["Transportation", "Logistics"], "region": "Central Coast"},
    {"name": "GreenTech Supplies", "cert_type": "SB", "services": ["Paper", "Office Supplies"], "region": "Southern California"},
    {"name": "Sierra Networks", "cert_type": "SB", "services": ["IT Hardware", "Networking"], "region": "Northern California"},
    {"name": "Veteran Mechanical", "cert_type": "DVBE", "services": ["HVAC", "Plumbing"], "region": "Central Coast"}
]

def search(service, region=None):
    results = []
    for v in VENDORS:
        if service.lower() in " ".join(v["services"]).lower():
            if not region or v["region"] == region:
                results.append(v)
    return results

def main():
    print("SB/DVBE Vendor CLI Lookup Tool")
    service = input("Enter service type (e.g., Plumbing, IT, Office): ")
    region = input("Enter region (optional): ").strip() or None
    found = search(service, region)
    print(f"\n{len(found)} vendor(s) found:\n")
    print(json.dumps(found, indent=2))

if __name__ == "__main__":
    main()