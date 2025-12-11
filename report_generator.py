import pandas as pd
import json
import xlsxwriter
import io
from typing import Dict, Any

class ReportGenerator:
    def generate_excel_report(self, analysis_results: Dict[str, Any]) -> bytes:
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            # Summary Sheet
            scores_df = pd.DataFrame(list(analysis_results['compliance_scores'].items()), columns=['Framework', 'Score'])
            scores_df.to_excel(writer, sheet_name='Summary', index=False)

            # PII Sheet
            if analysis_results.get('pii_detected'):
                pii_df = pd.DataFrame(analysis_results['pii_detected'])
                pii_df.to_excel(writer, sheet_name='PII Detected', index=False)
            
            # Violations Sheet
            if analysis_results.get('violations'):
                vio_df = pd.DataFrame(analysis_results['violations'])
                vio_df.to_excel(writer, sheet_name='Violations', index=False)
        
        return output.getvalue()

    def generate_json_report(self, analysis_results: Dict[str, Any]) -> str:
        return json.dumps(analysis_results, indent=2)

    # Simplified PDF generation (usually requires FPDF or ReportLab, keeping it simple for now)
    # Could add text-based report here if needed.
