import pyodbc
import json


#caminho arquivo json
with open(r"caminho arquivo json","r", encoding='utf-8-sig') as arq_json:
    linhas_json=json.load(arq_json)


#string para conectar ao banco de dados no sql
string_con = (
    
    #string para conectar ao banco de dados no sql
)
conexao = pyodbc.connect(string_con,autocommit=True)
print("Conectado con Suceso")
cursor = conexao.cursor()

log = []

for key, reg in linhas_json.items():
    try:
        cursor.execute(
            f"""
               # comando sql
            """
        )

    except Exception as erro:
        log.append([key, erro])
print(log)


