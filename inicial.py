#!/usr/bin/env python
# coding: utf-8

# # Python Insights - Analisando Dados com Python
#
# ### Case - Cancelamento de Clientes
#
# Você foi contratado por uma empresa com mais de 800 mil clientes para um projeto de Dados. Recentemente a empresa percebeu que da sua base total de clientes, a maioria são clientes inativos, ou seja, que já cancelaram o serviço.
#
# Precisando melhorar seus resultados ela quer conseguir entender os principais motivos desses cancelamentos e quais as ações mais eficientes para reduzir esse número.
#
# Base de dados e arquivos: https://drive.google.com/drive/folders/1uDesZePdkhiraJmiyeZ-w5tfc8XsNYFZ?usp=drive_link

# In[1]:


# passo a passo do seu projeto
# passo 1: importar a base de dados

import plotly.express as px
import pandas

tabela = pandas.read_csv("cancelamentos.csv")
# passo 2: visualizar a base de dados
# informacao que nao te ajuda, te atrapalha
# limha -> axis = 0
# coluna -> axis = 1

tabela = tabela.drop("CustomerID", axis=1)
display(tabela)


# In[2]:


# passo 3: tratamentos de erros (resolver as cagadas da base de dados)
# display(tabela.info())
# tratar valores vazios
tabela = tabela.dropna()
display(tabela.info())


# In[3]:


# passo 4: análise inicial dos dados (entender como estao os cancelamentos)
display(tabela["cancelou"].value_counts())
display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))


# In[4]:


display(tabela["duracao_contrato"].value_counts())
display(tabela["duracao_contrato"].value_counts(
    normalize=True).map("{:.1%}".format))


# In[5]:


# contrato do mensal sempre cancela
tabela = tabela[tabela["duracao_contrato"] != "Monthly"]
# vamos ve o cancelamento tirando os caras do mensal
display(tabela["duracao_contrato"].value_counts())
display(tabela["duracao_contrato"].value_counts(
    normalize=True).map("{:.1%}".format))


# In[6]:


# passo 5: análise profunda da base de dados (encontrando a causa dos cancelamentos)
# informacao para que o grafico funcione: 1 tabela da base de tados, 2

grafico = px.histogram(tabela, x="duracao_contrato")
grafico.show()
