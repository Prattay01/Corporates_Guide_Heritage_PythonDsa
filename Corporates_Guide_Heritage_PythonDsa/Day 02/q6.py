raw_name = '  John Doe  '

initial_len = len(raw_name)
cleaned_name = raw_name.strip()
cleaned_len = len(cleaned_name)

uppercase_name = cleaned_name.upper()
lowercase_name = cleaned_name.lower()

print(f"Original String       : '{raw_name}' (Length: {initial_len})")
print(f"After strip()         : '{cleaned_name}' (Length: {cleaned_len})")
print(f"After upper()         : '{uppercase_name}'")
print(f"After lower()         : '{lowercase_name}'")