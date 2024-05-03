from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html', imc="")

@app.route('/imc', methods=['POST'])
def imc():
    altura = float(request.form['altura'])
    peso = float(request.form['peso'])
    imc = round( peso / ((altura/100) * (altura/100)), 1)
    if imc < 16.9:
        tabela = 'Muito Abaixo do Peso'
    elif 17 <= imc <= 18.4:
        tabela = 'Baixo Peso'
    elif 18.5 <= imc <= 24.9:
        tabela = 'Peso Normal'
    elif 25 <= imc <= 29.9:
        tabela = 'Sobrepeso'
    elif 30 <= imc <= 34.9:
        tabela = 'Obesidade Grau 1'
    elif 35 <= imc <= 39.9:
        tabela = 'Obesidade Grau 2'
    elif imc > 40:
        tabela = 'Obesidade Grau 3'
    return render_template('calculadora.html', imc=f'O seu IMC: {imc}, sua classificação: {tabela}')

if __name__ == '__main__':
    app.run(debug=True)