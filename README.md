# Crawl4AI Web Interface

A web interface for the Crawl4AI library that allows users to crawl websites and get markdown output.

## Features

- Input multiple URLs for crawling
- Automatic protocol (http/https) handling
- Clean, modern UI
- Copy-to-clipboard functionality
- Async processing for better performance

## Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5002`

## Deployment

This application is configured for deployment on Render.com. The `render.yaml` file contains the necessary configuration.
