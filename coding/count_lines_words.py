def line_counter():
    with open("sopranos_users.csv", "r") as file:
        for idx, _ in enumerate(file):
            pass
    return idx + 1


def sum_lines():
    with open("sopranos_users.csv", "r") as f:
        line_count = sum(1 for line in f)
    return line_count


def sum_lines2():
    with open("sopranos_users.csv") as f:
        line_count = sum(1 for _ in f)
    return line_count


def word_counter():
    count = 0
    with open("words.txt", "r") as file:
        for line in file:
            words = len(line.split(" "))
            count += words

    return count


def count_words():
    with open("words.txt") as f:
        data = f.read()
        return sum(1 for word in data.split())


# Count Lines
print(line_counter())
print(sum_lines())

# Count Words
print(word_counter())
print(count_words())
