'''Text Utilities

a content analytics tool processress user text it needds to count words find unique terms and
manipulate strings

challenges 
ensure accurate word counts even with repeared words
unique word extraction should ignore duplicates 
string operatrions must work correctly for all cases

Word count - hello word should return 2
unique words - repeated words should appear once in results
string reversal reversing abc to cba
edge cases empty strings single words, special characters
case sensitivity Hello vs hello treated separately or normalised'''


class TextUtilities:

    def __init__(self):
        pass

    def word_count(self, text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string")

        if text == "":
            return 0

        words = text.split()
        return len(words)


    def unique_words(self, text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string")

        if text == "":
            return []

        words = text.split()

        unique = []

        for word in words:
            if word not in unique:
                unique.append(word)

        return unique


    def reverse_string(self, text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string")

        return text[::-1]


    def main(self):

        while True:
            print("\n===== Text Utilities Menu =====")
            print("1. Count Words")
            print("2. Find Unique Words")
            print("3. Reverse String")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                text = input("Enter text: ")
                print("Word Count:", self.word_count(text))


            elif choice == "2":
                text = input("Enter text: ")
                print("Unique Words:", self.unique_words(text))


            elif choice == "3":
                text = input("Enter text: ")
                print("Reversed String:", self.reverse_string(text))


            elif choice == "4":
                print("Exiting...")
                break


            else:
                print("Invalid choice")


if __name__ == "__main__":
    text_util = TextUtilities()
    text_util.main()