from dotenv import load_dotenv
import os

load_dotenv()
file_path = os.getenv("FILE_PATH")

def duplicate_detect(file_path):
    seen_set = set()
    duplicate_set = set()

    with open(file_path, 'r') as f:
        email = f.readline()
        while(email):
            email = email.strip()
            if email in seen_set:
                if email not in duplicate_set:
                    duplicate_set.add(email)
            else:
                seen_set.add(email)

            email = f.readline()
    return duplicate_set

if __name__ == "__main__":
    duplicate_set = duplicate_detect(file_path)
    print(duplicate_set)