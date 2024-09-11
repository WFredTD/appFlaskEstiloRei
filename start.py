from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def iniciar():
    return 'inicio'

@app.route('/login')
def login():
    return 'login'

@app.route('/logout')
def logout():
    return 'logout'

@app.route('/cadastrarBarbeiro')
def cadastrarBarbeiro():
    return 'cadastrar barbeiro'

@app.route('/cadastrarCliente')
def cadastrarCliente():
    return 'cadastrar cliente'

@app.route('/cadastrarAgendamento')
def cadastrarAgendamento():
    return 'cadastrar agendamento'

@app.route('/cadastroServico')
def cadastrarServico():
    return 'cadastrar serviço'

@app.route('/listaBarbeiros')
def listaBarbeiros():
    return 'lista de barbeiros'

@app.route('/listaClientes')
def listaClientes():
    return 'lista de clientes'

@app.route('/agenda')
def agenda():
    return 'agenda'

@app.route('/listaServico')
def listaServico():
    return ('lista de serviços')


app.run(debug=True)