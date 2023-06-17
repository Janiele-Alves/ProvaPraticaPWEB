from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista de times
times = []

# Rota principal - exibe a lista de times cadastrados

@app.route('/exibir')
def index():
    return render_template('index.html', times=times)

@app.route('/')
def home():
    return render_template('inicio.html')


# Rota para adicionar um novo time
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nome = request.form['nome']
        treinador = request.form['treinador']
        classificacao = request.form['classificacao']
        time = {'id': len(times), 'nome': nome, 'treinador': treinador, 'classificacao': classificacao}
        times.append(time)
        return redirect('/exibir')
    return render_template('cadastrarTime.html')

# Rota para editar um time
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    time = next((time for time in times if time['id'] == id), None)
    if time:
        if request.method == 'POST':
            time['nome'] = request.form['nome']
            time['treinador'] = request.form['treinador']
            time['classificacao'] = request.form['classificacao']
            return redirect('/exibir')
        return render_template('editarTime.html', time=time)
    return "time não encontrado."

# Rota para excluir um time
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    del times[id]
    return redirect('/exibir')

if __name__ == '__main__':
    app.run()
