try:  
    text = input("Enter the text: ")
    num_sentences = text.count('.') + text.count('!') + text.count('?')
    print(f"Number of sentences in the text: {num_sentences}")
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')