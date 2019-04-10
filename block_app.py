from flask import Flask, render_template, request, jsonify, url_for
from searcher import phraser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check')
def check():
    search_term = request.args.get('search_term')
    search = phraser(search_term)
    print(search)
    return jsonify(result=search[0], blocks=search[1])

if __name__ == '__main__':
    app.run(debug=True)
