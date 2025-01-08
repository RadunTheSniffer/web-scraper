from flask import Flask, render_template, request, jsonify
import sentiment
app = Flask(__name__)


@app.route('/scraper', methods=['POST'])
def scraper():
    data = request.get_json()
    link = data.get('link')
    result = sentiment.analyze(link)
    return jsonify(result) 
    
if __name__ == '__main__':
    app.run(debug=True)