AI-Powered Enterprise Compliance Checker

Intelligent Regulatory Compliance & Risk Assessment using Python, Streamlit, GPT-4o, and NLP
License: MIT

Live URL : https://compliance-documents.streamlit.app/

Overview

The AI-Powered Enterprise Compliance Checker is an automated system for detecting regulatory violations across GDPR, SOC2, HIPAA, and RBI frameworks.
It uses OpenAI GPT-4o, spaCy NLP, rule-based detection, and advanced document processing to evaluate documents, policies, emails, and reports for non-compliance, missing clauses, and potential PII leaks.

The application supports PDF, DOCX, and TXT formats and provides compliance insights, dashboards, exportable reports, and AI-generated recommendations.

Key Features
Multi-Framework Compliance Detection

Supports analysis against:

GDPR (privacy, consent, rights, DPIA)

SOC2 (security, logging, availability, confidentiality)

HIPAA (PHI protection, safeguards, auditing)

RBI (cybersecurity framework, data localization, financial compliance)

AI-Powered Analysis (GPT-4o)

Context-aware analysis of documents

Regulatory interpretation and explanations

Severity-based risk scoring

Recommended corrective actions

Advanced PII Detection

spaCy NER and regex-driven PII identification for:

Emails

Phone numbers

SSNs

Credit card numbers

PHI terms

Personal identifiers

Document Processing

PDF extraction (PyPDF2, pdfplumber)

DOCX parsing (python-docx)

Automatic text cleaning

Section-level segmentation for improved accuracy

Interactive Compliance Dashboard

Overall compliance score

Framework-specific scoring

PII detection visualization

Violation summaries

Exportable Excel and JSON reports

Tech Stack
Layer	Technology
Frontend	Streamlit
Backend / AI	Python, OpenAI GPT-4o
NLP	spaCy, regex
Document Parsing	PyPDF2, pdfplumber, python-docx
Visualization	Plotly
Reporting	XlsxWriter
Environment	python-dotenv

Installation
Prerequisites

Python 3.11+

OpenAI API Key

Step 1: Clone the repository
git clone https://github.com/yourusername/ai-compliance-checker.git
cd ai-compliance-checker

Step 2: Install dependencies
pip install -r requirements.txt

Step 3: Download spaCy model
python -m spacy download en_core_web_sm

Step 4: Add your environment variables

Create a .env file:

OPENAI_API_KEY=your_api_key_here

Step 5: Run the app
streamlit run app.py

Usage
1. Configure Settings

Enter OpenAI API Key

Select frameworks (GDPR, SOC2, HIPAA, RBI)

Enable PII detection

Enable AI analysis (GPT-4o)

2. Upload Document

Supported formats: PDF, DOCX, TXT
Max size: 200MB

3. Review Compliance Insights

The system provides:

Overall compliance score

Framework-level scoring

PII entities found

Violations and risk levels

AI-generated recommendations (if enabled)

4. Export Results

Excel report

JSON data

Architecture Overview
Streamlit UI
      |
Document Processor
      |
PII Detector (spaCy + regex)
      |
Compliance Engine (rule-based scoring)
      |
GPT-4o AI Analysis Layer
      |
Report Generator (Excel/JSON)

API Reference
Compliance Checker
checker = ComplianceChecker(
    frameworks=["GDPR", "SOC2", "HIPAA", "RBI"],
    sensitivity="medium",
    include_pii=True,
    include_ai_analysis=True
)
results = checker.analyze_document(text)

PII Detector
detector = PIIDetector()
entities = detector.detect_pii(text)

Testing

Run automated tests:

pytest


Format code:

black .
isort .


Type checking:

mypy .

Roadmap

Add PCI-DSS and CCPA support

Real-time compliance scanning for emails and documents

Multi-language compliance detection

PDF export for full compliance reports

Cloud integration

Automated remediation workflows

Disclaimer

This tool provides automated compliance assistance and risk detection.
It does not constitute legal advice. Organizations must conduct independent legal and regulatory reviews.

Contributing

Fork the repository

Create a feature branch

Commit your changes

Submit a pull request

Contributions for additional frameworks, improved PII models, and performance optimizations are welcome.

License

This project is licensed under the MIT License.
