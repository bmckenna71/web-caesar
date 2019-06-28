from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action = "/" method = "post">
            <label for = "rotate-by"> 
                Rotate by: 
                <input id = "rot" type="text" name = "q" value ="0"/> 
            </label>
            <textarea name = "text">{0}</textarea>
            <input type = "submit" value="Submit Query" />
    
      </form>
      
    </body>
</html> 
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['q']
    text = request.form['text']
    cipher = rotate_string(text,int(rot))
    return form.format(cipher)

app.run()