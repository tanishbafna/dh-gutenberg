import os
from tqdm import tqdm
import zipfile

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

FILE = 'corpus/'

def downloadFunc(corpusContent):

    failed = list()

    for key, values in tqdm(corpusContent.items()):

        text = strip_headers(load_etext(values)).strip()
        
        if 'html' in text:
            failed.append(key)
            continue

        with open(FILE + key + '.txt', 'w') as file:
            file.write(text)
        
        text = None
    
    if len(failed) == 0:
        return None
    else:
        string = '\n'.join(failed)
        return 'Failed:\n' + string

def zipFunc(path):

    zipf = zipfile.ZipFile('corpus.zip', 'w', zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(path):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))

    return True

print(downloadFunc(bookList))
zipFunc(FILE)
