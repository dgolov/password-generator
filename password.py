import secrets


def create_new(length, character_list):
    characters = ""
    is_valid = False

    for item in character_list:
        characters += item

    while not is_valid:
        password = "".join(secrets.choice(characters) for _ in range(length))
        for item in character_list:
            if not item:
                break
            if any(char in password for char in item):
                is_valid = True
            else:
                is_valid = False
                break

    return password
