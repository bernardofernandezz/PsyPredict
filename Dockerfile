# Dockerfile for Mental Health Prediction Project
FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose ports for Jupyter, Streamlit, and FastAPI
EXPOSE 8888 8501 8000

# Default command: open bash (user can choose service)
CMD ["/bin/bash"]

# ---
# To run Jupyter:
# docker run -p 8888:8888 <image> jupyter notebook --ip=0.0.0.0 --allow-root --no-browser
# To run Streamlit:
# docker run -p 8501:8501 <image> streamlit run app_streamlit.py
# To run FastAPI:
# docker run -p 8000:8000 <image> uvicorn api.app:app --host 0.0.0.0 --reload
