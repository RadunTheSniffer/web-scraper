from flask import Flask, render_template, request, jsonify
import sentiment
app = Flask(__name__)


@app.route('/scrape', methods=['POST'])
def scraper():
    link = request.get(link)
    data = request.json
    link = data.get('link')
    result = sentiment.analyze(link)
    return jsonify(result) 
    
if __name__ == '__main__':
    app.run(debug=True)