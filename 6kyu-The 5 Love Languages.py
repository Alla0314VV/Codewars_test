from preloaded import LOVE_LANGUAGES
import random

def love_language(partner, weeks):
    """
    Finds the partner's primary love language.

    Args:
        partner: A Partner instance (with a response method).
        weeks: The number of weeks to try.

    Returns:
        The most likely love language of the partner (a string).
    """

    records = {lang: 0 for lang in LOVE_LANGUAGES}
    tries = 7 * weeks

    for _ in range(tries):
        love_language = random.choice(LOVE_LANGUAGES)
        response = partner.response(love_language)

        if response == "positive":
            records[love_language] += 1
        elif response == "neutral":
            pass
        else:
            records[love_language] -= 1 #Reduce from 1.

    best_language = max(records, key=records.get)

    return best_language
