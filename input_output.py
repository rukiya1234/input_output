

# 1. Name and Age
def name_age():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"Hello {name}, you are {age} years old.")

# 2. Sum of two numbers
def sum_two_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum:", a + b)

# 3. Count words in a file
def count_words_in_file(filename):
    with open(filename, 'r') as f:
        words = f.read().split()
    print("Word count:", len(words))

# 4. Write sentence in reverse order to file
def reverse_sentence_to_file(sentence, filename):
    with open(filename, 'w') as f:
        f.write(sentence[::-1])

# 5. Read CSV into dictionary
import csv
def csv_to_dict(filename):
    data = {}
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data[row[0]] = row[1:]
    return data

# 6. Monitor log file for keyword
def monitor_log(filename, keyword):
    with open(filename, 'r') as f:
        for line in f:
            if keyword in line:
                print("ALERT:", line.strip())
