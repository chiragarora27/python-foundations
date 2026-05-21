string1 = input("Enter a sentence: ")

my_list = [letter for letter in string1]

my_dict = {}

my_dict = {characters: 0 for characters in my_list}

for characters in my_dict.keys():
    for letter in my_list:
        if (characters == letter):
            my_dict[characters] += 1

for key, value in my_dict.items():
    print(key + '-> ', value)
