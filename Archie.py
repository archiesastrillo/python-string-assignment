def reverse_sentence(text):
    return text[::-1]

def count_vowels(text):
    return sum(1 for char in text.lower() if char in "aeiou")

def is_palindrome(text):
    cleaned = ''.join(filter(str.isalnum, text.lower()))
    return cleaned == cleaned[::-1]

def find_and_replace(text):
    word_to_find = input("Enter the word to find: ")
    word_to_replace = input("Enter the replacement word: ")
    return text.replace(word_to_find, word_to_replace)

def format_title_case(text):
    return text.title()

def split_into_words(text):
    return text.split()

def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def swap_case(text):
    return text.swapcase()

def show_menu():
    print("""
Choose an operation:
0. Enter a new sentence
1. Reverse the sentence
2. Count vowels
3. Check if palindrome
4. Find and replace a word
5. Format (title case)
6. Split into words
7. Word frequency counter
8. Swap case
9. Exit
""")

def main():
    text = input("Enter a sentence: ")

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '0':
            text = input("Enter a new sentence: ")

        elif choice == '1':
            print("Reversed:", reverse_sentence(text))

        elif choice == '2':
            print("Vowel count:", count_vowels(text))

        elif choice == '3':
            result = is_palindrome(text)
            print("Palindrome?" , "Yes" if result else "No")

        elif choice == '4':
            text = find_and_replace(text)
            print("Updated sentence:", text)

        elif choice == '5':
            print("Title Case:", format_title_case(text))

        elif choice == '6':
            print("Words:", split_into_words(text))

        elif choice == '7':
            freq = word_frequency(text)
            print("Word Frequency:")
            for word, count in freq.items():
                print(f"{word}: {count}")

        elif choice == '8':
            print("Swapped Case:", swap_case(text))

        elif choice == '9':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
