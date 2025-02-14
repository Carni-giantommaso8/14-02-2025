inventario = {
0 : {"nome": "Il PC di Giantommaso", "quantità": 1, "prezzo": 3999},
1 : {"nome": "Nintendo Switch 2", "quantità": 10, "prezzo": 449},
2 : {"nome": "GTA VI", "quantità": 3, "prezzo": 100}
}
contatore = 2
def aggiunta ():
    global contatore
    nome = input("scrivi nome: ")
    quantità = int(input("scrivi una quantità: "))
    prezzo = int(input("scrivi prezzo: "))
    contatore += 1
    inventario[contatore]= {"nome": nome,"quantità": quantità,"prezzo": prezzo}
    return  contatore,inventario

print("inserisci 1 per aggiungere uno/a studente")
while True:
    comando = int(input("scegli un opzione: "))
    if comando == 1:
        print(aggiunta())