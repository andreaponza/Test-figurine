#Simulatore album di figurine, stima di pacchetti da recuperare per completarlo
import random
import csv

n_tot = 748 #Figurine album
n_fig_pac = 5 #Numero figurine in un pacchetto
album = [] #Album da riempire	
doppioni = 0 #Contatore doppioni
mancanti = n_tot #Contatore mancanti
n_pac = 1000 #Numero pacchetti
pacs = [] #Pacchetti con figurine
pac_index = 0 #Numero pacchetto aperto

#Creiamo l'album da riempire
for i in range(1, 749):
    album.append(0)

#Prepariamo il file csv dove salvare i dati
with open('data.csv', mode='w') as data_file:
    data_file = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data_file.writerow(["Pacchetto", "Mancanti", "Doppioni"])

#Creiamo i pacchetti da spacchettare
    for i in range(0, n_pac):
        pac =[]
        for fig in range(0, n_fig_pac):
            pac.append(random.randint(1, n_tot))
        pacs.append(pac)

#Spacchettiamo i pacchetti
    for pac in pacs:
        for fig in pac:
            if album[fig-1] == 0: #Se la figurina manca nell'album la appiccichiamo altrimenti la aggiungiamo ai doppioni
                album[fig-1] = fig
                mancanti = mancanti-1
            else:
                doppioni = doppioni+1
        if mancanti == 0: #Interrompi se l'album è completo
            break
        pac_index = pac_index + 1 #Teniamo il conto dei pacchetti aperti
        data_file.writerow([pac_index, mancanti, doppioni]) #Salviamo i dati nel file data.csv dopo l'apertura di ogni pacchetto

#Controlliamo l'album
fig_attaccate = 0
for fig in album:
    if fig != 0:
        fig_attaccate = fig_attaccate+1
#Riepilogo del risultato
print("Pacchetti", "Attaccate", "Mancanti",  "Totali", "Doppioni")
print(pac_index, fig_attaccate, mancanti, (fig_attaccate + mancanti), doppioni)