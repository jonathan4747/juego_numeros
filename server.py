from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "estoessecreto"

lista=[]
@app.route('/' ,methods=['GET'])
def pagina():
        session['numero']=random.randint(1, 100)
        return render_template('index.html')

@app.route('/guess',methods=['GET'])
def paginaSession():
        if int(session['num_seleccionado'])==session['numero']:
            var = "igual"
        elif int(session['num_seleccionado'])>=session['numero']:
            var = "mayor"
        else:
            var = "menor"
        return render_template('sesion.html', valor = var, numero=int(session['num_seleccionado']))


@app.route('/num', methods=['POST'])
def generoMumero():
   session['num_seleccionado'] = request.form["num_seleccionado"]
   print(session['num_seleccionado'])
   return redirect('/guess')


@app.route('/salir', methods=['GET'])
def Salir():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run( debug = True )