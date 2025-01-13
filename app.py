from quart import Quart, render_template, request, jsonify
import asyncio
from crawl4ai import AsyncWebCrawler
import os

app = Quart(__name__)
app.config['PROVIDE_AUTOMATIC_OPTIONS'] = True

async def crawl_urls(urls):
    try:
        results = []
        async with AsyncWebCrawler() as crawler:
            for url in urls:
                try:
                    # Ensure URL starts with http:// or https://
                    if not url.startswith(('http://', 'https://')):
                        url = 'https://' + url
                    result = await crawler.arun(url=url)
                    results.append({"url": url, "markdown": result.markdown})
                except Exception as e:
                    results.append({"url": url, "error": str(e)})
        return results
    except Exception as e:
        return {"error": str(e)}

@app.route('/')
async def home():
    return await render_template('index.html')

@app.route('/crawl', methods=['POST'])
async def crawl():
    try:
        data = await request.get_json()
        urls = data.get('urls', [])
        if isinstance(urls, str):
            urls = [urls]
        if not urls:
            return jsonify({"error": "No URLs provided"}), 400
        results = await crawl_urls(urls)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
