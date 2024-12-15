from flask import Flask, jsonify, request
from flasgger import Swagger
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'Calculator',
    'openapi': '3.0.0'
}
CORS(app)

swagger = Swagger(app, template_file="docs/openapi.yaml")

@app.route("/operations", methods=["GET"])
def retornarOperacoesDisponiveis_get():
    return jsonify(["Adição", "subtração", "Divisão", "Multiplicação"])

@app.route("/operations/addition", methods=["POST"])
@cross_origin()
def somar_post():
    return jsonify(int(request.json["valor1"]) + int(request.json["valor2"]))

@app.post("/operations/subtraction")
def subtrair_post():
    return jsonify(int(request.json["valor1"]) - int(request.json["valor2"]))

@app.post("/operations/multiplication")
def multiplicar_post():
    return jsonify(int(request.json["valor1"]) * int(request.json["valor2"]))

@app.post("/operations/division")
def dividir_post():
    return jsonify(int(request.json["valor1"]) / int(request.json["valor2"]))