# Clinical Trial Protocol Analyzer Agent 🏥🤖

## Overview
An AI-powered agent that analyzes clinical trial protocols to identify potential issues, discrepancies, and answers questions about protocol details. This project demonstrates expertise in clinical research methodology and AI implementation.

## Features
✅ **PDF Protocol Reading** - Upload and parse clinical trial protocols  
✅ **Quality Checks** - Identifies common discrepancies and missing sections  
✅ **Interactive Q&A** - Ask questions about the protocol  
✅ **Issue Detection** - Flags missing endpoints, safety plans, enrollment criteria, etc.  
✅ **Section Extraction** - Retrieves specific sections from protocols  
✅ **Protocol Summary** - Generates a quick overview of the protocol structure  

## Detected Issues
The agent checks for:
- Missing or unclear inclusion/exclusion criteria
- Undefined primary and secondary endpoints
- Absent adverse event definitions
- Missing sample size specifications
- Incomplete statistical analysis plans
- Unclear study duration

## Installation

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Prepare Your Protocol
- Place your clinical trial protocol PDF in the project directory
- Name it `protocol.pdf` (or modify the filename in the script)

### 3. Run the Agent
```bash
python clinical_protocol_agent.py
```

## Usage Example
```python
from clinical_protocol_agent import ProtocolAnalyzer

# Initialize the analyzer
analyzer = ProtocolAnalyzer()

# Load a protocol
analyzer.load_protocol("my_protocol.pdf")

# Check for discrepancies
issues = analyzer.check_discrepancies()
for issue in issues:
    print(f"[{issue['severity']}] {issue['issue']}")

# Search for specific information
results = analyzer.search_protocol("inclusion criteria")

# Get protocol summary
summary = analyzer.generate_summary()
```

## API Functions

### `load_protocol(pdf_path: str) -> str`
Loads and extracts text from a clinical trial protocol PDF.

### `check_discrepancies() -> List[Dict]`
Analyzes the protocol for common issues and returns a list of detected discrepancies.

### `search_protocol(query: str) -> List[str]`
Searches for specific information within the protocol.

### `get_section(section_name: str) -> str`
Extracts a specific section (e.g., "Methods", "Inclusion Criteria") from the protocol.

### `generate_summary() -> Dict`
Returns a summary of the protocol structure and key components.

## Technical Stack
- **Python 3.8+**
- **pdfplumber** - PDF text extraction
- **LangChain** - Agent framework (ready for LLM integration)
- **Regular Expressions** - Pattern matching for clinical data

## Future Enhancements
🚀 Integrate with free LLMs (Ollama, HuggingFace)  
🚀 Extract structured data (enrollment numbers, study duration, etc.)  
🚀 Generate compliance reports  
🚀 Support for multiple document formats  
🚀 Machine learning models for endpoint prediction  
🚀 Integration with ClinicalTrials.gov API  

## Skills Demonstrated
✨ Clinical Research Knowledge (protocol structure, GCP)  
✨ Python Programming  
✨ PDF Processing & Text Analysis  
✨ AI/ML Agent Development  
✨ Data Extraction & Quality Assurance  
✨ Healthcare Data Handling  

## License
Open source - feel free to use and modify

---
**Built by:** Anjali Dereck | MSc Drug Discovery with AI | University of Liverpool
