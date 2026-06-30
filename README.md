# SocialPPM - Social Network

**Studente:** Gabriele Fabbri

* **Tipo di progetto scelto:** Full-Stack Applicazione Web
* **Framework usato:** Django

## Descrizione
Questa applicazione è un Social Network completo sviluppato in Django, permette agli utenti di registrarsi, creare e personalizzare il proprio profilo, pubblicare post, seguire altri utenti e visualizzare un feed personalizzato con i contenuti pubblicati. L'interfaccia è stata sviluppata utilizzando HTML, CSS e Bootstrap. 
## Funzionalità Implementate per Ruolo 

##### Funzionalità implementate (per Ruolo)

L'applicazione gestisce una gerarchia di permessi a 3 livelli:

**1. Utente Standard (User):**
- Registrazione, Login e Logout.
- Creazione, visualizzazione, modifica ed eliminazione dei propri post.
- Visualizzazione e modifica del proprio profilo personale.
- Possibilità di seguire/smettere di seguire altri utenti (Follow system).
- Visualizzazione del Feed principale.

**2. Moderatore (Manager):**
- Tutte le funzionalità dell'utente standard.
- Permesso speciale per eliminare post inappropriati di qualsiasi utente, eccetto dell'admin.
- Possibilità di disattivare o bannare gli account degli utenti standard.

**3. Amministratore (Admin):**
- Accesso completo al pannello di controllo (Django Admin).
- Gestione totale del database.
- Potere assoluto di gestire, promuovere, retrocedere o eliminare qualsiasi account (inclusi i Moderatori).
## Istruzioni per l'Installazione Locale

Istruzioni per l'Installazione Locale

**1 Clona il repository: git clone [https://github.com/gabrielefabbri03/progetto_social_network.git](https://github.com/gabrielefabbri03/progetto_social_network.git)**

**2 Entra nella cartella: cd progetto_social_network** 

**3 Crea e attiva un ambiente virtuale:**

- Windows: python -m venv .venv e .venv\Scripts\activate

- Mac/Linux: python3 -m venv .venv e source .venv/bin/activate

**4 Installa le dipendenze: pip install -r requirements.txt**

**5 Applica le migrazioni: python manage.py migrate**

**6 Avvia il server: python manage.py runserver**

L'applicazione sarà disponibile all'indirizzo [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Scenario di Test (Browser)
Per verificare il corretto funzionamento del progetto, si consiglia di: 

**1** Test Post: Effettuare il login come user_1 e pubblicare un nuovo post nel feed.

**2** Test Moderazione: Loggarsi come manager_user e verificare la possibilità di eliminare il post creato da user_1

**3** Test Follow: Testare le funzionalità di follow/unfollow tra utenti diversi.

**4** Test Ban: Loggarsi come admin, bannare un account (disattivandolo), quindi verificare che l'utente bannato non riesca più ad accedere al sistema.
## Database e Account Demo

Il repository include il file **`db.sqlite3`**, che è pre-popolato con dati demo realistici (utenti, profili, post e relazioni di follow) per permettere l'esplorazione immediata dell'applicazione.

**Account Demo Disponibili:**
* **admin** / `admin123` - administrator 
* **manager_user** / `ciao12345` - moderator
* **user_1** / `user12345` - standard user

## Link al Deployment

Il progetto è online e raggiungibile al seguente link:  
https://progetto-social-network.onrender.com

---
*Progetto sviluppato per il corso Back-end PPM 2026.*