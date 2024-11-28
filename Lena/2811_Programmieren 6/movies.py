filme = {
    "Science-Fiction": "Inception",
    "Fantasy": "Harry Potter",
    "Geschichtsdrama": "Titanic"
}

filme.get("Fantasy")
print(filme["Fantasy"])

filme["Science-Fiction"] = str("The Matrix")

ausgabe = ", ".join([f"{genre}: {title}" for genre, title in filme.items()])
print(ausgabe)

#for genre, title in filme.items():
#print(genre, title)