# ===== Question 3 =====

print("\n===== Question 3 =====")

# a) Create phonebook with at least 8 contacts

phonebook = {
    "Aman": {
        "phone": "9876543210",
        "email": "aman@gmail.com",
        "city": "Kolkata"
    },
    "Riya": {
        "phone": "9876543211",
        "email": "riya@gmail.com",
        "city": "Delhi"
    },
    "Rahul": {
        "phone": "9876543212",
        "email": "rahul@gmail.com",
        "city": "Mumbai"
    },
    "Neha": {
        "phone": "9876543213",
        "email": "neha@gmail.com",
        "city": "Pune"
    },
    "Arjun": {
        "phone": "9876543214",
        "email": "arjun@gmail.com",
        "city": "Kolkata"
    },
    "Priya": {
        "phone": "9876543215",
        "email": "priya@gmail.com",
        "city": "Chennai"
    },
    "Ishita": {
        "phone": "9876543216",
        "email": "ishita@gmail.com",
        "city": "Delhi"
    },
    "Karan": {
        "phone": "9876543217",
        "email": "karan@gmail.com",
        "city": "Bangalore"
    }
}

# b) Search Contact

def search_contact(name):
    if name in phonebook:
        print(f"\n{name} Details:")
        print(phonebook[name])
    else:
        print("Contact not found")


# c) Add Contact

def add_contact(name, phone, email, city):
    phonebook[name] = {
        "phone": phone,
        "email": email,
        "city": city
    }
    print(f"{name} added successfully")


# d) Delete Contact

def delete_contact(name):
    if name in phonebook:
        phonebook.pop(name)
        print(f"{name} deleted successfully")
    else:
        print("Contact not found")


# e) Contacts in a specific city

def contacts_in_city(city):
    result = []

    for name, details in phonebook.items():
        if details["city"].lower() == city.lower():
            result.append(name)

    return result


# f) Display all contacts

def display_all():
    print("\nAll Contacts:")

    for name, details in phonebook.items():
        print(f"""
Name : {name}
Phone: {details['phone']}
Email: {details['email']}
City : {details['city']}
-------------------------
""")


# g) Testing all functions (minimum 3 calls each)

print("\n--- Testing search_contact() ---")
search_contact("Aman")
search_contact("Riya")
search_contact("Unknown")

print("\n--- Testing add_contact() ---")
add_contact("Zoya", "9999999999", "zoya@gmail.com", "Delhi")
add_contact("Meera", "8888888888", "meera@gmail.com", "Kolkata")
add_contact("Dev", "7777777777", "dev@gmail.com", "Mumbai")

print("\n--- Testing delete_contact() ---")
delete_contact("Dev")
delete_contact("Meera")
delete_contact("Unknown")

print("\n--- Testing contacts_in_city() ---")
print(contacts_in_city("Kolkata"))
print(contacts_in_city("Delhi"))
print(contacts_in_city("Mumbai"))

print("\n--- Testing display_all() ---")
display_all()
