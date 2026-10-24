// Hints for phrases that often make English text sound machine-written.
// A hint is a place to reread, not a verdict: the editor decides whether the phrase is justified.

function word(source, flags = 'gi') {
  return new RegExp('\\b(?:' + source + ')\\b', flags);
}

const PATTERNS = [
  [word("it(?:'s| is) (?:worth noting|important to note|worth mentioning)|needless to say|it goes without saying"), 'throat-clearing: state the point directly'],
  [word('delve|leverage|seamless(?:ly)?|robust|pivotal|tapestry|testament to|embark|foster|elevate|game-changer|unlock the (?:full )?potential|navigat(?:e|ing) the complexit(?:y|ies)'), 'overused stock word'],
  [word("in today's (?:fast-paced |digital )?world|in the (?:modern|digital) (?:era|age)|let's dive in|let us dive in|in this article,? we will explore"), 'generic opening: start with an event or data'],
  [word('in conclusion|to sum up|in summary|all in all|at the end of the day'), 'summary ending: return to the example instead'],
  [word("(?:is|are|was|were)n't just|is not just|not only [^.!?]{1,60} but also|it's not about"), '"not just X, but Y": check that these do not pile up'],
  [word('does not (?:guarantee|prove|mean)|is not a (?:guarantee|proof)|not a recorded|results may vary'), 'caveat: is it needed here, or already said once'],
  [word('moreover|furthermore|additionally'), 'connector: check whether the sentences really need it'],
  [word('honest (?:answer|result)|the (?:function|program|model) (?:wants|tries|thinks|believes)'), 'treating the program as a person'],
  [word("the (?:author|owner) (?:asked|clarified|requested|wanted|approved|rejected|noted)|at the (?:author|owner)'s request|per the (?:author|owner)"), 'maintainer text written by an assistant: write impersonally or in the first person'],
  [word('from the (?:chat|dialogue|conversation)|(?:in|for) the next session'), 'trace of a conversation with a model'],
  [word('(?:humans|people|users|individuals) (?:usually|typically|tend to|often)'), 'looking at people from outside'],
];

function findStyleHints(text) {
  const hints = [];
  const lines = text.split(/\r\n|\n|\r/);
  let inCode = false;
  for (let index = 0; index < lines.length; index += 1) {
    const line = lines[index];
    if (/^\s*(?:>\s*)?```/.test(line)) {
      inCode = !inCode;
      continue;
    }
    if (inCode) continue;
    for (const [pattern, message] of PATTERNS) {
      pattern.lastIndex = 0;
      let match;
      while ((match = pattern.exec(line)) !== null) {
        hints.push({line: index + 1, column: match.index + 1, phrase: match[0], message});
      }
    }
  }
  return hints;
}

function formatHint(hint) {
  return 'Line ' + hint.line + ', column ' + hint.column + ': "' + hint.phrase + '" - ' + hint.message;
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = {findStyleHints, formatHint};
  if (require.main === module) {
    const fs = require('node:fs');
    const paths = process.argv.slice(2);
    if (!paths.length) {
      console.error('Pass a Markdown file: node scripts/check_style.js article.md');
      process.exitCode = 2;
    } else {
      try {
        let count = 0;
        for (const path of paths) {
          const hints = findStyleHints(fs.readFileSync(path, 'utf8'));
          for (const hint of hints) console.log(path + ': ' + formatHint(hint));
          count += hints.length;
        }
        console.log('Files checked: ' + paths.length + '. Places to reread: ' + count + '.');
        console.log('These are hints, not errors: the editor decides about each phrase. Files are not changed.');
        process.exitCode = count ? 1 : 0;
      } catch (error) {
        console.error('Could not read the file: ' + error.message);
        process.exitCode = 2;
      }
    }
  }
}
