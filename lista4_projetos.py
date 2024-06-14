import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
    page_title="App Lucas&Paola",
    page_icon="👾",
)

st.header("Lista de Exercícios 4") 
st.subheader("Seja bem-vindo a apresentação dos Projetos!")

"---"

st.write('Os dados se referem aos valores futuros previstos para receita mensal de 5 projetos diferentes. A análise dos dados permitirá a decisão sobre o investitmento em um ou mais alternativas de projetos. Neste cenário, os dados futuros se referem ao período de 2022 e 2023, logo, a data referência da análise é de dezembro/2021')

code = '''
arquivo = "https://raw.githubusercontent.com/paolaribeiroq/ListaExercicios4/main/projetos-1.csv" 
df = pd.read_csv(arquivo, sep=';') 
st.dataframe(df.head(23))
'''
st.code(code, language='python')

if st.checkbox('Mostrar dataframe'):
    
    st.dataframe(df) 

arquivo = "https://raw.githubusercontent.com/paolaribeiroq/ListaExercicios4/main/projetos-1.csv" 
df = pd.read_csv(arquivo, sep=';') 
st.dataframe(df.head(23))

"---"

st.write('''O dataframe foi atualizado adicionando mais uma linha ao final com os dados referentes ao mês de dezembro de 2023. 

mes | ano | Projeto1 | Projeto2 | Projeto3 | Projeto4 | Projeto5
--- | --- | -------- | -------- | -------- | -------- | --------
 12 | 2023| 29376    | 40392    | 63648    | 29376    | 25704


obs: a partir deste ponto, utilize a df atualizada, agora com 24 meses de dados''')

code = '''
df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])
st.write(df)
'''

st.code(code, language='python')

df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])
st.write(df)

"---"

st.write('Apresentação da soma dos valores de cada projeto agrupado por ano')

code = '''
st.write(df.groupby('ano').sum())
'''
st.code(code, language='python')

st.write(df.groupby('ano').sum())

if st.checkbox('Mostrar dataframe'):
    
    st.dataframe(df) 

"---"

st.write("Geração do gráfico de dispersão cruzando os dados do `Projeto1` e `Projeto2`, com marcadores verdes e em formato de estrela")

code = '''
fig, ax = plt.subplots()
df.plot(kind = 'scatter', x = 'Projeto1', y = 'Projeto2', color='darkgreen', marker='*', ax=ax)
st.pyplot(fig)
'''
st.code(code, language='python')

fig, ax = plt.subplots()
df.plot(kind = 'scatter', x = 'Projeto1', y = 'Projeto2', color='darkgreen', marker='*', ax=ax)
st.pyplot(fig)

"---"  

st.write('''Gráfico do tipo histograma com os dados do Projeto 1 e Projeto4

Dica: Ao criar dois histograma em sequência, o python agrupa em apenas um desenho''')

code = '''
fig, ax = plt.subplots()
df["Projeto1"].plot(kind='hist', ax=ax)

df["Projeto4"].plot(kind='hist', ax=ax)
st.pyplot(fig)
'''
st.code(code, language='python')

fig, ax = plt.subplots()
df["Projeto1"].plot(kind='hist', ax=ax)

df["Projeto4"].plot(kind='hist', ax=ax)
st.pyplot(fig)
