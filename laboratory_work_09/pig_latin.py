def to_pig_latin(text):
    """Переводит текст в свиную латынь"""

    def convert_word(word):
        if not word or not word.isalpha():
            return word

        vowels = 'aeiouAEIOU'
        if word[0] in vowels:
            return word + "yay"
        else:
            return word[1:] + word[0] + "ay"

    return ' '.join(convert_word(word) for word in text.split())


def from_pig_latin(text):
    """Переводит из свиной латыни обратно"""

    def convert_back(word):
        if not word or not word.isalpha():
            return word

        word_lower = word.lower()
        if word_lower.endswith('yay'):
            return word[:-3]
        elif word_lower.endswith('ay'):
            return word[-3] + word[:-3]
        return word

    return ' '.join(convert_back(word) for word in text.split())