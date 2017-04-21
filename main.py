
# CREATE DB

# MENUS
def view_menu():
    a = """Welcome to the domain manager.
    What would you like to do? Choose from the menu below:
    1. View All Entries
    2. View Specific Entry
    3. Create New Entry"""
    print(a)
    user_choice = int(input())
    if (user_choice == 1):
        view_all_entries()
    elif (user_choice == 2):
        view_entry()
    elif (user_choice == 3):
        create_entry()
    else:
        print("You entered an invalid command. Sending you back to main menu.")
        view_menu()

def view_all_entries():
    print("View all entries.")

def view_entry():
    print("View individual entry.")

def create_entry():
    date_added = input("When was the site created? Use month, day, year.")
    url = input("What is the URL? No http required.")
    web_host = input("What web host is this site located at?")
    host_login = input("What is the FTP login IP or URL?")
    username = input("What is the FTP username?")
    password = input("What is the FTP password?")
    city = input("What city does this site represent?")
    niche = input("What niche does this site focus on?")
    forwarding_email = input("What email address should this be forwarded to?")

    print("Please confirm this information is correct.")
    print("Date added: {}".format(date_added))
    print("URL: {}".format(url))
    print("Web Host: {}".format(web_host))
    print("FTP URL or IP: {}".format(host_login))
    print("FTP User Name: {}".format(username))
    print("FTP Password: {}".format(password))
    print("Target City: {}".format(city))
    print("Target City: {}".format(niche))
    print("Forwarding Email: {}".format(forwarding_email))
    confirm = input("Is this correct? Y or N ")

    if (confirm == "Y"):
        # inject data into database
        pass
    else:
        create_entry()

def edit_entry():
    print("Edit entry.")

def delete_entry():
    print("Delete entry.")

if __name__ == "__main__":
    view_menu()
