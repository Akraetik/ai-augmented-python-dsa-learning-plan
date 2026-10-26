"""
build_quiz.py — turn a section's quiz/quiz_data.py into:
  quiz/quiz.html          self-scoring quiz, opens in any browser, works offline
  quiz/quiz.md            the questions, for reading on a phone or printing
  quiz/quiz_answers.md    answer key with explanations

Usage:  python tools/build_quiz.py sections/01-array-string
"""
import html
import importlib.util
import json
import pathlib
import sys


def load(path):
    spec = importlib.util.spec_from_file_location("quiz_data", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


PAGE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<style>
:root{--bg:#f7f6f2;--card:#fff;--ink:#1d1d1b;--mut:#6b6a65;--line:#e3e1da;--acc:#2f5d8a;--ok:#2e7d4f;--bad:#b3412f;--code:#f0eee8}
@media (prefers-color-scheme:dark){:root{--bg:#141412;--card:#1d1d1b;--ink:#ecebe6;--mut:#9c9a93;--line:#33322e;--acc:#7fb0e0;--ok:#6cc58f;--bad:#ec8a78;--code:#262522}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 system-ui,-apple-system,Segoe UI,sans-serif}
main{max-width:760px;margin:0 auto;padding:24px 16px 80px}
h1{font-size:1.5rem;margin:0 0 4px}.sub{color:var(--mut);margin:0 0 24px}
.q{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px;margin:0 0 14px}
.qh{display:flex;justify-content:space-between;gap:8px;color:var(--mut);font-size:.8rem;text-transform:uppercase;letter-spacing:.04em}
.qt{font-weight:600;margin:6px 0 10px}
pre{background:var(--code);border-radius:6px;padding:10px 12px;overflow-x:auto;font:14px/1.45 ui-monospace,Consolas,monospace;margin:0 0 10px}
label{display:block;padding:8px 10px;border:1px solid var(--line);border-radius:6px;margin:6px 0;cursor:pointer}
label:hover{border-color:var(--acc)}input{margin-right:8px}
label.right{border-color:var(--ok);background:color-mix(in srgb,var(--ok) 12%,transparent)}
label.wrong{border-color:var(--bad);background:color-mix(in srgb,var(--bad) 12%,transparent)}
.why{display:none;margin-top:10px;padding:10px;border-left:3px solid var(--acc);background:var(--code);border-radius:4px;font-size:.95rem}
.done .why{display:block}
.study{margin-top:8px;padding-top:8px;border-top:1px dashed var(--line);font-size:.9rem;color:var(--mut)}
.study b{color:var(--ink)}
ol.miss li{margin:4px 0}
button{font:inherit;padding:10px 18px;border-radius:8px;border:1px solid var(--acc);background:var(--acc);color:var(--bg);cursor:pointer;margin:4px 8px 4px 0}
button.ghost{background:transparent;color:var(--acc)}
#result{display:none;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px;margin:0 0 20px}
.bar{height:10px;background:var(--line);border-radius:5px;overflow:hidden;margin:4px 0 10px}.bar i{display:block;height:100%}
.row{display:flex;justify-content:space-between;font-size:.95rem}
.big{font-size:2rem;font-weight:700}
code{font-family:ui-monospace,Consolas,monospace;background:var(--code);padding:1px 4px;border-radius:3px}
</style></head><body><main>
<h1>__TITLE__</h1><p class="sub">__SUB__</p>
<div id="result"></div>
<form id="f"></form>
<button id="submit">Score it</button><button class="ghost" id="reset">Start over</button>
</main>
<script>
const QUIZ = __DATA__;
const f = document.getElementById('f');
function esc(s){return s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]))}
function inline(s){return esc(s).replace(/`([^`]+)`/g,'<code>$1</code>')}
QUIZ.questions.forEach((q,i)=>{
  const d=document.createElement('div');d.className='q';d.id='q'+i;
  let h=`<div class="qh"><span>Q${i+1}</span><span>${esc(QUIZ.topics[q.topic]||q.topic)}</span></div><div class="qt">${inline(q.q)}</div>`;
  if(q.code) h+=`<pre>${esc(q.code)}</pre>`;
  q.options.forEach((o,j)=>{h+=`<label><input type="radio" name="q${i}" value="${j}">${inline(o)}</label>`});
  h+=`<div class="why">${inline(q.why)}${q.study?`<div class="study">If you missed it, study: <b>${inline(q.study)}</b></div>`:''}</div>`;d.innerHTML=h;f.appendChild(d);
});
document.getElementById('submit').onclick=()=>{
  let right=0;const per={};const missed=[];
  QUIZ.questions.forEach((q,i)=>{
    const d=document.getElementById('q'+i);d.classList.add('done');
    const pick=d.querySelector('input:checked');const labels=d.querySelectorAll('label');
    labels.forEach(l=>l.classList.remove('right','wrong'));
    labels[q.answer].classList.add('right');
    per[q.topic]=per[q.topic]||[0,0];per[q.topic][1]++;
    if(pick&&+pick.value===q.answer){right++;per[q.topic][0]++}
    else{if(pick)labels[+pick.value].classList.add('wrong');missed.push(i+1)}
  });
  const n=QUIZ.questions.length,pct=Math.round(100*right/n),pass=right/n>=QUIZ.pass_mark;
  let h=`<div class="big">${right}/${n} · ${pct}%</div><p>${pass?'<b style="color:var(--ok)">Gate passed.</b> '+QUIZ.pass_msg:'<b style="color:var(--bad)">Not yet.</b> '+QUIZ.fail_msg}</p><h3>By topic</h3>`;
  const weak=[];
  Object.entries(per).forEach(([t,[a,b]])=>{const p=a/b;if(p<0.8)weak.push(t);
    h+=`<div class="row"><span>${esc(QUIZ.topics[t]||t)}</span><span>${a}/${b}</span></div><div class="bar"><i style="width:${100*p}%;background:${p>=0.8?'var(--ok)':'var(--bad)'}"></i></div>`});
  if(weak.length){h+='<h3>Review these</h3><ul>'+weak.map(t=>`<li><b>${esc(QUIZ.topics[t]||t)}</b>: ${inline(QUIZ.review[t]||'')}</li>`).join('')+'</ul>'}
  if(missed.length){h+='<h3>Study list for your misses</h3><ol class="miss">'+missed.map(n=>{const q=QUIZ.questions[n-1];return `<li>Q${n}: ${inline(q.study||QUIZ.review[q.topic]||'')}</li>`}).join('')+'</ol>'}
  h+='<button id="copy">Copy results for Claude</button>';
  const r=document.getElementById('result');r.innerHTML=h;r.style.display='block';window.scrollTo(0,0);
  const summary=`${QUIZ.title}: ${right}/${n} (${pct}%). Weak topics: ${weak.map(t=>QUIZ.topics[t]).join(', ')||'none'}. Missed: ${missed.map(n=>'Q'+n+' ('+(QUIZ.questions[n-1].study||QUIZ.topics[QUIZ.questions[n-1].topic])+')').join('; ')||'none'}.`;
  document.getElementById('copy').onclick=()=>{navigator.clipboard&&navigator.clipboard.writeText(summary);document.getElementById('copy').textContent='Copied'};
  try{const k='quiz:'+QUIZ.title;const hist=JSON.parse(localStorage.getItem(k)||'[]');hist.push({when:new Date().toISOString(),right,n});localStorage.setItem(k,JSON.stringify(hist.slice(-20)))}catch(e){}
};
document.getElementById('reset').onclick=()=>{f.reset();document.querySelectorAll('.q').forEach(d=>{d.classList.remove('done');d.querySelectorAll('label').forEach(l=>l.classList.remove('right','wrong'))});document.getElementById('result').style.display='none';window.scrollTo(0,0)};
</script></body></html>"""


def main(section):
    section = pathlib.Path(section)
    qd = load(section / "quiz" / "quiz_data.py")
    data = {
        "title": qd.TITLE,
        "pass_mark": qd.PASS_MARK,
        "pass_msg": qd.PASS_MSG,
        "fail_msg": qd.FAIL_MSG,
        "topics": qd.TOPICS,
        "review": qd.REVIEW,
        "questions": qd.QUESTIONS,
    }
    for q in qd.QUESTIONS:
        assert 0 <= q["answer"] < len(q["options"]), q["id"]
        assert q["topic"] in qd.TOPICS, q["id"]
    sub = f"{len(qd.QUESTIONS)} questions · pass mark {int(qd.PASS_MARK * 100)}% · no notes, no IDE, no AI"
    page = (PAGE.replace("__TITLE__", html.escape(qd.TITLE)).replace("__SUB__", sub)
            .replace("__DATA__", json.dumps(data)))
    (section / "quiz" / "quiz.html").write_text(page, encoding="utf-8")

    letters = "ABCDEFG"
    md = [f"# {qd.TITLE}\n", f"{sub}. Answers: [quiz_answers.md](quiz_answers.md). "
          "Better: open `quiz.html` in a browser for instant scoring by topic.\n"]
    ans = [f"# {qd.TITLE} — Answer Key\n"]
    for i, q in enumerate(qd.QUESTIONS, 1):
        md.append(f"**{i}.** *({qd.TOPICS[q['topic']]})* {q['q']}\n")
        if q.get("code"):
            md.append("```python\n" + q["code"] + "\n```\n")
        for j, o in enumerate(q["options"]):
            md.append(f"- {letters[j]}. {o}")
        md.append("")
        study = f" *Study: {q['study']}.*" if q.get("study") else ""
        ans.append(f"**{i}. {letters[q['answer']]}** — {q['why']}{study}\n")
    ans.append("\n## If you missed a topic\n")
    for t, label in qd.TOPICS.items():
        ans.append(f"- **{label}:** {qd.REVIEW.get(t, '')}")
    (section / "quiz" / "quiz.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (section / "quiz" / "quiz_answers.md").write_text("\n".join(ans) + "\n", encoding="utf-8")
    print(f"built quiz: {len(qd.QUESTIONS)} questions")


if __name__ == "__main__":
    main(sys.argv[1])
