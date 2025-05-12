import codewars_test as test

def get_count(sentence):
    """
    Возвращает количество гласных в заданной строке (a, e, i, o, u).
    """
    vowels = "aeiou"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

