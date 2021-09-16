with open('inputs.txt', 'r') as f:
    lines = f.readlines()
    num_valid = 0 

    for line in lines:
        frequency, character, password = tuple(line.split(' '))

        num_min, num_max = tuple(map(int, frequency.split('-')))
        character = character.replace(':', '')
        password = password.strip()
    
        if num_min <= password.count(character) <= num_max:
            num_valid += 1

    print(num_valid)