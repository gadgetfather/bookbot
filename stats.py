def get_book_text(book_path):
    with open(book_path) as f:
        file_content = f.read()
    return file_content

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    text = text.lower()
    letters = {}
    for char in text:
        if char.isalpha():
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
    return letters

# retrun list of dictionarries sorted by frequency of letters from dictionary
def get_sorted_letter_count(letter_count):
    res = [ ]
    for letter, count in letter_count.items():
        res.append({"char": letter, "num": count})
    res.sort(reverse=True, key=lambda x: x["num"])
    return res