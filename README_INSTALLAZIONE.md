# Auguri WhatsApp V3 Web

Applicazione web per gestire compleanni e inviare automaticamente messaggi tramite WhatsApp Cloud API.

## Funzioni
- login amministratore
- dashboard compleanni di oggi
- rubrica con categorie, note e attivazione/disattivazione
- template WhatsApp approvati suddivisi per categoria
- scelta random del template per categoria
- variabili `{nome}` e `{eta}` nell'anteprima
- invio manuale e automatico
- storico con ID messaggio Meta
- blocco doppio invio nello stesso giorno
- import CSV/XLSX, export XLSX, backup database
- interfaccia responsive per PC e smartphone

## Requisiti server
- Python 3.10+ (consigliato 3.11/3.12)
- HTTPS sul dominio
- possibilità di eseguire un'app WSGI (Passenger, Gunicorn + reverse proxy, ecc.)
- cron job server consigliato

## Installazione su lariotech.it/auguri
1. Caricare questa cartella sul server, ad esempio in `lariotech.it/auguri`.
2. Creare ambiente virtuale Python e installare:
   `pip install -r requirements.txt`
3. Copiare `.env.example` in `.env`.
4. Cambiare almeno `SECRET_KEY`, `ADMIN_PASSWORD`, `CRON_SECRET`.
5. Inserire `WHATSAPP_TOKEN` e `WHATSAPP_PHONE_NUMBER_ID` ottenuti da Meta.
6. Configurare l'app WSGI usando `passenger_wsgi.py` oppure Gunicorn.
7. Associare pubblicamente l'app al percorso HTTPS `https://lariotech.it/auguri`.
8. Aprire il sito e accedere con la password configurata.

### Nota importante sul sottopercorso /auguri
La configurazione esatta dipende dall'hosting. Se cPanel/Passenger permette di scegliere l'Application URL, impostarlo direttamente su `/auguri`. Se si usa Nginx/Apache come reverse proxy, inoltrare `/auguri` verso l'applicazione preservando correttamente `SCRIPT_NAME` oppure rimuovendo il prefisso lato proxy.

## Configurazione WhatsApp Cloud API
La V3 usa l'endpoint ufficiale Graph API e invia messaggi di tipo `template`.

La struttura standard inclusa presume che i template approvati abbiano due parametri BODY:
- `{{1}}` = nome
- `{{2}}` = età

Esempio testo template da creare/approvare in Meta:
`Buon compleanno {{1}}! Tanti auguri per i tuoi {{2}} anni! 🎉`

Nel pannello V3 inserire:
- Etichetta: a piacere
- Categoria: es. Amici
- Nome template Meta: esattamente il nome approvato
- Lingua: es. `it`
- Anteprima: `Buon compleanno {nome}! Tanti auguri per i tuoi {eta} anni! 🎉`

Per avere frasi random, creare e far approvare più template Meta e inserirli nella stessa categoria.

## Invio automatico - metodo consigliato
Configurare un cron server una volta al giorno all'orario desiderato:
`cd /PERCORSO/auguri && /PERCORSO/python cron_send.py >> cron.log 2>&1`

Il pannello mostra l'orario desiderato, ma se si usa `cron_send.py` è il cron server a determinare l'orario effettivo. Impostare quindi il cron alla stessa ora scelta nel pannello.

### Alternativa: cron HTTP
È disponibile `POST /cron/run`, protetto da header:
`X-Cron-Secret: <CRON_SECRET>`

Può essere richiamato ogni 5 minuti. L'app invia soltanto nella finestra di 15 minuti successiva all'orario impostato.

## Primo test consigliato
1. Creare un contatto di prova con compleanno oggi.
2. Inserire un template Meta già APPROVATO.
3. Controllare che `.env` contenga token e Phone Number ID corretti.
4. Dal pannello usare “Invia ora”.
5. Controllare lo Storico.
6. Solo dopo attivare il cron automatico.

## Sicurezza
- non pubblicare mai `.env`
- usare HTTPS
- usare password forte
- usare un token Meta adatto all'uso server e proteggerlo
- mantenere backup del file `data/auguri_v3.db`

## Avvio locale per test
`python app.py`
Poi aprire `http://127.0.0.1:5000`
