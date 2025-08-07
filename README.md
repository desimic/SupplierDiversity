# Cal Poly SB/DVBE Procurement Automation Toolkit

This repository provides scripts, templates, and visual architecture to help Cal Poly San Luis Obispo meet its mandated 25% Small Business (SB) and 3% Disabled Veteran Business Enterprise (DVBE) participation goals.

## Contents

- `vendor_lookup.py`: Simulates vendor discovery by service/region.
- `vendor_cli_tool.py`: CLI-based vendor search tool.
- `vendor_streamlit_app.py`: Web-based vendor interface (Streamlit).
- `sb_dvbe_policy.yaml`: YAML policy for compliance enforcement.
- `vendor_evaluation_claude_prompts.jsonl`: JSONL prompts for Claude LLM evaluation.
- `supplier_diversity_architecture_diagram.png`: System flow diagram.

## Requirements

- Python 3.8+
- Optional: `streamlit` for web app

## Run the Streamlit App

```bash
pip install streamlit
streamlit run vendor_streamlit_app.py
```