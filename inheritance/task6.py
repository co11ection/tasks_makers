class ContactList(list):

    def search_by_name(self, name: str) -> list:
        result = [contact for contact in self if name.lower() in contact.lower()]
        
        return result


all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])

print(all_contacts.search_by_name('Olya'))
