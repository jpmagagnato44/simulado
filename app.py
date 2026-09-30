from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    erros = []
    resultado = None
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


        resultado = None

        if not erros:
            if meio_transporte == 'bicicleta':
                fator = 0.00
            elif meio_transporte == 'eletrico':
                fator = 0.05
            elif meio_transporte == 'onibus':
                fator = 0.07
            elif meio_transporte == 'moto':
                fator = 0.10
            else:  # 'gasolina'
                fator = 0.20

            km_mes = distancia_valida * dias_validos * 4
            emissao_mensal = km_mes * fator

            resultado = {
                'km_mes': km_mes,
                'emissao_mensal': emissao_mensal,
            }
    return render_template('index.html', erros=erros, resultado=resultado, distancia_dia=distancia_dia,
                           dias_semana=dias_semana, meio_transporte=meio_transporte)










if __name__ == '__main__':
    app.run(debug=True)