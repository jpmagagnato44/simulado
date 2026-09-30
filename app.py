from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    if request.method == 'POST':
        distancia_dia = request.form.get('distancia_dia')
        dias_semana = request.form.get('dias_semana')
        meio_transporte = request.form.get('meio_transporte')
        print(distancia_dia, dias_semana, meio_transporte)

    return render_template('index.html')













if __name__ == '__main__':
    app.run(debug=True)