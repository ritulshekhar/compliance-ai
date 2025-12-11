try:
    from document_processor import DocumentProcessor
    from pii_detector import PIIDetector
    from compliance_checker import ComplianceChecker
    from report_generator import ReportGenerator
    import spacy
    
    print("Imports successful.")
    
    try:
        nlp = spacy.load("en_core_web_sm")
        print("SpaCy model loaded.")
    except Exception as e:
        print(f"SpaCy model load failed: {e}")

    doc_proc = DocumentProcessor()
    print("DocumentProcessor instantiated.")
    
    detector = PIIDetector()
    print("PIIDetector instantiated.")
    
    checker = ComplianceChecker(frameworks=["GDPR"])
    print("ComplianceChecker instantiated.")
    
    gen = ReportGenerator()
    print("ReportGenerator instantiated.")

    print("Smoke test passed!")

except Exception as e:
    print(f"Smoke test failed: {e}")
