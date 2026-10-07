# Schema cPanel / Passenger

Questi passaggi sono generici perché i nomi esatti delle voci cambiano in base al provider.

1. In cPanel aprire **Setup Python App**.
2. Creare una nuova applicazione Python.
3. Application root: cartella che contiene `app.py`.
4. Application URL: `lariotech.it/auguri`.
5. Startup file: `passenger_wsgi.py`.
6. Entry point: `application`.
7. Entrare nell'ambiente virtuale indicato da cPanel e installare `requirements.txt`.
8. Creare il file `.env` copiando `.env.example`.
9. Riavviare l'app Python dal pannello cPanel.
10. Verificare `https://lariotech.it/auguri/health`.

## Cron cPanel
Da **Cron Jobs**, creare una riga giornaliera, per esempio alle 09:00:
`cd /home/USERNAME/PERCORSO/auguri && /home/USERNAME/virtualenv/PERCORSO/3.11/bin/python cron_send.py >> /home/USERNAME/auguri_cron.log 2>&1`

Sostituire i percorsi con quelli mostrati dal proprio cPanel.
