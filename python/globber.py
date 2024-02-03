import glob
for f in glob.glob('/path/**/*.c', recursive=True):
    print(f)

from pathlib import Path

for path in Path('src').rglob('*.c'):
    print(path.name)

for i, path in enumerate(Path('src').rglob('*.png')):
    print(path.name)

import os

for fo in os.scandir("path"):
    fo.
