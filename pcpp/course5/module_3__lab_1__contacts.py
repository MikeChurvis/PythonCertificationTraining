import csv


class PhoneContact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Phone:
    def __init__(self):
        self.contacts: list[PhoneContact] = []
        self.load_contacts_from_csv()

    def load_contacts_from_csv(self):
        with open('contacts.csv', newline='') as contacts_file:
            contacts_reader = csv.DictReader(contacts_file)
            self.contacts = [PhoneContact(contact['Name'], contact['Phone']) for contact in contacts_reader]

    def search_contacts(self):
        user_search_input = input("Search contacts for: ").strip().lower()

        search_results = tuple(filter(
            lambda contact: contact.name.lower().startswith(user_search_input),
            self.contacts
        ))

        if len(search_results) == 0:
            print("No contacts found.")
            return

        for result in search_results:
            print(f"{result.name} ({result.phone})")


if __name__ == '__main__':
    def main():
        Phone().search_contacts()


    main()
