# Generador de archivos txt

import os

for folder in os.listdir():
    if folder.startswith('nombres'):
        os.remove(folder)