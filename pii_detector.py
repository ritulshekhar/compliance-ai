import spacy
import re
from typing import List, Dict, Any

class PIIDetector:
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            # If model is not found, we'll wait for the user to install it or handle it gracefully
            print("Warning: spacy model 'en_core_web_sm' not found. PII detection will be limited to regex.")
            self.nlp = None

        self.regex_patterns = {
            "EMAIL": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            "PHONE": r'\b(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b',
            "SSN": r'\b\d{3}-\d{2}-\d{4}\b',
            "CREDIT_CARD": r'\b(?:\d{4}[-\s]?){3}\d{4}\b',
            "URL": r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
        }

    def detect_pii(self, text: str) -> List[Dict[str, Any]]:
        pii_entities = []

        # 1. Regex-based detection
        for label, pattern in self.regex_patterns.items():
            matches = re.finditer(pattern, text)
            for match in matches:
                pii_entities.append({
                    "text": match.group(),
                    "label": label,
                    "start": match.start(),
                    "end": match.end(),
                    "method": "Regex"
                })

        # 2. NLP-based detection (if model available)
        if self.nlp:
            # Clean text specifically for NLP if needed, but usually raw is fine
            # Limit text length to avoid memory issues on large docs for checking
            doc = self.nlp(text[:100000]) 
            for ent in doc.ents:
                if ent.label_ in ["PERSON", "ORG", "GPE", "DATE"]:
                    # We might want to filter what we consider "PII"
                    if ent.label_ == "PERSON":
                         pii_entities.append({
                            "text": ent.text,
                            "label": ent.label_,
                            "start": ent.start_char,
                            "end": ent.end_char,
                            "method": "spaCy"
                        })
        
        return pii_entities
