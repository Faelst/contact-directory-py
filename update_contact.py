from show_contacts import showContacts
from validate_index import validateIndex
from save_file import salveFile


def updateContact(contacts):
    showContacts(contacts)
    
    contactIndex = int(input('Digite o numero do contato que deseja alterar: ')) - 1
    
    if not validateIndex(contactIndex, contacts):
        print("Contato invalido")
        return
    
    print('\nQual das informacoes deseja alterar:')
    print('1. Nome')
    print('2. Telefone')
    print('3. Favoritar/Desfavoritar')
    print('4. Voltar')

    choose = int(input('Digite a informação que deseja alterar: '))
    
    if choose == 1:
        name = input('Digite o nome: ')
        contacts[contactIndex]["name"] = name
    elif choose == 2:
        number = input('Digite o numero: ')
        contacts[contactIndex]["number"] = number
    elif choose == 3:
        contacts[contactIndex]['isFavorite'] = not contacts[contactIndex]['isFavorite']
    elif choose == 4:
        return
    
    salveFile(contacts)
    print('Contato Atualizado')
    
    return