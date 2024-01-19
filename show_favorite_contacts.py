def showFavoriteContacts(contacts):
    print("\nContatos favoritos :")

    for index, contact in enumerate(contacts, start=1):
        if contact["isFavorite"]:
            print(f"❤️ {index}. {contact['name']}: {contact['number']}")
