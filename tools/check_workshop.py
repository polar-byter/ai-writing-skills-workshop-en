"""Check navigation, independent stages, the ready package and the shared checker."""
import ast
import hashlib
import json
from pathlib import Path
import re
import shutil
import struct
import subprocess
import tempfile
import unicodedata
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]


def check_links(path, text):
    links = re.findall(r'\[[^\]]*\]\(([^)]+)\)', text) + re.findall(r'(?:src|href)="([^"]+)"', text)
    for link in links:
        url = urlsplit(link)
        if url.scheme or url.netloc or not url.path:
            continue
        target = (path.parent / unquote(url.path)).resolve()
        assert target.is_relative_to(ROOT) and target.exists(), (path, link)
    return len(links)


def check_archive(archive_path, folder):
    expected = {(Path(folder.name) / path.relative_to(folder)).as_posix(): path.read_bytes()
                for path in folder.rglob('*') if path.is_file() and '__pycache__' not in path.parts}
    with ZipFile(archive_path) as archive:
        assert archive.testzip() is None, archive_path
        assert set(archive.namelist()) == set(expected), archive_path
        for name, data in expected.items():
            assert archive.read(name) == data, (archive_path, name)


def main():
    manifest = json.loads((ROOT / 'tools/workshop-map.json').read_text(encoding='utf-8'))
    assert len(manifest) == 7
    links, text_files = 0, 0
    for path in ROOT.rglob('*'):
        if not path.is_file() or any(part in ('.git', '.checks', '__pycache__', '.venv') for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix in ('.md', '.py', '.js', '.json', '.html', '.yaml', '.yml', '.txt', '.csv'):
            text = path.read_text(encoding='utf-8')
            assert not re.search('[\u0400-\u04ff]', text), path
            text_files += 1
            if path.suffix in ('.md', '.html'):
                links += check_links(path, text)
            if path.suffix == '.md':
                assert text.count('```') % 2 == 0, path
                assert not any(ord(char) > 127 and unicodedata.category(char)[0] in 'PSZ' for char in text), path
            if path.suffix == '.py':
                ast.parse(text, filename=str(path))
        if path.suffix in ('.gif', '.png'):
            data = path.read_bytes()
            width = struct.unpack('<H', data[6:8])[0] if path.suffix == '.gif' else struct.unpack('>I', data[16:20])[0]
            assert width == 480, (path, width)
    assert len(list((ROOT / 'assets').glob('*.gif'))) == 9
    for path in (ROOT / 'assets').glob('*.gif'):
        assert path.with_suffix('.png').is_file(), path
    for stage in manifest:
        folder = ROOT / 'exercises' / stage['root']
        check_archive(ROOT / 'downloads' / (stage['root'] + '.zip'), folder)
        skill = folder / '.opencode/skills/write-clear-english/SKILL.md'
        assert skill.exists() == (stage['number'] >= 2), folder
        if stage['number'] in (2, 3, 4, 5):
            assert '<!--' in skill.read_text(encoding='utf-8'), skill
        if stage['number'] == 6:
            assert '<!--' not in skill.read_text(encoding='utf-8'), skill
        if stage['number'] >= 5:
            reference = ROOT / 'skill/write-clear-english/scripts/check_text.js'
            assert (skill.parent / 'scripts/check_text.js').read_bytes() == reference.read_bytes()
    check_archive(ROOT / 'downloads/write-clear-english.zip', ROOT / 'skill/write-clear-english')
    node = shutil.which('node')
    if node:
        script = ROOT / 'skill/write-clear-english/scripts/check_text.js'
        program = '''const assert = require('node:assert/strict');
const check = require(process.argv[1]);
assert.equal(check.findUnusualPunctuation('Plain "text" -> result...').length, 0);
assert.deepEqual(check.findUnusualPunctuation('a\\n' + String.fromCodePoint(0x2014)), [{line:2,column:1,codepoint:'U+2014'}]);
assert.equal(check.findUnusualPunctuation('caf' + String.fromCodePoint(0xe9)).length, 0);
'''
        subprocess.run([node, '-e', program, str(script)], check=True)
        scratch = ROOT / '.checks'
        scratch.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=scratch) as directory:
            path = Path(directory) / 'sample.md'
            for value, code in [('Plain text.', 0), ('a' + chr(0x2014) + 'b', 1)]:
                path.write_text(value, encoding='utf-8')
                before = hashlib.sha256(path.read_bytes()).digest()
                result = subprocess.run([node, str(script), str(path)], capture_output=True)
                assert result.returncode == code, result.stderr
                assert hashlib.sha256(path.read_bytes()).digest() == before
            assert subprocess.run([node, str(script)], capture_output=True).returncode == 2
            assert subprocess.run([node, str(script), str(path.with_name('absent.md'))], capture_output=True).returncode == 2
        print('Node checker function and CLI cases passed; inputs unchanged.')
    else:
        print('Node unavailable: checker execution not tested on this host.')
    print(f'Checked {text_files} English text files, {links} links, seven starters, ready skill ZIP and nine GIF/PNG pairs.')
    print('No live OpenCode or model comparison was performed by this check.')


if __name__ == '__main__':
    main()
