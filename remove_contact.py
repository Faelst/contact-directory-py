from validate_index import validateIndex
from save_file import salveFile


def removeContact(contacts):
    contactIndex = int(input("Digite o numero do contato que deseja remover: ")) - 1

    if validateIndex(contactIndex, contacts):
        contactName = contacts[contactIndex]["name"]
        contacts.pop(contactIndex)
        salveFile(contacts)
        print(f"Contato {contactName} excluído")
    else:
        print("Contato invalido")
    return
