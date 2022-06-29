from crypt import methods
from flask import Flask, make_response, render_template, request
from index import getGoodsCsv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST', 'GET'])
def download():
    csv = getGoodsCsv(request.form.get('url'))
    response = make_response(csv)
    response.headers["Content-Type"] = 'application/octet-stream'
    response.headers["Content-Disposition"] = 'attachment; filename=hello.txt'
    return response

if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')
