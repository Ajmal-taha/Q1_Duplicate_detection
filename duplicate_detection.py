FILE_PATH = "document.txt"

seen_set = set()
duplicate_set = set()

with open(FILE_PATH, 'r') as f:
    email = f.readline()
    while(email):
        email = email.strip()
        if email in seen_set:
            if email not in duplicate_set:
                duplicate_set.add(email)
        else:
            seen_set.add(email)

        email = f.readline()

print(duplicate_set)