import requests
import sqlite3
from bs4 import BeautifulSoup
import FFMath as mt

alfabeto = []
for i in range(26):
    alfabeto.append(chr(i + ord('a')).upper())

inizio = "https://dizionari.corriere.it/dizionario_sinonimi_contrari/"
fine = ".shtml"

n = 0


def reset_db():
    conn = sqlite3.connect('dizionari.corriere.it.db')
    c = conn.cursor()
    for lettera in alfabeto:
        c.execute("""CREATE TABLE IF NOT EXISTS {} (
                    id TEXT PRIMARY KEY,
                    parola TEXT,
                    tipo TEXT,
                    genere TEXT,
                    aggiuntivo TEXT,
                    link TEXT)""".format(lettera))
        conn.commit()
    conn.close()


def aggiungi_parola(n, parola, tipo, genere, aggiuntivo, link):
    id = mt.to36(n)
    conn = sqlite3.connect('dizionari.corriere.it.db')
    c = conn.cursor()
    c.execute("""INSERT INTO {} (
                id, parola, tipo, genere, aggiuntivo, link) 
                VALUES (?, ?, ?, ?, ?, ?)""".format(parola[0].upper()), (id, parola, tipo, genere, aggiuntivo, link))
    conn.commit()
    conn.close()


def conosci(stringa: str, diz: list = None):
    if diz is None:
        diz = {'tipo': ["agg.",
                        "aggettivo ",
                        "art.",
                        "articolo ",
                        "avv.",
                        "avverbio ",
                        "cong.",
                        "congiunzione ",
                        "escl.",
                        "interiezione ",
                        "loc.",
                        "locuzione ",
                        "prep.",
                        "preposizione ",
                        "s.",
                        "sostantivo ",
                        "v.",
                        "verbo "
                        ],
               'genere': ["m.",
                          "maschile ",
                          "f.",
                          "femminile "
                          ],
               'aggiuntivo': ["inv.",
                              "invariabile ",
                              "determ.",
                              "determinativo ",
                              "tr.",
                              "transitivo ",
                              "intr.",
                              "intransitivo ",
                              "rifl.",
                              "riflessivo "
                              ]}
    risultato = {"tipo": "", "genere": "", "aggiuntivo": ""}
    for n_tipo in range(len(diz['tipo'])):
        if n_tipo % 2 == 0 and stringa.find(diz['tipo'][n_tipo]) != -1 and diz['tipo'][n_tipo] != "v.":
            risultato['tipo'] += (diz['tipo'][n_tipo + 1])
        elif diz['tipo'][n_tipo] == "v." and stringa.find("avv.") == -1 and stringa.find("inv.") == -1 and stringa.find("v.") != -1:
            risultato['tipo'] += "verbo "
    for n_genere in range(len(diz['genere'])):
        if n_genere % 2 == 0 and stringa.find(diz['genere'][n_genere]) != -1:
            risultato['genere'] += diz['genere'][n_genere + 1]
    for n_aggiuntivo in range(len(diz['aggiuntivo'])):
        if n_aggiuntivo % 2 == 0 and stringa.find(diz['aggiuntivo'][n_aggiuntivo]) != -1:
            risultato['aggiuntivo'] += (diz['aggiuntivo'][n_aggiuntivo + 1])
    return risultato


def pagina_dizionario(link: str):
    page = requests.get(link)
    return page.text


def trova_link(pagina, lettera: str):
    html = BeautifulSoup(pagina, 'html.parser')
    link_inizio = lettera.upper() + '/'
    link_fine = '.shtml'
    risultati = {'parole': [], 'link': []}
    for link in html.find_all('a', href=True):
        if ("#" not in link['href']) and ("tel:" not in link['href']) and ("mailto:" not in link['href']) and ("javascript:" not in link['href']):
            if link['href'][:2] == link_inizio and link['href'][-6:] == link_fine:
                risultati['link'].append(
                    "/dizionario_sinonimi_contrari/" + link['href'])
                risultati['parole'].append(link.text)
    return risultati


def sicura(pagina):
    html = BeautifulSoup(pagina, 'html.parser')
    if html.find('div', class_='title'):
        return False
    return True

reset_db()


for lettera in alfabeto:
    sicuro = True
    pagina = 0

    while sicuro == True:
        pagina += 1
        if pagina == 1:
            link = inizio + lettera.lower() + fine
        else:
            link = inizio + lettera.lower() + "_" + str(pagina) + fine
        pag = pagina_dizionario(link)
        sicuro = sicura(pag)
        parole = trova_link(pag, lettera)
        for n_parole in range(len(parole['parole'])):
            parola = parole['parole'][n_parole].split(" ")[0]
            if parola.isalpha() == False and parola[:-1].isalpha() == True:
                parola = parola[:-1]
            n += 1
            conoscenza = conosci(parole['parole'][n_parole])
            #print(mt.to36(n), parola, conoscenza['tipo'], conoscenza['genere'],
            #    conoscenza['aggiuntivo'], parole['link'][n_parole])
            aggiungi_parola(n, parola, conoscenza['tipo'], conoscenza['genere'], conoscenza['aggiuntivo'], parole['link'][n_parole])
        print(link)