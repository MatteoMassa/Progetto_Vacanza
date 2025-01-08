# Progetto_Vacanza
sono stanco

# COME ACCEDERE AL PROGRAMMA!

# Step 1.
fare un install dei requirements.txt prima di procedere.

# Step 2.
Andare nella cartella "Progetto" e selezionare il PlantUML per poi procedere con un ALT+D per visualizzare l'interfaccia grafica

# Step 3.
Sempre nella cartella "Progetto" selezionare il file python "Progetto_Bank" ed eseguire tramite terminale il comando "python Progetto_Bank" oppure cliccando sulla freccetta a schermo nel lato destro del monitor 

# Step 4.
Divertiti a far finta di essere miliardario con un conto fasullo!


## Dettagli del Programma

Il programma `Progetto_Vacanza` è un'applicazione di tracciamento del budget progettata per aiutare gli utenti a gestire le loro finanze personali. Ecco una panoramica dettagliata delle funzionalità e della struttura del programma:

# Piano di Sviluppo(non ho usato il modello waterfall):

1. **Classi Transaction e Budget**
    - La classe `Transaction` rappresenta una singola transazione finanziaria, con attributi come importo, categoria, descrizione, data e tipo (spesa o entrata).
    - La classe `BudgetTracker` gestisce il database delle transazioni e fornisce metodi per aggiungere nuove transazioni.

2. **Database SQLite**
    - Il programma utilizza un database SQLite per memorizzare le transazioni. La tabella `transactions` contiene campi per l'id, l'importo, la categoria, la descrizione, la data e il tipo di transazione.

3. **GUI con customtkinter**
    - L'interfaccia utente è costruita utilizzando la libreria `customtkinter`, che fornisce widget personalizzati per creare un'interfaccia grafica intuitiva e user-friendly.

Questa applicazione è progettata per essere estensibile e facile da usare, con una chiara separazione tra la logica di gestione del budget e l'interfaccia utente.