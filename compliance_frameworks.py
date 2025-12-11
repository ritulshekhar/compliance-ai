from typing import Dict, List

# Definitions of frameworks and their key indicators for heuristic analysis
FRAMEWORKS: Dict[str, Dict[str, List[str]]] = {
    "GDPR": {
        "keywords": [
            "personal data", "data subject", "consent", "right to erasure", 
            "data protection officer", "dpo", "processing", "controller", "processor",
            "article 6", "article 30", "privacy by design"
        ],
        "description": "General Data Protection Regulation (EU). Focuses on data protection and privacy."
    },
    "SOC2": {
        "keywords": [
            "security", "availability", "processing integrity", "confidentiality", 
            "privacy", "control", "audit", "access control", "monitoring", "incident response",
            "disaster recovery", "encryption"
        ],
        "description": "System and Organization Controls 2. Focuses on non-financial reporting controls."
    },
    "HIPAA": {
        "keywords": [
            "phi", "protected health information", "covered entity", "business associate",
            "medical record", "patient privacy", "health insurance", "security rule",
            "privacy rule", "breach notification"
        ],
        "description": "Health Insurance Portability and Accountability Act. Focuses on healthcare data."
    },
    "RBI": {
        "keywords": [
            "reserve bank of india", "payment system", "data localization", "storage of payment system data",
            "kyc", "aml", "cyber security framework", "outsourcing", "customer protection"
        ],
        "description": "Reserve Bank of India Guidelines. Focuses on financial compliance in India."
    }
}
