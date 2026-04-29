"""
Example usage of the Clinical Trial Protocol Analyzer Agent
"""

from clinical_protocol_agent import ProtocolAnalyzer


def example_usage():
    """Demonstrates how to use the protocol analyzer"""
    
    print("=" * 70)
    print("EXAMPLE: Clinical Trial Protocol Analyzer Agent")
    print("=" * 70)
    
    # Initialize analyzer
    analyzer = ProtocolAnalyzer()
    
    # Example 1: Load a protocol
    print("\n📂 Step 1: Loading protocol...")
    try:
        # Replace with your actual PDF path
        analyzer.load_protocol("your_protocol.pdf")
    except FileNotFoundError:
        print("   ⚠️  No protocol.pdf found. Showing example functionality...")
        
        # For demonstration, we'll use a sample protocol text
        analyzer.protocol_text = """
        Clinical Trial Protocol: A Phase III Study of Treatment X
        
        1. BACKGROUND
        Study of new treatment for disease Y.
        
        2. INCLUSION CRITERIA
        - Age 18-75
        - Diagnosed with disease Y
        - Willing to participate
        
        3. METHODS
        Primary endpoint: Efficacy at week 12
        Secondary endpoints: Safety and tolerability
        
        4. ADVERSE EVENTS
        All adverse events will be recorded and graded.
        """
        print("   ✓ Sample protocol loaded for demonstration")
    
    # Example 2: Generate summary
    print("\n📋 Step 2: Protocol Summary")
    print("-" * 70)
    summary = analyzer.generate_summary()
    for key, value in summary.items():
        status = "✓" if value else "✗"
        print(f"   {status} {key}: {value}")
    
    # Example 3: Check for discrepancies
    print("\n🔍 Step 3: Quality Check - Identified Issues")
    print("-" * 70)
    issues = analyzer.check_discrepancies()
    
    if issues:
        for i, issue in enumerate(issues, 1):
            print(f"\n   Issue {i}: {issue['issue']}")
            print(f"   Severity: {issue['severity'].upper()}")
            print(f"   Description: {issue['description']}")
            print(f"   Recommendation: {issue['recommendation']}")
    else:
        print("   ✓ No major issues detected!")
    
    # Example 4: Search functionality
    print("\n💬 Step 4: Search Example")
    print("-" * 70)
    search_queries = [
        "inclusion criteria",
        "primary endpoint",
        "adverse events"
    ]
    
    for query in search_queries:
        print(f"\n   Query: '{query}'")
        results = analyzer.search_protocol(query)
        for result in results[:2]:
            print(f"   → {result[:80]}...")
    
    print("\n" + "=" * 70)
    print("💡 HOW TO USE WITH YOUR OWN PROTOCOL:")
    print("=" * 70)
    print("""
    1. Place your clinical trial protocol PDF in the same directory
    2. Update the filename in the script (default: "protocol.pdf")
    3. Run the agent:
       
       python clinical_protocol_agent.py
    
    4. The agent will:
       ✓ Load and analyze your protocol
       ✓ Check for common discrepancies
       ✓ Answer your questions about the protocol
       ✓ Extract specific sections on demand
    
    5. Interactive mode features:
       - Type any question about the protocol
       - The agent searches for relevant information
       - Type 'quit' to exit
    """)
    
    print("\n📚 API EXAMPLES:")
    print("-" * 70)
    print("""
    # Load a protocol
    analyzer.load_protocol("my_protocol.pdf")
    
    # Check for issues
    issues = analyzer.check_discrepancies()
    
    # Search for specific information
    results = analyzer.search_protocol("inclusion criteria")
    
    # Extract a section
    methods = analyzer.get_section("Methods")
    
    # Get summary
    summary = analyzer.generate_summary()
    """)


if __name__ == "__main__":
    example_usage()
