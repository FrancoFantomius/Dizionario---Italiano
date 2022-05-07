#   Dizionario Italiano

In questa repository si trova il codice per generare un dizionario in italiano dal <a href = "https://it.wiktionary.org/">dizionario di wikipedia</a>.
Può essere utile in caso si dovessero trovare le definizioni o i sinonimi di tutte le 556 376 parole presenti per l'italiano.

Ultimo aggiornamento README.md: 07 maggio 2022 16:34


#   Scaricare la versione presente

Nella cartella <code>Dizionario</code> è presente l'ultima versione creata. In <code>info.txt</code> si trova la data dell'ultimo aggiornamento, in caso si voglia una versione precedente è presente la cartella <code>Storico</code> con le cartelle di tutte le versioni precedenti.

Il dizionario ha un database SQLite accessibile in Python dove è presente un'indice delle parole (sia forma base sia forme composte per nomi e aggettivi) con la relativa collocazione.
Tutte le forme base delle parole sono in file <b>.json</b> organizzati in sotto-cartelle in base alle prime due lettere della forma base delle parole (Esempio: <b>Abaco</b> -> <b>/a/ab/abaco.json</b>).
Tutti i file hanno le seguenti categorie:
-   Forma base;
-   Sillabazione;
-   Pronuncia;
-   Definizione;
-   Forme composte (solamente per nomi e aggettivi).

Alcuni file hanno anche:
-   Sinonimi;
-   Contrari;
-   Parole derivate;
-   Termini correlati.

#   Per generare un nuovo dizionario:

##  Requisiti:
-   <b>Python 3.9</b> o superiore (è stato testato con la versione 3.9.6)
-   <a href = 'https://pypi.org/project/beautifulsoup4/'><b> Beautiful Soup </b></a>
-   <a href = 'https://pypi.org/project/requests/'><b> Requests </b></a>

##  Informazioni:
Il programma richiede ai server della <a href = 'https://wikimediafoundation.org/'>Fondazione Wikimedia</a> le pagine del dizionario, è consigliato <b>controllare i loro <a href = 'https://foundation.wikimedia.org/wiki/Terms_of_Use/en'>termini di utilizzo</a></b> prima di eseguire il programma.

##  Istruzioni:
-   ⬇️<b>Scaricare</b> la cartella <code>Codice</code>
-   ✔️Verificare che i <b>requisiti</b> siano soddisfatti
-   📦<b>Decomprimere</b> i file
-   ▶️<b>Eseguire</b> <code>start.py</code>
