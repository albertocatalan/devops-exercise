# Use a slim Python image for efficient deployment and scaling, supporting best practices in DevOps culture.
FROM python:3.9-slim

# Set working directory to ensure consistency across environments, promoting good DevOps practices in deployment.
WORKDIR /app

# Copy app.py and requirements.txt. This includes logic to count POST requests and return on GET requests.
COPY app.py requirement.txt /app/

# Install dependencies without cache to ensure up-to-date versions and reduce image size.
# This prevents outdated dependencies that could affect the POST request counter functionality.
RUN pip install --no-cache-dir -r requirement.txt

# Expose port 5000 for external access, essential for deployment, monitoring, and scaling the application.
EXPOSE 5000

# Start the Flask app, enabling it to handle POST and GET requests, scale, and be monitored easily.
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

