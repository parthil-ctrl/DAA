
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Student Sorting - DAA Project</title>

<style>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: #f1f5f9;
  color: #183047;
}

header {
  background: linear-gradient(120deg, #102a43, #0f766e);
  color: white;
  padding: 45px 20px;
  text-align: center;
}

header h1 {
  margin: 10px 0;
  font-size: 42px;
}

header p {
  line-height: 1.6;
}

main {
  max-width: 1050px;
  margin: 25px auto;
  padding: 0 15px;
}

.stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 15px;
}

.stat, .panel {
  background: white;
  padding: 20px;
  border-radius: 14px;
  box-shadow: 0 4px 15px #00000010;
  margin-bottom: 18px;
}

.stat strong {
  display: block;
  font-size: 26px;
  color: #0f9f91;
  margin-bottom: 5px;
}

.layout {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 18px;
  margin-top: 18px;
}

.controls {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin: 18px 0;
}

select, button {
  padding: 11px;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  font-size: 14px;
}

select {
  flex: 1;
  min-width: 130px;
}

button {
  cursor: pointer;
  font-weight: bold;
}

.primary {
  background: #0f9f91;
  color: white;
  border: none;
}

.secondary {
  background: white;
  color: #183047;
}

button:hover {
  opacity: 0.85;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 15px;
}

th, td {
  text-align: left;
  padding: 12px 7px;
  border-bottom: 1px solid #e2e8f0;
}

th {
  font-size: 12px;
  color: #64748b;
}

.marks {
  color: #0f9f91;
  font-weight: bold;
}

.badge {
  background: #d9f7ef;
  color: #08786e;
  border-radius: 20px;
  padding: 5px 8px;
  font-size: 12px;
}

.muted {
  color: #64748b;
  line-height: 1.6;
  font-size: 14px;
}

.steps li {
  margin: 15px 0;
  line-height: 1.5;
}

.code {
  background: #101c2d;
  color: #d8e8fa;
  padding: 15px;
  border-radius: 10px;
  overflow-x: auto;
  white-space: pre;
  font: 12px/1.7 monospace;
}

footer {
  text-align: center;
  padding: 20px;
  color: #64748b;
}

@media (max-width: 750px) {
  .layout {
    grid-template-columns: 1fr;
  }

  .stats {
    gap: 8px;
  }

  .stat {
    padding: 12px;
  }

  .stat strong {
    font-size: 20px;
  }

  header h1 {
    font-size: 32px;
  }

  .panel {
    overflow-x: auto;
  }
}
</style>
</head>

<body>

<header>
  <p>DESIGN & ANALYSIS OF ALGORITHMS</p>
  <h1>Student Sorting</h1>
  <p>Sort student records using the Bubble Sort algorithm.</p>
</header>

<main>

  <section class="stats">
    <div class="stat">
      <strong id="count">5</strong>
      Student Records
    </div>
    <div class="stat">
      <strong>O(n²)</strong>
      Average/Worst Time
    </div>
    <div class="stat">
      <strong>O(1)</strong>
      Auxiliary Space
    </div>
  </section>

  <div class="layout">

    <section class="panel">
      <h2>Student Records</h2>
      <p class="muted">
        Select a sorting key and order, then run Bubble Sort.
      </p>

      <div class="controls">
        <select id="sortKey" aria-label="Sort key">
          <option value="marks">Sort by Marks</option>
          <option value="name">Sort by Name</option>
          <option value="rollNo">Sort by Roll Number</option>
        </select>

        <select id="sortOrder" aria-label="Sort order">
          <option value="desc">Descending</option>
          <option value="asc">Ascending</option>
        </select>

        <button class="primary" id="sortBtn">
          Run Bubble Sort
        </button>

        <button class="secondary" id="resetBtn">
          Reset
        </button>
      </div>

      <p class="muted" id="status" aria-live="polite">
        Ready to sort.
      </p>

      <table>
        <thead>
          <tr>
            <th>Roll No.</th>
            <th>Name</th>
            <th>Marks</th>
            <th>Position</th>
          </tr>
        </thead>
        <tbody id="studentRows"></tbody>
      </table>
    </section>

    <aside class="panel">
      <h2>How Bubble Sort Works</h2>
      <p class="muted">
        Bubble Sort compares adjacent elements and swaps them
        when they are in the wrong order.
      </p>

      <ol class="steps">
        <li>Start from the first student.</li>
        <li>Compare two adjacent student records.</li>
        <li>Swap them if they are in the wrong order.</li>
        <li>Repeat until the records are sorted.</li>
      </ol>

      <h3>Time Complexity</h3>
      <p>Best case: O(n), with early stopping</p>
      <p>Average case: O(n²)</p>
      <p>Worst case: O(n²)</p>
      <p>Space complexity: O(1)</p>

      <h3>Pseudocode</h3>
      <div class="code">for i = 0 to n - 2
  for j = 0 to n - i - 2
    if elements are out of order
      swap elements</div>
    </aside>

  </div>

  <section class="panel">
    <h2>C++ Source Code</h2>
    <p class="muted">
      Bubble Sort implementation for sorting students by marks.
    </p>

    <div class="code" id="cppCode">#include &lt;iostream&gt;
