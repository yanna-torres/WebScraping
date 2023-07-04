import requests
from bs4 import BeautifulSoup
import re
import psycopg2
from Filme import Filme
import sqlite3 as sql

def inserir(filme):
    sucesso = False
    dbname = './database/top250filmesimdb.db'
    try:
        connection = sql.connect(dbname)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO filme (titulo, ano, avaliacao, classificacao) VALUES ('{}','{}','{}','{}')".format(filme.titulo, filme.ano, filme.avaliacao, filme.classificacao))
        connection.commit()
        if cursor.rowcount == 1:
            sucesso = True

    except (Exception, sql.Error) as error:
        sucesso = False
    finally:
        if connection:
            cursor.close()
            connection.close()
    return sucesso


def main():
    url = "https://www.imdb.com/chart/top"

    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML , like Gecko) Chrome/83.0.4103.61 Safari/537.36" }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    filmes = soup.select('td.titleColumn')
    avaliacoes = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]

    resultado = []

    for i in range(0, len(filmes)):
        filme_string = filmes[i].get_text()
        filme = (' '.join(filme_string.split()).replace('.', ''))
        filme_titulo = filme[len(str(i))+1:-7]
        ano = re.search('\((.*?)\)', filme_string).group(1)
        classificacao = filme[:len(str(i)) - (len(filme))]

        f = Filme()
        f.titulo = filme_titulo
        f.ano = ano
        f.avaliacao = float(avaliacoes[i])
        f.classificacao = classificacao

        resultado.append(f)

    for f in resultado:
        print("{} - {} - {} - {}".format(f.titulo, f.ano, f.avaliacao, f.classificacao))
        print(inserir(f))


if __name__ == "__main__":
    main()
