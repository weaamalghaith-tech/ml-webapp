FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy all files to the container
COPY . /app

RUN pip install "streamlit<1.51" numpy scikit-learn

CMD ["streamlit", "run", "app_streamlit.py", "--server.port=80", "--server.address=0.0.0.0"]