#include &lt;vector&gt;
#include &lt;string&gt;
#include &lt;algorithm&gt;
using namespace std;

struct Student {
    int rollNo;
    string name;
    int marks;
};

int main() {
    vector&lt;Student&gt; students = {
        {101, "Aarav", 72},
        {102, "Diya", 91},
        {103, "Kabir", 65},
        {104, "Meera", 84},
        {105, "Ishaan", 78}
    };

    int n = students.size();

    for (int i = 0; i &lt; n - 1; i++) {
        bool swapped = false;

        for (int j = 0; j &lt; n - i - 1; j++) {
            if (students[j].marks &lt; students[j + 1].marks) {
                swap(students[j], students[j + 1]);
                swapped = true;
            }
        }

        if (!swapped) break;
    }

    for (const Student&amp; s : students) {
        cout &lt;&lt; s.rollNo &lt;&lt; " "
             &lt;&lt; s.name &lt;&lt; " "
             &lt;&lt; s.marks &lt;&lt; endl;
    }

    return 0;
}</div>

    <button class="primary" id="copyBtn" style="margin-top:12px">
      Copy C++ Code
    </button>
  </section>

</main>

<footer>
  DAA Mini Project | Student Sorting with Bubble Sort
</footer>

<script>
const originalStudents = [
  { rollNo: 101, name: "Aarav", marks: 72 },
  { rollNo: 102, name: "Diya", marks: 91 },
  { rollNo: 103, name: "Kabir", marks: 65 },
  { rollNo: 104, name: "Meera", marks: 84 },
  { rollNo: 105, name: "Ishaan", marks: 78 }
];

let students = originalStudents.map(s => ({ ...s }));

const rows = document.getElementById("studentRows");
const status = document.getElementById("status");

function renderStudents() {
  rows.innerHTML = "";

  students.forEach((student, index) => {
    const tr = document.createElement("tr");

    const values = [
      student.rollNo,
      student.name,
      student.marks,
      "#" + (index + 1)
    ];

    values.forEach((value, i) => {
      const td = document.createElement("td");
      td.textContent = value;

      if (i === 1) td.style.fontWeight = "bold";
      if (i === 2) td.className = "marks";
      if (i === 3) {
        const badge = document.createElement("span");
        badge.className = "badge";
        badge.textContent = value;
        td.textContent = "";
        td.appendChild(badge);
      }

      tr.appendChild(td);
    });

    rows.appendChild(tr);
  });

  document.getElementById("count").textContent = students.length;
}

function compare(a, b, key) {
  if (key === "name") {
    return a.name.localeCompare(b.name);
  }

  return a[key] - b[key];
}

document.getElementById("sortBtn").addEventListener("click", () => {
  const key = document.getElementById("sortKey").value;
  const order = document.getElementById("sortOrder").value;
  let swaps = 0;

  for (let i = 0; i < students.length - 1; i++) {
    let swapped = false;

    for (let j = 0; j < students.length - i - 1; j++) {
      const result = compare(students[j], students[j + 1], key);
      const wrongOrder = order === "asc"
        ? result > 0
        : result < 0;

      if (wrongOrder) {
        [students[j], students[j + 1]] =
          [students[j + 1], students[j]];

        swapped = true;
        swaps++;
      }
    }

    if (!swapped) break;
  }

  renderStudents();

  const labels = {
    marks: "marks",
    name: "name",
    rollNo: "roll number"
  };

  status.textContent =
    "Sorted by " + labels[key] + " (" + order +
    "). Swaps performed: " + swaps + ".";
});

document.getElementById("resetBtn").addEventListener("click", () => {
  students = originalStudents.map(s => ({ ...s }));
  renderStudents();
  status.textContent = "Reset complete. Original order restored.";
});

document.getElementById("copyBtn").addEventListener("click", async () => {
  const code = document.getElementById("cppCode").innerText;
  const button = document.getElementById("copyBtn");

  try {
    await navigator.clipboard.writeText(code);
    button.textContent = "Copied!";
  } catch (error) {
    const range = document.createRange();
    range.selectNodeContents(document.getElementById("cppCode"));

    const selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);

    button.textContent = "Code selected - press Ctrl+C";
  }

  setTimeout(() => {
    button.textContent = "Copy C++ Code";
  }, 2000);
});

renderStudents();
</script>

</body>
</html>
