import random

# STEP 1: input utente
def step_input(_):
    scelta = input("Scegli 'testa' o 'croce': ").lower()
    return scelta

# STEP 2: lancio moneta
def step_lancio(scelta):
    risultato = random.choice(["testa", "croce"])
    return scelta, risultato

# STEP 3: confronto
def step_confronto(dati):
    scelta, risultato = dati
    vittoria = scelta == risultato
    return scelta, risultato, vittoria

# STEP 4: output finale
def step_output(dati):
    scelta, risultato, vittoria = dati
    
    print("\n--- RISULTATO ---")
    print(f"Hai scelto: {scelta}")
    print(f"È uscito: {risultato}")
    
    if vittoria:
        print("Hai vinto! 🎉")
    else:
        print("Hai perso 😢")

# PIPELINE
def pipeline():
    dato = None
    dato = step_input(dato)
    dato = step_lancio(dato)
    dato = step_confronto(dato)
    step_output(dato)

# ESECUZIONE
pipeline()