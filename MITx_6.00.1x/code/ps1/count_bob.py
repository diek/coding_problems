# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl',
# then your program should print

# Number of times bob occurs is: 9

random_string = "bobobgbobobbobxboobxqbobbkbobbowobubobob"


def count_bob(count, idx, random_string):
    for _ in range(1, (len(random_string))):
        if random_string.find("bob", idx) >= 0:
            idx = random_string.find("bob", idx)
            idx += 1
            count += 1
    return count


print(f"Number of times bob occurs is: {count_bob(0, 0, random_string)}")
