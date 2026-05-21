nums = [1, 2, 3, 4]

squares = [n*n for n in nums]
print(squares)

cubes = [n**3 for n in nums]
print(cubes)

string = ["apple", "BaNana", "sTring"]

upper_string = [str.upper(element) for element in string]
print(upper_string)

string_len = [len(element) for element in string]
print(string_len)

even_nums = [n for n in range(21) if n % 2 == 0]
print(even_nums)

nums2 = [-2, 5, 0, -9, 3, 5, -4]

nums2_positive = [n for n in nums2 if n > 0]
print(nums2_positive)

words = ["chirag", "for", "and", "footy", "movie", "is"]

long_words = [element for element in words if len(element) > 4]
print(long_words)

empty = ["mom", "toy", "", "hi", "", "trust"]

remove_empty = [element for element in empty if len(element) > 0]
print(remove_empty)

replace_negatives = [n if n > 0 else 0 for n in nums2]
print(replace_negatives)

even_odd = ['even' if n % 2 == 0 else 'odd' for n in nums]
print(even_odd)

first_letter = [word[0] for word in words]
print(first_letter)

l = "education"
vowels = ['a', 'e', 'i', 'o', 'u']

vowels_string = [l[n] for n in range(
    len(l)) if l[n] == 'a' or l[n] == 'e' or l[n] == 'i' or l[n] == 'o' or l[n] == 'u']
print(vowels_string)

nested = [[1, 2], [3, 4], [5, 6]]

joined = [n for y in range(len(nested)) for n in nested[y]]
print(joined)

nums3 = [10, 20, 30]

normalized = [n / sum(nums3) for n in nums3]
print(normalized)

students = [
    {"name": "A", "marks": 95},
    {"name": "B", "marks": 70}
]

filtered = [students[n]
            for n in range(len(students)) if students[n]["marks"] > 90]
print(filtered)

filtered_names = [students[n]["name"]
                  for n in range(len(students)) if students[n]["marks"] > 90]
print(filtered_names)
