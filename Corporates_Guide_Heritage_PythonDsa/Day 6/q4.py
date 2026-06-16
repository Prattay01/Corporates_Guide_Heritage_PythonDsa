age = 22
is_citizen = True
is_registered = True

def check_age():
    print("[Executing] Checking age boundary...")
    return age >= 18

def check_citizenship():
    print("[Executing] Checking citizenship status...")
    return is_citizen is True

def check_registration():
    print("[Executing] Checking voting registry...")
    return is_registered is True

print("--- Starting Voter Eligibility Verification ---")

if check_age() and check_citizenship() and check_registration():
    print("\nResult: Eligible to vote!")
else:
    print("\nResult: NOT eligible to vote.")