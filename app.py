from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/operations")
def retornarOperacoesDisponiveis_get():
    return jsonify(["Adição", "subtração", "Divisão", "Multiplicação"])


@app.post("/operations/addition")
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