################ Exercice 1:####################

def transform(chain):
    # Mon programme ici
    chain1 = chain[0]
    chain2 = chain[1]
    chain = chain1 + chain2
    if sorted(chain):
        return chain
    else:
        return None

# vous ne modifierez rien après cette ligne
if __name__ == "__main__":
    arr1 = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
    out = transform(arr1)
    print(out) # doit afficher --->31,4,1:nom_prenom_classe
    
    arr3 = ["9, 3, 5, 7, 14", "10, 2, 6, 16, 15"]
    out = transform(arr3)
    print(out) # doit afficher  ---->None