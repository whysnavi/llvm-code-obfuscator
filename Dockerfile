FROM python:3.11-slim

# Install clang at build time (Render's own build environment — not tied to
# Streamlit Cloud's broken Debian image)
RUN apt-get update && \
    apt-get install -y --no-install-recommends clang && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Render sets $PORT dynamically; Streamlit must bind to it and to 0.0.0.0
CMD streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
