from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    erros = []
    distancia_dia = ''
    dias_semana = ''
    meio_transporte = ''

    if request.method == 'POST':
        distancia_dia = request.form.get('distancia_dia', '').strip()
        dias_semana = request.form.get('dias_semana', '').strip()
        meio_transporte = request.form.get('meio_transporte', '')

        distancia_valida = None
        if not distancia_dia:
            erros.append('A distância percorrida por dia é obrigatória.')
        else:
            try:
                distancia_valida = float(distancia_dia)
                if distancia_valida <= 0:
                    erros.append('A distância deve ser maior que 0.')
                    distancia_valida = None
            except ValueError:
                erros.append('Digite um número válido para a distância.')

        dias_validos = None
        if not dias_semana:
            erros.append('Os dias de deslocamento por semana são obrigatórios.')
        else:
            try:
                dias_validos = int(dias_semana)
                if dias_validos < 1 or dias_validos > 7:
                    erros.append('Os dias por semana devem estar entre 1 e 7.')
                    dias_validos = None
            except ValueError:
                erros.append('Digite um número inteiro válido para os dias por semana.')

        if not meio_transporte:
            erros.append('Selecione o meio de transporte.')

    return render_template('index.html', erros=erros, distancia_dia=distancia_dia,
                           dias_semana=dias_semana, meio_transporte=meio_transporte)










if __name__ == '__main__':
    app.run(debug=True)