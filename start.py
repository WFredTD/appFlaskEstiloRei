from flask import Flask, render_template, request, redirect, session, url_for, flash
from usuario import Usuario
app = Flask (__name__)

app.secret_key = 'supersecretkey'

usuario1 = Usuario('rafael.gimenez@gmail.com', 'JaRafael', 'JavaScript')
usuario2 = Usuario('romulo.silvestre@gmail.com', 'SilverRon', 'Sistema_S')
usuario3 = Usuario('suzane.hospital@gmail.com', 'MarZu', 'Santa_SUS')

usuarios = { usuario1.email : usuario1,
            usuario2.email: usuario2,
            usuario3.email : usuario3 }

@app.route('/')
def iniciar():
    return render_template ('index.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['email'] in usuarios:
        usuario = usuarios [request.form['email']]
        if request.form['senha'] == usuario.password:
            session['nickname_logado'] = usuario.nickname
            return redirect('agenda')
        else:
            return redirect ('/')

@app.route('/logout')
def logout():
    session.pop('usuario_logado', None)
    return redirect (url_for('iniciar'))

@app.route('/cadastrarBarbeiro')
def cadastrarBarbeiro():
    return 'cadastrar barbeiro'

@app.route('/cadastrarCliente')
def cadastrarCliente():
    return render_template ('cadastrarCliente.html')

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

@app.route('/agenda', methods=['GET', 'POST'])
def agenda():
    if 'nickname_logado' in session:
        nickname_logado = session.get('nickname_logado')
        return render_template ('agenda.html', nickname_logado = nickname_logado)
    else:
        return redirect ('index')

@app.route('/listaServico')
def listaServico():
    return ('lista de serviços')


app.run(debug=True)
