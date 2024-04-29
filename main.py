def get_text(book):
    with open(book) as f:
        return f.read()
    
def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_letters(book_text):
    letter_count = {}
    l_case_text = book_text.lower()
    for char in l_case_text:
        if char in letter_count:
            letter_count[char] += 1
        elif char not in letter_count:
            letter_count[char] = 1
    return letter_count
    
        

def main():
    book_location = "books/frankenstein.txt"
    text = get_text(book_location)
    word_count = count_words(text)
    letter_count = count_letters(text)
    print(letter_count)

 
    
main()