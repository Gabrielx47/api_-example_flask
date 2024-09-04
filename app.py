from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/operations", methods=["GET"])
def retornarOperacoesDisponiveis():
    return jsonify(["Soma", "subtração"])
