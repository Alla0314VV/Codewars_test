import codewars_test as test

def duplicate_count(text):
    text = text.lower()
    counts = {}
    duplicates = 0
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for count in counts.values():
        if count > 1:
            duplicates += 1
    return duplicates
