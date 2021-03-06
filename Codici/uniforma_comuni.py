# Questo codice serve ad inserire il codice del comune all'interno del dataset degli ospedali
# e delle biblioteche partendo dal dataset dei codici dei comuni preso dall'istat
import pandas as pd
import csv

# carichiamo il dataset contenente i comuni e i relativi codici catastali
comuni=pd.read_csv(open("Open data/Progetto/dataset/Elenco_codici_comuni.csv"))

# Listacomuni contiene coppie del tipo{NomeComune:Codicecomune(istat)} 
listacomuni=dict(zip(comuni.DENOMINAZIONE_COMUNE.str.lower().unique(),comuni.CODICE_COMUNE.unique()))

#----------Ospedali------------

ospedali=csv.reader(open("Open data/Progetto/dataset/Ospedali e case di cura.csv"))

# Scrittura del file di output
writer_osp=csv.writer(open("Open data/Progetto/dataset/Ospedali e case di cura1.csv","wt",newline=""))
writer_osp.writerow(["Provincia","Denominazione_Strutture","Indirizzo","CAP","Comune","Descrizione_tipo_struttura","Email","Sito_web","Latitudine","Longitudine","Cordinate_comune","Codice_Comune"])

next(ospedali)

for row in ospedali:
    if row[4].lower() in listacomuni.keys():# Row[4] contiene il nome del comune contenuto del datset degli ospedali 
        # Row[4] viene usato come chiave per listacomuni, restituendo il codice del comune corrispondente
        row.append(listacomuni[row[4].lower()])
        writer_osp.writerow(row)
    else:
        writer_osp.writerow(row)

#---------Biblioteche------------

biblioteche=csv.reader(open("Open data/Progetto/dataset/Biblioteche.csv",encoding="utf-8"))
writer_bib=csv.writer(open("Open data/Progetto/dataset/Biblioteche1.csv","wt",newline=""))

#Scriviamo l'intestazione
writer_bib.writerow(["Provincia","Biblioteca","URI","Indirizzo","CAP","Comune","Latitudine","Longitudine","Codice_comune"])
next(biblioteche)

for row in biblioteche:
    if row[5].lower() in listacomuni.keys():# Row[5] contiene il nome del comune contenuto del datset degli ospedali 
        # Row[5] viene usato come chiave per listacomuni, restituendo il codice del comune corrispondente
        row.append(listacomuni[row[5].lower()])
        writer_bib.writerow(row)
    else:
        writer_bib.writerow(row)
