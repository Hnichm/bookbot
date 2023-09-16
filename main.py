def get_book_text(path):
  with open(path) as f:
    file_contents = f.read()
    return file_contents
  
def get_num_words(text):
  words = text.split()
  return len(words)

def get_chars_dict(text):
  chars = {}
  for c in text:
    lowered = c.lower()
    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1
  return chars




file_contents = get_book_text("books/frankenstein.txt")
print(get_num_words(file_contents))
print(get_chars_dict(file_contents))


