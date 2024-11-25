from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from

app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'Calculator',
    'openapi': '3.0.0'
}

swagger = Swagger(app, template_file="docs/openapi.yaml")

@app.route("/operations", methods=["GET"])
def retornarOperacoesDisponiveis_get():
    return jsonify(["Adição", "subtração", "Divisão", "Multiplicação"])

@app.route("/operations/addition", methods=["POST"])
def somar_post():
    return jsonify(int(request.form["valor1"]) + int(request.form["valor2"]))

@app.post("/operations/subtraction")
def subtrair_post():
    return jsonify(int(request.form["valor1"]) - int(request.form["valor2"]))

@app.post("/operations/multiplication")
def multiplicar_post():
    return jsonify(int(request.form["valor1"]) * int(request.form["valor2"]))

@app.post("/operations/division")
def dividir_post():
    return jsonify(int(request.form["valor1"]) / int(request.form["valor2"]))