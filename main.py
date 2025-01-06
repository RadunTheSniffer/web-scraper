from flask import Flask, render_template
import sentiment
app = Flask(__name__)

@app.route('/')



@app.route('/output')
def output():
    # Scrape data
    data1 = sentiment.output
    print(data1)
    #return render_template("index.html",data=data1)
    
    
    
if __name__ == '__main__':
    app.run(debug=True)