# 00-1 How This Works

**Narrator:** The AI-Augmented Python DSA Learning Plan. Section zero, track one. How this works.

**Narrator:** This track is for the road. You don't need a screen. You don't need to take notes. Just listen.

*[pause 1s]*

**Narrator:** Here is the goal. You want to pass the coding part of a software engineering interview. In Python.

**Narrator:** That part comes in two forms. The first is an online assessment. A timed test. LeetCode, Codility, HackerRank. Nobody watches you. A machine grades you.

**Narrator:** The second is a live round. A person watches you solve a problem. They ask questions while you work.

**Narrator:** This course trains for both.

*[pause 1s]*

**Narrator:** Let's start with the machine. What does it grade?

**Narrator:** Two things. Correctness, and performance.

**Narrator:** Correctness means your function gives the right answer. On every input. Not just the examples you can see. The grader runs hidden tests. An empty list. A list with one item. All the same number. Negative numbers. And the biggest input the problem allows.

**Narrator:** Performance means your code is fast enough on that biggest input. Often a hundred thousand items or more.

**Narrator:** Here's the trap. Most beginners only practice correctness. They write code that works on the small examples. Then the big hidden test runs, and it times out.

**Narrator:** Codility is blunt about this. It gives you two scores. One for correctness. One for performance. A slow answer can get a hundred on the first and a zero on the second.

**Narrator:** So every lab in this course runs a big input with a timer. You'll see the word SLOW when your code is correct but too slow. That's a real failure. Treat it like one.

*[pause 1s]*

**Narrator:** Next. Return, don't print.

**Narrator:** The grader calls your function and looks at what comes back. It doesn't read your screen.

**Narrator:** If you print the answer, the function gives back nothing. In Python, nothing is called None. The grader sees None, and marks you wrong.

**Narrator:** Some problems say: change the list in place, and return nothing. Then you edit the list you were given. The grader checks that list after your function finishes.

**Narrator:** How do you know which one you need? Read the function signature. The little arrow at the end of the first line tells you what comes back. If it says None, you change the input in place.

**Narrator:** This is mistake M six in your log. Not reading the return type. The fix is simple. Before you plan anything, write down: returns, and then what it returns.

*[pause 1s]*

**Narrator:** Now the live round. A person watches. What are they grading?

**Narrator:** Four things. Communication. Problem solving. Code quality. And testing.

**Narrator:** Communication means you talk while you think. You restate the problem. You ask what happens with an empty input. You say, the simple way is this, and it's too slow because of that.

**Narrator:** Problem solving means you find something that works, then you make it better.

**Narrator:** Code quality means clean Python. Good variable names.

**Narrator:** Testing means you walk through your own code with a small example. Out loud. And you catch your own bugs before they do.

**Narrator:** In twenty twenty six, big companies still run these rounds with AI turned off. Many also run a debug round. They hand you broken code and watch you fix it. That's why each section has a Bug Hunt lab.

*[pause 1s]*

**Narrator:** Now, how this course works.

**Narrator:** Each section follows the same eight steps.

**Narrator:** One. Prime. You listen to the audio primer before you read anything. Like this track. It plants the words in your head so the reading goes faster.

**Narrator:** Two. Learn. You read the lesson with your editor open. You type every example. Typing matters. Your fingers need the reps.

**Narrator:** Three. Build. You do the labs. They come in tiers. Core is easy. Build is medium. Stretch is hard. Plus one Bug Hunt.

**Narrator:** Four. Drill. Flashcards in Anki. Every day. Five to twenty minutes. On breaks.

**Narrator:** Five. Explain. A question and answer session with Claude. You explain. It asks why. It catches fuzzy thinking.

**Narrator:** Six. Test. A short quiz that scores you by topic. It tells you where you're weak.

**Narrator:** Seven. Repair. You fix the weak spots. You log any mistake you've made twice. It becomes a flashcard.

**Narrator:** Eight. Gate. Two days later, you solve problems from a blank file. Timed. No notes. Pass, and you move on.

*[pause 1s]*

**Narrator:** Why so many steps? Because of how memory works.

**Narrator:** Reading something feels like learning. It mostly isn't. What builds memory is pulling the answer out of your own head. That's called retrieval practice. Flashcards, quizzes, and blank-file solves are all retrieval.

**Narrator:** Spacing helps too. Short sessions over many days beat one long session. Anki handles the spacing for you.

**Narrator:** And mixing helps. When problems are mixed up, you learn to pick the right tool. Not just use the tool the chapter told you to use.

**Narrator:** One more. When a problem is hard, struggle a little before you look for help. Not forever. About fifteen minutes on an easy one. Then open one hint. Just one.

*[pause 1s]*

**Narrator:** Let's talk about the hint ladder.

**Narrator:** Every problem has three hints. Hint one asks you a question. Hint two names the pattern. Hint three gives you pseudocode.

**Narrator:** Open them one at a time. Try for ten more minutes after each one.

**Narrator:** If you needed hint three, mark the problem as assisted. It comes back later for a cold solve.

**Narrator:** Full solutions live in a separate folder. Open them after you solve the problem. Or after a real fight. Never before.

*[pause 1s]*

**Narrator:** Last thing. The problem routine. You'll hear this many times. Here it is once, slowly.

**Narrator:** Restate the problem in your own words. And say what it returns.

**Narrator:** Work one example by hand. On paper.

**Narrator:** List the edge cases. Empty. One item. All the same. Negatives. Huge.

**Narrator:** Say the brute force, and say how slow it is.

**Narrator:** Find the pattern that cuts out the repeated work.

**Narrator:** Then code it.

**Narrator:** Then test it. By tracing. Line by line. Before you hit run.

*[pause 1s]*

**Narrator:** That's the whole system. Next track, Big O. How to tell if your code is fast enough, before you ever run it.
