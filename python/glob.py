import glob
for f in glob.glob('/path/**/*.c', recursive=True):
    print(f)

from pathlib import Path

for path in Path('src').rglob('*.c'):
    print(path.name)
