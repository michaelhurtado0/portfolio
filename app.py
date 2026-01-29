# -*- coding: utf-8 -*-
"""
Created on Sun May 18 01:52:23 2025

@author: micha
"""

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello, Flask from Spyder!"

# # if __name__ == '__main__':
# #     app.run(debug=True)
# if __name__ == '__main__':
#     app.run(debug=True, use_reloader=False)

#######

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index2.html')  # This will look for templates/index.html

# if __name__ == '__main__':
#     app.run(debug=True, use_reloader=False)
    
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    my_projects = [
        {
            "title": "C/C++", 
            "category": "Bluetooth car controller", 
            "img": "c_logo.png" # The filename must match your folder!
        }
    ]
    return render_template('index.html', projects=my_projects)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)