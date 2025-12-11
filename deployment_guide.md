# Deployment Guide

## Issue with Vercel
You are seeing a `404: NOT_FOUND` error because **Vercel is designed for static and serverless web apps** (like Next.js, React), but **Streamlit requires a continuously running Python server** to handle its interactive features and WebSockets. Vercel's serverless functions shut down after a few seconds, which kills Streamlit.

## Recommended Solution: Streamlit Community Cloud (Free & Easiest)
This is the official platform for hosting Streamlit apps. behavior is native and stable.

1.  **Push your code to GitHub**:
    Ensure your `requirements.txt` is in the root folder (it already is).
2.  **Go to [share.streamlit.io](https://share.streamlit.io/)**.
3.  **Click "New App"**.
4.  **Select your Repository**, Branch (`main`), and Main File Path (`app.py`).
5.  **Click "Deploy"**.
    *   *Note: You may need to add your `OPENAI_API_KEY` in the App Settings > Secrets section on Streamlit Cloud.*

## Alternative: Render (If you need a custom server)
1.  Create a `requirements.txt` (Done).
2.  Create a new Web Service on [Render](https://render.com/).
3.  Connect your GitHub repo.
4.  Use the following **Start Command**:
    ```bash
    streamlit run app.py --server.port $PORT --server.address 0.0.0.0
    ```
5.  Render will automatically detect Python and install dependencies.
