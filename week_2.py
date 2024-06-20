def count_words(input_string):
    # Split the string by whitespace and filter out any empty strings
    words = input_string.split()
    return len(words)


def main():
    while True:
        # Prompt the user to enter a sentence or paragraph
        input_string = input("Enter a sentence or paragraph: ")

        # Check if the input is empty
        if len(input_string) == 0:
            print("Please enter a non-empty string.")
        else:
            # Count the number of words in the input
            word_count = count_words(input_string)

            # Display the word count
            print(f"The number of words in the input is: {word_count}")
            break


if __name__ == "__main__":
    main()
