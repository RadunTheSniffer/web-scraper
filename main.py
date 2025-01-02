from flask import Flask, render_template_string
import extractor
app = Flask(__name__)

@app.route('/')
def home():
    # Scrape data
    data = extractor.scraped_data()
    
    
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
        <p>{data}</p>  <!-- Data output -->
    </body>
    </html>
    '''
    
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)