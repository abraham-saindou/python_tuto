#fonctions agissant sur les liste

myliste = ["banana", "apple", "pomegranate"]
print(myliste)
#- ajout d'éléments

myliste.append("lemon")
print(myliste)
# insert() add an item to a specified index position
myliste.insert(1, "mango")
print(myliste)

#- enlever des éléments
# pop() enleve, sans parametre, le dernier objet de l'index ou sinon specifier directement le num d'index
item1 = myliste.pop(1)
print(myliste)

# remove()
item2 = myliste.remove(myliste[0])
print(myliste)

"""myliste.clear()
if len(myliste):
    print("myliste is not empty")
else: print("myliste is empty")"""

#copy() create a separate list or newlist = list(myliste) do the same
myliste_copy = myliste.copy()
myliste_copy.pop(1)
print(myliste)
print(myliste_copy)