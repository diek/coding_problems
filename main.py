def count_up_to(n):
    """Yield numbers from 1 up to n."""
    num = 1
    while num <= n:
        yield num
        num += 1


def main():
    # Using the generator
    for number in count_up_to(5):
        print(number)


if __name__ == "__main__":
    main()
