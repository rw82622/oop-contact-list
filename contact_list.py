def sortKey(e):
        return e['name']
class ContactList():
    
    def __init__(self, name, contacts):
        self.name = name
        self.contacts = contacts
    
    def add_contact(self, new_contact):
        self.contacts.append(new_contact)
        if len(self.contacts) > 1:
            self.contacts.sort(key = sortKey)
        
    def remove_contact(self, name_key):
        self.contacts = list(filter(lambda a : a['name'] != name_key, self.contacts))
        
    def find_shared_contacts(self, c_list):
        common_contacts = []
        other_contacts = c_list.__dict__["contacts"]
        for item in self.contacts:
            if (item in other_contacts):
                common_contacts.append(item)
        return common_contacts