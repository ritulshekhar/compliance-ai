import streamlit as st
import pandas as pd
import plotly.express as px
from document_processor import DocumentProcessor
from compliance_checker import ComplianceChecker
from report_generator import ReportGenerator
from utils import clean_text, CUSTOM_CSS

# Page Configuration
st.set_page_config(
    page_title="ComplianceAI - Enterprise Checker",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply Custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/9322/9322127.png", width=50) # Placeholder Icon
    st.title("Settings")
    
    api_key = st.text_input("OpenAI API Key", type="password", help="Required for AI Analysis")
    
    st.subheader("Frameworks")
    frameworks = {
        "GDPR": st.checkbox("GDPR", value=True),
        "SOC2": st.checkbox("SOC2", value=True),
        "HIPAA": st.checkbox("HIPAA", value=False),
        "RBI": st.checkbox("RBI", value=False)
    }
    selected_frameworks = [k for k, v in frameworks.items() if v]
    
    st.subheader("Analysis Options")
    include_pii = st.toggle("Detect PII", value=True)
    include_ai = st.toggle("AI Analysis (GPT-4o)", value=True)

# Main Content
st.markdown('<div class="main-header">🛡️ Generic Compliance Checker</div>', unsafe_allow_html=True)
st.markdown("### Intelligent Regulatory Compliance & Risk Assessment")

# File Upload
uploaded_file = st.file_uploader("Upload Document (PDF, DOCX, TXT)", type=['pdf', 'docx', 'txt'])

if uploaded_file:
    # Processing
    with st.spinner("Processing Document..."):
        file_ext = uploaded_file.name.split('.')[-1]
        processor = DocumentProcessor()
        text_content = processor.extract_text(uploaded_file, file_ext)
        clean_content = clean_text(text_content)
    
    if clean_content:
        st.success("Document processed successfully!")
        
        # Analyze Button
        if st.button("Run Compliance Analysis", type="primary"):
            with st.spinner("Analyzing Compliance Risks..."):
                checker = ComplianceChecker(
                    api_key=api_key if api_key else None,
                    frameworks=selected_frameworks,
                    include_pii=include_pii,
                    include_ai_analysis=include_ai and api_key
                )
                results = checker.analyze_document(clean_content)
                
                # --- DASHBOARD ---
                st.markdown("---")
                
                # Top Metrics
                col1, col2, col3 = st.columns(3)
                with col1:
                    avg_score = sum(results['compliance_scores'].values()) / len(results['compliance_scores']) if results['compliance_scores'] else 0
                    st.metric("Overall Compliance Score", f"{avg_score:.1f}%", delta=f"{avg_score-80:.1f}%")
                
                with col2:
                    st.metric("Violations Detected", len(results.get('violations', [])), delta=-len(results.get('violations', [])), delta_color="inverse")
                    
                with col3:
                    st.metric("PII Entities Found", len(results.get('pii_detected', [])), delta=-len(results.get('pii_detected', [])), delta_color="inverse")

                # Charts & Details
                col_chart, col_details = st.columns([1, 1])
                
                with col_chart:
                    st.subheader("Framework Usage Scores")
                    df_scores = pd.DataFrame(list(results['compliance_scores'].items()), columns=['Framework', 'Score'])
                    fig = px.bar(df_scores, x='Framework', y='Score', color='Score', range_y=[0, 100], template='plotly_dark')
                    st.plotly_chart(fig, use_container_width=True)

                    if include_pii and results['pii_detected']:
                        st.subheader("PII Distribution")
                        pii_counts = pd.DataFrame(results['pii_detected'])['label'].value_counts()
                        fig_pii = px.pie(values=pii_counts.values, names=pii_counts.index, title="Detected PII Types", template='plotly_dark')
                        st.plotly_chart(fig_pii, use_container_width=True)

                with col_details:
                    st.subheader("AI Insights")
                    st.info(results.get('ai_insights', "No AI analysis available."))
                    
                    st.subheader("Key Violations")
                    if results.get('violations'):
                        for v in results['violations']:
                            st.warning(f"**{v['framework']}**: {v['issue']} ({v['severity']})")
                    else:
                        st.success("No potential violations detected via heuristics.")

                # Exports
                st.markdown("---")
                st.subheader("Export Report")
                gen = ReportGenerator()
                
                col_ex1, col_ex2 = st.columns(2)
                with col_ex1:
                    excel_data = gen.generate_excel_report(results)
                    st.download_button("Download Excel Report", excel_data, file_name="compliance_report.xlsx")
                with col_ex2:
                    json_data = gen.generate_json_report(results)
                    st.download_button("Download JSON Data", json_data, file_name="compliance_report.json")

    else:
        st.error("Could not extract text from the document.")

else:
    st.info("Please upload a document to begin analysis.")
