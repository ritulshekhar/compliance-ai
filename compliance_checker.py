import os
from typing import List, Dict, Any
from openai import OpenAI
from pii_detector import PIIDetector
from compliance_frameworks import FRAMEWORKS

class ComplianceChecker:
    def __init__(self, api_key: str = None, frameworks: List[str] = None, include_pii: bool = True, include_ai_analysis: bool = True):
        self.client = OpenAI(api_key=api_key) if api_key else None
        self.frameworks = frameworks or list(FRAMEWORKS.keys())
        self.include_pii = include_pii
        self.include_ai_analysis = include_ai_analysis
        self.pii_detector = PIIDetector() if include_pii else None

    def analyze_document(self, text_content: str) -> Dict[str, Any]:
        results = {
            "pii_detected": [],
            "compliance_scores": {},
            "violations": [],
            "ai_insights": "AI Analysis not enabled or API key missing."
        }

        # 1. PII Detection
        if self.include_pii and self.pii_detector:
            results["pii_detected"] = self.pii_detector.detect_pii(text_content)

        # 2. Heuristic Analysis (Keyword matching)
        scores = {}
        for fw in self.frameworks:
            keywords = FRAMEWORKS.get(fw, {}).get("keywords", [])
            matches = [kw for kw in keywords if kw.lower() in text_content.lower()]
            # Simple scoring: % of key terms found
            score = (len(matches) / len(keywords)) * 100 if keywords else 0
            scores[fw] = round(score, 2)
            
            if score < 50:
                results["violations"].append({
                    "framework": fw, 
                    "issue": f"Low keyword coverage ({score}%)", 
                    "severity": "High" if score < 20 else "Medium"
                })

        results["compliance_scores"] = scores

        # 3. AI Analysis
        if self.include_ai_analysis and self.client:
            try:
                results["ai_insights"] = self._run_ai_analysis(text_content)
            except Exception as e:
                results["ai_insights"] = f"AI Analysis failed: {str(e)}"
        
        return results

    def _run_ai_analysis(self, text: str) -> str:
        # Truncate text to avoid token limits if necessary
        truncated_text = text[:15000] 
        prompt = f"""
        Analyze the following text for compliance violations against these frameworks: {', '.join(self.frameworks)}.
        
        Text content:
        {truncated_text}
        
        Provide a concise summary of:
        1. Key Compliance Risks
        2. Missing Disclosures
        3. Recommendations
        """

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert compliance auditor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
