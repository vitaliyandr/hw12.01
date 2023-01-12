try:
    text = input("Enter the text: ")
    reserved_words = input("Enter a list of reserved words separated by commas: ").split(',')
    for word in text.split():
        if word.lower() in reserved_words:
            text = text.replace(word, word.upper())
    print(text)
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')