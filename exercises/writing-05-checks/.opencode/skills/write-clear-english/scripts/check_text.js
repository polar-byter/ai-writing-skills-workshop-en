// One deterministic punctuation check shared by the browser and Node CLI.
function findUnusualPunctuation(text) {
  const findings = [];
  const lines = text.split(/\r\n|\n|\r/);
  for (let index = 0; index < lines.length; index += 1) {
    let column = 0;
    for (const character of lines[index]) {
      column += 1;
      const code = character.codePointAt(0);
      if (code > 127 && /[\p{P}\p{S}\p{Z}]/u.test(character)) {
        findings.push({line: index + 1, column, codepoint: 'U+' + code.toString(16).toUpperCase().padStart(4, '0')});
      }
    }
  }
  return findings;
}

function formatFinding(finding) {
  return 'Line ' + finding.line + ', column ' + finding.column + ': ' + finding.codepoint;
}

if (typeof document !== 'undefined') {
  const editor = document.getElementById('text');
  const results = document.getElementById('results');
  const status = document.getElementById('status');
  document.getElementById('file').addEventListener('change', async (event) => {
    const file = event.target.files[0];
    if (file) { editor.value = await file.text(); status.textContent = 'File opened. Click Check.'; results.replaceChildren(); }
  });
  document.getElementById('check').addEventListener('click', () => {
    const findings = findUnusualPunctuation(editor.value);
    results.replaceChildren();
    for (const finding of findings) {
      const item = document.createElement('li');
      item.textContent = formatFinding(finding);
      results.appendChild(item);
    }
    status.textContent = findings.length ? 'Unusual characters: ' + findings.length : 'No unusual characters found.';
  });
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = {findUnusualPunctuation, formatFinding};
  if (require.main === module) {
    const fs = require('node:fs');
    const paths = process.argv.slice(2);
    if (!paths.length) { console.error('Usage: node scripts/check_text.js article.md'); process.exitCode = 2; }
    else {
      try {
        let count = 0;
        for (const path of paths) {
          const findings = findUnusualPunctuation(fs.readFileSync(path, 'utf8'));
          for (const finding of findings) console.log(path + ': ' + formatFinding(finding));
          count += findings.length;
        }
        console.log('Files checked: ' + paths.length + '. Unusual characters: ' + count + '.');
        console.log('This does not assess meaning, clarity or factual accuracy. Files are unchanged.');
        process.exitCode = count ? 1 : 0;
      } catch (error) { console.error('Could not read file: ' + error.message); process.exitCode = 2; }
    }
  }
}
