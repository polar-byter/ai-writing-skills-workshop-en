"""Rebuild maintainer-owned starters with stable cross-platform text bytes."""
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
TEXT = {'.md', '.js', '.html', '.json', '.csv', '.txt', '.yaml', '.yml'}


def package(folder, destination):
    assert folder.resolve().is_relative_to(ROOT)
    for path in folder.rglob('*'):
        if path.is_file() and path.suffix in TEXT:
            path.write_bytes(path.read_bytes().replace(b'\r\n', b'\n'))
    with ZipFile(destination, 'w', ZIP_DEFLATED) as archive:
        for path in sorted(folder.rglob('*')):
            if path.is_file() and '__pycache__' not in path.parts:
                archive.write(path, (Path(folder.name) / path.relative_to(folder)).as_posix())


def main():
    stages = json.loads((ROOT / 'tools/workshop-map.json').read_text(encoding='utf-8'))
    for stage in stages:
        package(ROOT / 'exercises' / stage['root'], ROOT / 'downloads' / (stage['root'] + '.zip'))
    package(ROOT / 'skill/write-clear-english', ROOT / 'downloads/write-clear-english.zip')
    print('Rebuilt seven starters and the ready skill with LF text bytes.')


if __name__ == '__main__':
    main()
