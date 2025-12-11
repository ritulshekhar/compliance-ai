import hashlib
import re

def clean_text(text: str) -> str:
    """Cleans text by removing extra whitespace and special characters."""
    if not text:
        return ""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def generate_file_hash(file_content: bytes) -> str:
    """Generates a SHA-256 hash of the file content."""
    return hashlib.sha256(file_content).hexdigest()

def format_currency(amount: float) -> str:
    """Formats a number as currency."""
    return "${:,.2f}".format(amount)

# Custom CSS for the "Premium" look
CUSTOM_CSS = """
<style>
    .stApp {
        background-color: #0E1117;
    }
    .main-header {
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        color: #FFFFFF;
        font-size: 2.5rem;
        margin-bottom: 1rem;
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .card {
        background-color: #262730;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        border: 1px solid #333;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #4facfe;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #b0b0b0;
    }
    div[data-testid="stExpander"] {
        border: 1px solid #333;
        border-radius: 10px;
        background-color: #1E1E1E;
    }
</style>
"""
