# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install Graphviz system package and other dependencies
RUN apt-get update && apt-get install -y graphviz && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Set the default command
CMD ["python", "main.py"]
