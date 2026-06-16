username = 'admin'
password = 'secure@123'
is_active = True

if username == 'admin':
    if password == 'secure@123':
        if is_active:
            print("Login successful! Welcome, Admin.")
        else:
            print("Account is deactivated.")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")
