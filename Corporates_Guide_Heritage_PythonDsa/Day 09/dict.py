# update() — merge dicts / add multiple keys at once
profile = {'name': 'Sam', 'age': 25}
extra   = {'city': 'Pune', 'role': 'Developer'}
profile.update(extra)
print(profile)  # {'name': 'Sam', 'age': 25, 'city': 'Pune', 'role': 'Developer'}

profile.update(age=26, salary=60000)   # keyword form also works

# pop() — remove and return a value
removed = profile.pop('role')
print(removed)   # Developer
print(profile)   # role is gone

# pop with default (no KeyError)
val = profile.pop('phone', 'N/A')   # 'N/A'

# setdefault() — insert only if key is missing
profile.setdefault('status', 'active')   # inserts 'active'
profile.setdefault('name', 'Unknown')    # does nothing (name exists)

# Practical: grouping items
words = ['cat', 'apple', 'cow', 'ant', 'cherry']
groups = {}
for w in words:
    groups.setdefault(w[0], []).append(w)
print(groups)  # {'c': ['cat', 'cow', 'cherry'], 'a': ['apple', 'ant']}
