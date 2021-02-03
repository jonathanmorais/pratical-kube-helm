import math
from flask import Flask
from flask import request, jsonify
import json
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return 'OK'

@app.route('/pow', methods = ['POST'])
def potencia():
    if request.method == 'POST':
        data = request.json
        res = math.pow(int(data['base']), int(data['exp']))
        digitos = 0    

        print('resultado: %s \t digitos: %s' % (res, digitos))

        return str(res)
    else:
        print("Metodo incorreto")
        return   

app.run(debug=True)
