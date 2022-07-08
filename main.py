import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

#construir as funcionalidades
@app.route('/')
def homepage():
  return 'A API está no ar'

@app.route('/pegarvendas')
def pegarvendas():
  tabela = pd.read_csv('adv.csv')
  total_vendas = tabela['Vendas'].sum()
  resposta = {'total_vendas': total_vendas}
  return jsonify(resposta)

  
#rodar a api
app.run(host='0.0.0.0')

#tabela = pd.read_csv('adv.csv')
#total_vendas = tabela['Vendas'].sum()
#print(total_vendas)