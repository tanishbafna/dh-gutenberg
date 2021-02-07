import os
from tqdm import tqdm

os.environ['GUTENBERG_MIRROR'] = "http://www.gutenberg.org/dirs/"

from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

# Book Title: Ebook Number
bookList = {
    'Ulysses': 4300, 
    'Fanny Hill Memoirs of a Woman of Pleasure': 20028,
    'Women in Love': 4240,
    'Madame Bovary': 2413
}

for key, values in tqdm(bookList.items()):

    text = strip_headers(load_etext(values)).strip()
    
    if 'html' in text:
        print(f'Failed: {key}')
        continue

    with open(key + '.txt', 'w') as file:
        file.write(text)
    
    text = None