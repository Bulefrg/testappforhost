from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Привет, мир! Это базовая программа на Flask.'

if __name__ == '__main__':
    app.run(debug=True)
