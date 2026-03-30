FROM python:3.10-slim
RUN pip install requests beautifulsoup4
WORKDIR /app
COPY scraper.py .
CMD ["python", "scraper.py"]
