from flask import Flask, request, redirect, url_for, render_template
import converter

app = Flask(__name__)

@app.route('/') 
def my_Form():
    return render_template('main.html')

@app.route('/', methods=['POST'])
def my_form_post():
    userNum = request.form['userNum']
    bitSize = request.form['bitSize']
    if userNum == '':
        userNum = 0
    output = converter.IEEE754(float(userNum),int(bitSize))
    return render_template('main.html', out=output, num=userNum)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)