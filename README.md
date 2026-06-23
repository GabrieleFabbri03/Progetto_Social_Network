# SocialPPM - Social Network

**Studente:** Gabriele Fabbri

* **Chosen project type:** Full-Stack Web Application
* **Framework used:** Django

## Descrizione
Questa applicazione è un Social Network completo sviluppato in Django, permette agli utenti di registrarsi, creare e personalizzare il proprio profilo, pubblicare post, seguire altri utenti e visualizzare un feed personalizzato con i contenuti pubblicati. L'interfaccia è stata sviluppata utilizzando HTML, CSS e Bootstrap. 
## Funzionalità Implementate per Ruolo 

##### Funzionalità implementate (per Ruolo)

L'applicazione gestisce una gerarchia di permessi a 3 livelli:

**1. Utente Standard:**
- Registrazione, Login e Logout.
- Creazione, visualizzazione, modifica ed eliminazione dei propri post.
- Visualizzazione e modifica del proprio profilo personale.
- Possibilità di seguire/smettere di seguire altri utenti (Follow system).
- Visualizzazione del Feed principale.

**2. Moderatore:**
- Tutte le funzionalità dell'utente standard.
- Permesso speciale per eliminare post inappropriati di qualsiasi utente.
- Possibilità di disattivare o bannare gli account degli utenti standard.

**3. Amministratore (Superuser):**
- Accesso completo al pannello di controllo (Django Admin).
- Gestione totale del database.
- Potere assoluto di gestire, promuovere, retrocedere o eliminare qualsiasi account (inclusi i Moderatori).
## Istruzioni per l'Installazione Locale

1. **Clona il repository:**
   git clone https://github.com/gabrielefabbri03/progetto_social_network.git
   cd progetto_social_network

2. **Crea e attiva un ambiente virtuale:**
   python -m venv .venv
   #### Su Windows:
   .venv\Scripts\activate
   ### Su macOS/Linux:
   source .venv/bin/activate



3. **Installa le dipendenze richieste:**
   pip install -r requirements.txt

4. **Applica le migrazioni (se necessario):**
   python manage.py migrate

5. **Avvia il server di sviluppo locale:**
   python manage.py runserver
   
   L'applicazione sarà disponibile all'indirizzo http://127.0.0.1:8000/.

## Database e Account Demo

Il repository include il file **`db.sqlite3`**, che è pre-popolato con dati demo realistici (utenti, profili, post e relazioni di follow) per permettere l'esplorazione immediata dell'applicazione.

**Account Demo Disponibili:**
* **admin** / `admin123` - administrator 
* **moderator** / `ciao12345` - advanced role (Moderator)
* **user_1** / `user12345` - standard user

## Link al Deployment

Il progetto è online e raggiungibile al seguente link:  
**FIXME AGGIUNGI IL LINK DI PYTHONANYWHERE**

---
*Progetto sviluppato per il corso Back-end PPM 2026.*