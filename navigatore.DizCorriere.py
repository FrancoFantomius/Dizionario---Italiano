import sqlite3
import FFMath as mt


alfabeto = []
for i in range(26):
    alfabeto.append(chr(i + ord('a')).upper())

def trova_parola(parola: str):
    conn = sqlite3.connect('dizionari.corriere.it.db')
    c = conn.cursor()
    c.execute("SELECT * FROM {} WHERE parola = ?".format(parola[0].upper()), (parola,))
    risultato = c.fetchone()
    conn.close()
    return risultato

def trova_parole(parola: str):
    conn = sqlite3.connect('dizionari.corriere.it.db')
    c = conn.cursor()
    c.execute("SELECT * FROM {} WHERE parola LIKE ?".format(parola[0].upper()), (parola + '%',))
    risultato = c.fetchall()
    conn.close()
    return risultato

def vedi_lettera(lettera: str):
    conn = sqlite3.connect('dizionari.corriere.it.db')
    c = conn.cursor()
    c.execute("SELECT * FROM {}".format(lettera))
    risultato = c.fetchall()
    conn.close()
    return risultato
