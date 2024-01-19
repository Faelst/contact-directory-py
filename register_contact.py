import json
from load_contacts import loadContacts
from save_file import salveFile

def registerContact(contacts):
    contact = {}
    contact['name'] = input('Digite o nome do contato: ')
    contact['number'] = input('Digite o numero do contato: ')
    contact['isFavorite'] = True if int(input('E um contato favorito ? (1 - Sim / 2 - Não)')) == 1 else False

    contacts.append(contact)
    salveFile(contacts)

    print('\nNovo contato adicionado.')
    return;
