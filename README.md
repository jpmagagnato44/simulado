 
Calculadora de Pegada de Carbono do Deslocamento

Simulado — Aulas 1 a 4 
Fatec Jahu — 2º Semestre/2026

*João Paulo e Vinicius
**Tema escolhido:** Tema A — Calculadora de Pegada de Carbono do Deslocamento

## O que o projeto faz

A aplicação recebe, por um formulário na rota `/`, a distância percorrida por dia, os dias de deslocamento por semana e o meio de transporte usado. A partir disso, calcula a emissão mensal estimada de CO₂ e classifica o resultado em uma das quatro faixas de impacto (Baixo, Moderado, Alto, Crítico).

Como executar o projeto


git clone https://github.com/jpmagagnato44/simulado.git
cd simulado

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python app.py


Depois, acesse **http://127.0.0.1:5000** no navegador.

## Por que o formulário deu erro 405 na Etapa 2?

O `<form>` já enviava os dados com `method="post"`, mas a rota `/` só aceitava `GET` (o padrão do Flask quando nenhum `methods` é informado). Como o método da requisição (POST) não batia com o método aceito pela rota, o Flask devolveu **405 Method Not Allowed**. Resolvido na Etapa 3, declarando `methods=['GET', 'POST']` na rota.

## Resultados obtidos nos testes

### Testes válidos

| # | Distância/dia | Dias/semana | Meio de transporte | Km/mês | Emissão mensal | Faixa obtida |

| 1 | 10 | 5 | Bicicleta ou a pé | 200,00 | 0,00 kg | Baixo impacto |
| 2 | 30 | 5 | Ônibus | 600,00 | 42,00 kg | Impacto moderado |
| 3 | 25 | 5 | Carro a gasolina | 500,00 | 100,00 kg | Alto impacto |
| 4 | 40 | 6 | Carro a gasolina | 960,00 | 192,00 kg | Impacto crítico |
| 5 | 50 | 7 | Carro elétrico | 1400,00 | 70,00 kg | Alto impacto |

### Testes inválidos

| # | Situação | Resultado |

| 6 | Distância 0 (ou negativa) | Erro: "A distância deve ser maior que 0." |
| 7 | Dias por semana 8 | Erro: "Os dias por semana devem estar entre 1 e 7." |
| 8 | Nenhum meio de transporte selecionado | Erro: "Selecione o meio de transporte." |
| 9 | Todos os campos vazios | Os três erros de campo obrigatório aparecem juntos |

Em nenhum dos casos inválidos a aplicação retornou erro 500.