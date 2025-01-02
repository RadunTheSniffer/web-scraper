from flask import Flask, render_template_string
import extractor
app = Flask(__name__)

@app.route('/')
def home():
    # Scrape data
    data = extractor.scraped_data
    print(f"Scraped Data: {data[:100]}...")
    
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Scraper Output</title>
    </head>
    <body>
        <h1>Scraper Output</h1>
        <pre>{data}</pre>  <!-- Data output -->
    </body>
    </html>
    '''
    
    return render_template_string(html_content, data=data)


if __name__ == '__main__':
    app.run(debug=True)