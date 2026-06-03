from fastapi import FastAPI, HTTPException
# Importiamo solo le funzioni logiche dal tuo file originale
from testaocroce import step_lancio, step_confronto

# Creiamo l'istanza dell'API
app = FastAPI(title="API Testa o Croce")

# Definiamo un "endpoint" (una rotta web) a cui gli utenti possono accedere
@app.get("/gioca")
def gioca_testa_o_croce(scelta: str):
    """
    Gioca a testa o croce! 
    Inserisci 'testa' o 'croce' come parametro.
    """
    scelta_pulita = scelta.lower()
    
    # Controllo che l'utente abbia inserito una scelta valida
    if scelta_pulita not in ["testa", "croce"]:
        raise HTTPException(status_code=400, detail="Errore: Devi scegliere 'testa' o 'croce'.")
    
    # 1. Saltiamo step_input() perché l'input arriva dall'URL (parametro 'scelta')
    
    # 2. Lancio la moneta usando la tua funzione
    dati_lancio = step_lancio(scelta_pulita)
    
    # 3. Confronto i risultati usando la tua funzione
    scelta_finale, risultato, vittoria = step_confronto(dati_lancio)
    
    # 4. Saltiamo step_output() e restituiamo un JSON (dizionario Python)
    return {
        "tua_scelta": scelta_finale,
        "risultato_moneta": risultato,
        "hai_vinto": vittoria,
        "messaggio": "Hai vinto! " if vittoria else "Hai perso "
    }