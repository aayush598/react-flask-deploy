from flask import Flask, send_from_directory
app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')

@app.route('/')
def hello():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)