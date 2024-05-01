def get_text(book) -> str:
    with open(book) as f:
        return f.read()
    
def count_words(book_text: str) -> int:
    words = book_text.split()
    return len(words)

def count_letters(book_text: str) -> dict[str, int]:
    letter_count = {}
    l_case_text = book_text.lower()
    for char in l_case_text:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            elif char not in letter_count:
                letter_count[char] = 1
    return letter_count

def split_letter_count(letter_count: dict[str, int]) -> list[dict]:
    rev_letter_count = []
    for letter in letter_count:
        rev_letter_count.append({"letter": letter, "count": letter_count[letter]})
    return rev_letter_count

def sort_on(dict: dict) -> int:
    return dict["count"]

def sort_letters(rev_count: list[dict]) -> list[dict]:
    rev_count.sort(reverse=True, key=sort_on)
    return rev_count
    




def main():
    book_location = "books/frankenstein.txt"
    text = get_text(book_location)
    word_count = count_words(text)
    letter_count = count_letters(text)
    rev_letter_count = split_letter_count(letter_count)
    sorted_letters: list[dict[str, int]]= sort_letters(rev_letter_count)
    print(f"--- Word and Letter Count Data for {book_location} ---")
    print()
    print(f"The document contains {word_count} words.")
    print()
    for entry in sorted_letters:
        print(f"The letter {entry["letter"]} occured {entry["count"]} times.")


 
    
main()