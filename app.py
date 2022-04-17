from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/predict',methods=['POST'])

if __name__ == "__main__":
    app.run(debug=True)
