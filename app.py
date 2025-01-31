from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

BOOKS_SERVICE_URL = "http://sse-lab10-simple.gucqgnd7b7azbuax.uksouth.azurecontainer.io:5000/books"

@app.route('/', methods=['GET', 'POST'])
def search_books():
    if request.method == 'POST':
        genre = request.form.get('genre')
        response = requests.get(BOOKS_SERVICE_URL, params={'genre': genre})
        if response.status_code == 200:
            books = response.json()
            return render_template('results.html', books=books)
    return render_template('search.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
