from sortedcontainers import SortedDict
from sortedcontainers import SortedList

class Contact():
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return "Name: {}\nPhone: {}\nEmail: {}\n".format(self.name, self.phone_number, self.email)

class ContactList():
    def __init__(self):
        self.contact_map = {}
        self.name_map = SortedDict()
        self.phone_map = {}
        self.email_map = {}
        self.unique_id = 1


    def add_contact(self, name, phone, email):
        self.contact_map[self.unique_id] = Contact(name, phone, email)
        self.name_map[name] = self.unique_id
        self.phone_map[phone] = self.unique_id
        self.email_map[email] = self.unique_id
        self.unique_id += 1


    def get_by_name(self, name):
        name_id = self.name_map[name]
        return self.contact_map[name_id]


    def get_by_phone(self, phone):
        phone_id = self.phone_map[phone]
        return self.contact_map[phone_id]


    def get_by_email(self, email):
        email_id = self.email_map[email]
        return self.contact_map[email_id]


    def get_by_id(self, unique_id):
        return self.contact_map[unique_id]


    def remove(self, unique_id):
        contact = self.contact_map[unique_id]
        del self.name_map[contact.name]
        del self.phone_map[contact.phone_number]
        del self.email_map[contact.email]
        del self.contact_map[unique_id]


    def get_contacts_ordered_by_name(self):
        ordered_contact_list = []
        for name in self.name_map:
            ordered_contact_list.append(name)
        return ordered_contact_list

    


contact_list = ContactList() 

contact_list.add_contact('Hanna Hönnudóttir', 1234567, 'hanna@hanna.is')
contact_list.add_contact('Jón Jónsson', 2345678, 'jon@jon.is') 
contact_list.add_contact('Anna Önnudóttir', 3456789, 'anna@anna.is')
contact_list.add_contact('Guðmundur Guðmundsson', 4567890, 'gummi@gummi.is')
contact_list.add_contact('Bryndís Bryndísardóttir', 1234560, 'disa@disa.is') 

some_contact_1 = contact_list.get_by_name('Anna Önnudóttir')
some_contact_2 = contact_list.get_by_phone(4567890) 
some_contact_3 = contact_list.get_by_email('hanna@hanna.is')
print(some_contact_1)
print(some_contact_2)
print(some_contact_3)

ordered_contact_list = contact_list.get_contacts_ordered_by_name() 
for contact in ordered_contact_list:     
    print(contact)
