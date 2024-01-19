def showContacts(contacts):
    print("\nContatos :")
    
    for index, contact in enumerate(contacts, start=1):
        isFavorite = "❤️" if contact['isFavorite'] else ' '
        print(f"{isFavorite} {index} - {contact['name']}: {contact['number']}")