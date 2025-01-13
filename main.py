from flask import Flask, render_template, request, jsonify
import sentiment
import classification
import extractor

app = Flask(__name__)

def preprocess_data(link):
    # Add your data cleaning and preprocessing steps here
    cleaned_data = extractor.scrape_data(link)
    return cleaned_data

@app.route('/scraper', methods=['POST'])
def scraper():
    data = request.get_json()
    link = data.get('link')
    
    # Preprocess the data
    cleaned_data = extractor.scrape_data(link)
    
    # Classification
    classify = classification.filter_redundant_texts(cleaned_data)
    
    # Sentiment Analysis
    result = sentiment.analyze(classify)
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
