"""
Clinical Trial Protocol Analyzer Agent
Analyzes clinical trial protocols for discrepancies and answers questions
"""

import pdfplumber
import os
from typing import List, Dict
import re


class ProtocolAnalyzer:
    """Analyzes clinical trial protocols for common issues and discrepancies"""
    
    def __init__(self):
        self.protocol_text = ""
        self.protocol_metadata = {}
        
    def load_protocol(self, pdf_path: str) -> str:
        """Load and extract text from PDF protocol"""
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"Protocol file not found: {pdf_path}")
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                self.protocol_text = ""
                for page in pdf.pages:
                    self.protocol_text += page.extract_text() + "\n"
            
            print(f"✓ Protocol loaded successfully ({len(pdf.pages)} pages)")
            return self.protocol_text
        except Exception as e:
            raise Exception(f"Error reading PDF: {str(e)}")
    
    def check_discrepancies(self) -> List[Dict]:
        """Check for common discrepancies in clinical trial protocols"""
        issues = []
        text = self.protocol_text.lower()
        
        # Check 1: Enrollment criteria consistency
        if "inclusion criteria" in text:
            inclusion_idx = text.find("inclusion criteria")
            exclusion_idx = text.find("exclusion criteria")
            
            if exclusion_idx == -1:
                issues.append({
                    "severity": "high",
                    "issue": "Missing Exclusion Criteria",
                    "description": "Exclusion criteria section not found. All protocols should specify exclusion criteria.",
                    "recommendation": "Add a clear exclusion criteria section"
                })
        
        # Check 2: Primary and secondary endpoints
        if "primary endpoint" not in text and "primary outcome" not in text:
            issues.append({
                "severity": "high",
                "issue": "Missing Primary Endpoint",
                "description": "Primary endpoint is not clearly defined",
                "recommendation": "Clearly define the primary efficacy endpoint"
            })
        
        if "secondary endpoint" not in text and "secondary outcome" not in text:
            issues.append({
                "severity": "medium",
                "issue": "Missing Secondary Endpoints",
                "description": "Secondary endpoints are not defined",
                "recommendation": "Define secondary endpoints for exploratory analysis"
            })
        
        # Check 3: Safety reporting
        if "adverse event" not in text and "safety" not in text:
            issues.append({
                "severity": "high",
                "issue": "Missing Adverse Event Definitions",
                "description": "Adverse event monitoring plan is not specified",
                "recommendation": "Include clear AE grading and reporting procedures"
            })
        
        # Check 4: Study population details
        if "sample size" not in text and "n=" not in text and "enrollment" not in text:
            issues.append({
                "severity": "medium",
                "issue": "Sample Size Not Specified",
                "description": "Target sample size or enrollment number is unclear",
                "recommendation": "Specify the target sample size with justification"
            })
        
        # Check 5: Statistical analysis plan
        if "statistical analysis" not in text and "analysis plan" not in text:
            issues.append({
                "severity": "medium",
                "issue": "Statistical Analysis Plan",
                "description": "Statistical analysis approach is not detailed",
                "recommendation": "Include a comprehensive statistical analysis plan"
            })
        
        # Check 6: Study duration
        if "duration" not in text and "follow-up" not in text:
            issues.append({
                "severity": "low",
                "issue": "Study Duration Not Clear",
                "description": "Duration of patient follow-up is not specified",
                "recommendation": "Clearly state the study duration and follow-up periods"
            })
        
        return issues
    
    def search_protocol(self, query: str) -> List[str]:
        """Search for specific information in the protocol"""
        results = []
        query_lower = query.lower()
        lines = self.protocol_text.split('\n')
        
        for line in lines:
            if query_lower in line.lower() and len(line.strip()) > 0:
                results.append(line.strip())
        
        return results if results else ["No relevant information found for: " + query]
    
    def get_section(self, section_name: str) -> str:
        """Extract a specific section from the protocol"""
        text_lower = self.protocol_text.lower()
        section_lower = section_name.lower()
        
        start_idx = text_lower.find(section_lower)
        if start_idx == -1:
            return f"Section '{section_name}' not found"
        
        # Try to find the next section
        next_sections = ["background", "methods", "results", "discussion", "references", 
                        "appendix", "conclusion", "statistical", "analysis"]
        
        end_idx = len(self.protocol_text)
        for section in next_sections:
            idx = text_lower.find(section, start_idx + 1)
            if idx != -1 and idx < end_idx:
                end_idx = idx
        
        return self.protocol_text[start_idx:end_idx].strip()
    
    def generate_summary(self) -> Dict:
        """Generate a summary of the protocol"""
        summary = {
            "total_pages_approx": len(self.protocol_text.split('\n')) // 30,
            "has_study_design": "study design" in self.protocol_text.lower(),
            "has_inclusion_criteria": "inclusion" in self.protocol_text.lower(),
            "has_exclusion_criteria": "exclusion" in self.protocol_text.lower(),
            "has_primary_endpoint": "primary" in self.protocol_text.lower(),
            "has_safety_plan": "adverse" in self.protocol_text.lower() or "safety" in self.protocol_text.lower(),
        }
        return summary


def main():
    """Main function to demonstrate protocol analysis"""
    print("=" * 60)
    print("Clinical Trial Protocol Analyzer Agent")
    print("=" * 60)
    
    analyzer = ProtocolAnalyzer()
    
    # Example usage
    pdf_file = "protocol.pdf"  # User should provide their own protocol
    
    try:
        if os.path.exists(pdf_file):
            # Load protocol
            analyzer.load_protocol(pdf_file)
            
            # Get summary
            print("\n📋 Protocol Summary:")
            summary = analyzer.generate_summary()
            for key, value in summary.items():
                print(f"  • {key}: {value}")
            
            # Check for discrepancies
            print("\n🔍 Quality Check - Potential Issues:")
            issues = analyzer.check_discrepancies()
            if issues:
                for i, issue in enumerate(issues, 1):
                    print(f"\n  {i}. [{issue['severity'].upper()}] {issue['issue']}")
                    print(f"     Issue: {issue['description']}")
                    print(f"     Recommendation: {issue['recommendation']}")
            else:
                print("  ✓ No major issues detected")
            
            # Interactive mode
            print("\n" + "=" * 60)
            print("💬 Ask questions about the protocol (type 'quit' to exit)")
            print("=" * 60)
            
            while True:
                user_query = input("\nYour question: ").strip()
                if user_query.lower() in ['quit', 'exit', 'q']:
                    break
                
                results = analyzer.search_protocol(user_query)
                print("\n📌 Relevant Information:")
                for result in results[:3]:  # Show top 3 results
                    print(f"  • {result}")
        
        else:
            print(f"\n❌ File '{pdf_file}' not found")
            print(f"Please place your clinical trial protocol PDF in the same directory")
            print(f"and name it '{pdf_file}'")
            print("\nExample usage:")
            print("  1. Place your protocol.pdf in this directory")
            print("  2. Run this script")
            print("  3. The agent will analyze the protocol and answer your questions")
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")


if __name__ == "__main__":
    main()
