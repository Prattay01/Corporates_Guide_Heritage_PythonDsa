DATABASE_USERNAME = "prattay_admin"
DATABASE_PASSWORD = "SecurePassword123"
IS_ACCOUNT_ACTIVE = True

input_username = input("Enter Username: ").strip()
input_password = input("Enter Password: ")

if input_username == DATABASE_USERNAME:
    if IS_ACCOUNT_ACTIVE:
        if input_password == DATABASE_PASSWORD:
            print("\nAccess Granted! Welcome back to the dashboard.")
        else:
            print("\nAccess Denied: Incorrect password. Please try again.")
    else:
        print("\nAccess Denied: This account is currently deactivated.")
else:
    print("\nAccess Denied: Username not found.")