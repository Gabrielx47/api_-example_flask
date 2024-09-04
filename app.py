from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/operations")
def retornarOperacoesDisponiveis():
    return jsonify(["Soma", "subtração", "Divisão", "Multiplicação"])
