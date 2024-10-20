import sys
import requests
import hashlib

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        # Print error to standard error and exit the program
        print(f"Error fetching: {res.status_code}, check the API and try again", file=sys.stderr)
        sys.exit(1)  # Exit with an error code
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hash_to_check = hash_to_check.upper()  # Ensure the comparison is case-insensitive
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return int(count)  # Return the breach count as an integer
    return 0  # If no match is found, return 0 breaches

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    print(f"First 5 characters: {first5_char}, Tail: {tail}")
    return get_password_leaks_count(response, tail)

def main():
    password = input("Enter a password to check: ")
    count = pwned_api_check(password)
    if count:
        print(f'{password} was found {count} times... change your password now!!!!')
    else:
        print(f'{password} was not found. You are good to go.')

if __name__ == '__main__':
    main()