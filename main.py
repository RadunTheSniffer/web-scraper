from flask import Flask, render_template
import extractor
app = Flask(__name__)

@app.route('/')



@app.route('/output')
def output():
    # Scrape data
    data = extractor.scraped_data
    return render_template("index.html",data=data)
    
    
    
if __name__ == '__main__':
    app.run(debug=True)