def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def main():
    """Main function to demonstrate the calculate_average function."""
    numbers = [2, 4, 6, 8, 10]
    average = calculate_average(numbers)
    print(f"The average of the numbers is {average}")


if __name__ == "__main__":
    main()

