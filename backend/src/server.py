

from flask import Flask


app = Flask(__name__)

@app.route('/')
def get_insult():
    return 'You are a fool!'

if __name__ == '__main__':
    app.run(port=5000, debug=True)



