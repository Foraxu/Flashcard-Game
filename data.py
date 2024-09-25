import pandas
import random

FRENCH_ENGLISH_DATA = 'data/french_words.csv'
ENGLISH_PORTUGUESE_DATA = 'data/english_words.csv'

df = pandas.read_csv(ENGLISH_PORTUGUESE_DATA)
df_rows = df.iterrows()

first_language_words = [i for i in df['English']]
df_dict = {y['English']:y['Portuguese'] for x, y in df_rows}

def get_random_word():
    return random.choice(first_language_words)

def remove_word(word):
    first_language_words.remove(word)
