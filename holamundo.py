from flask import Flask, request, url_for, redirect, abort, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return 'hola mundo'

@app.route('/post/<post_id>', methods=['GET', 'POST'])
def lala(post_id):
   if request.method == 'GET':
      return 'El id del post es: ' + post_id
   else:
      return 'Este es otro metodo y no GET'

@app.route('/lele', methods=['POST', 'GET'])
def lele():
   return {
      "username": 'Lo que sea',
      "email":  'loquesea@correo.com'
   }

@app.route('/home', methods=['GET'])
def home():
   return render_template('home.html', mensaje='Hola Mundo')
