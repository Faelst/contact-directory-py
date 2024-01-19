from load_contacts import loadContacts
from show_contacts import showContacts
from register_contact import registerContact
from show_favorite_contacts import showFavoriteContacts
from remove_contact import removeContact
from update_contact import updateContact

while True:
    print("\nMenu do Gerenciador de Contatos:\n")
    print("1. Listar Contatos")
    print("2. Listar Favoritos")
    print("3. Adicionar Contato")
    print("4. Remover Contato")
    print("5. Alterar Contato")
    print("6. Sair")

    choose = 0
    try:
        choose = int(input("Digite a sua escolha: "))
        contacts = loadContacts()
    except Exception as e:
        print("\nOpcao invalida...")

    if choose == 1:
        showContacts(contacts)
    elif choose == 2:
        showFavoriteContacts(contacts)
    elif choose == 3:
        registerContact(contacts)
    elif choose == 4:
        removeContact(contacts)
    elif choose == 5:
        updateContact(contacts)
    elif choose == 6:
        break
