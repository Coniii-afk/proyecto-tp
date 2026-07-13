from flask import Flask, render_template


app = Flask(__name__)


app.config["SECRET_KEY"] = "findpets123"

@app.route("/")
def inicio():
 return render_template("index.html")

@app.route("/iniciosesion")
def iniciosesion():
 return render_template("iniciosesion.html")

@app.route("/registrate")
def registrate():
 return render_template("registrate.html")

@app.route("/buscarporcodigo")
def buscarporcodigo():
 return render_template("buscarporcodigo.html")

@app.route("/formulariomascota")
def formulariomascota():
 return render_template("formulariomascota.html")

@app.route("/murocomunitario")
def murocomunitario():
 return render_template("murocomunitario.html")

@app.route("/paneldelusuario")
def paneldelusuario():
 return render_template("paneldelusuario.html")

@app.route("/paneladministrador")
def paneladministrador():
 return render_template("paneladministrador.html")

if __name__ == "__main__":
    app.run(debug=True)