def is_palindrome(sentence):
    # Normalize the string: remove spaces and make lowercase
    cleaned_sentence = sentence.replace(" ", "").lower()
    # Compare the cleaned string to its reverse
    return cleaned_sentence == cleaned_sentence[::-1]
