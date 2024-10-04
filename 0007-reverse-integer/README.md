<div align="center">

# 🧩 7 · Reverse Integer

### A clear solution, a reusable pattern, and a lesson worth remembering.

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem-FFA116?style=flat-square&logo=leetcode&logoColor=white)](https://leetcode.com/problems/reverse-integer/) [![Topic](https://img.shields.io/badge/Topic-Math-0F766E?style=flat-square)](#-pattern-recognition) [![Language](https://img.shields.io/badge/Language-C%2B%2B-2563EB?style=flat-square)](#-solution)

**Difficulty:** Medium · **Status:** Solved

</div>

---

## 🎯 Problem summary

<h2><a href="https://leetcode.com/problems/reverse-integer/">7. Reverse Integer</a></h2><h3>Medium</h3><hr><p>Given a signed 32-bit integer <code>x</code>, return <code>x</code><em> with its digits reversed</em>. If reversing <code>x</code> causes the value to go outside the signed 32-bit integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then return <code>0</code>.</p>

<p><strong>Assume the environment does not allow you to store 64-bit integers (signed or unsigned).</strong></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 123
<strong>Output:</strong> 321
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = -123
<strong>Output:</strong> -321
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 120
<strong>Output:</strong> 21
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


### Given, return & examples

Use the original problem statement above as the source of truth. Add a representative example and the key constraints when reviewing this question.

## 📌 Constraints

- Add the constraints that influence the approach.
- Record any sortedness, uniqueness, or range guarantees.
- Explain what they tell you about a practical solution.

---

## 🧭 Pattern recognition

### Primary pattern: **Math**

**Related topics:** `Math`

- Add the clue in the question that suggests this pattern.
- Add why this approach fits better than alternatives.

## 💡 Intuition

1. **Observation:** Add the key property.
2. **Key idea:** Explain what the algorithm does with it.
3. **Why it works:** Record the invariant or correctness argument.
4. **Stopping condition:** Record when it can safely return.

**Memory hook:** > Add a short phrase to recall this technique.

---

## 🪜 Approach

### Approach A — Brute force

Add a simple baseline only when it helps explain the optimized solution.

### Approach B — Accepted solution

Describe the repeated work or extra storage avoided by the submitted solution.

## 🧪 Dry run

| Step | Current state | Decision / action | Result |
|---:|---|---|---|
| 1 | Add a small example | Track relevant variables | Add outcome |

---

## 💻 Solution

### 🏆 Submission performance

| Metric | Details |
|---|---|
| Status | ✅ Accepted |
| Submitted | 10/4/2024, 5:09:59 PM |
| Language | C++ |
| Runtime | 0 ms · Beats 100.00% |
| Memory | 8.4 MB · Beats 97.85% |
| Runtime percentile | 100.00% |
| Memory percentile | 97.85% |

> Performance values come from this accepted submission and can vary between runs.

### My solution

```cpp
class Solution {
public:
    int reverse(int x) {

        long  rev = 0;
        while(true){
            if (x == 0) return rev;   
            int lastDigit = x % 10;
            x = (int) x/10;
            if ((rev * 10) <= INT_MIN ) return 0;
            if( (rev * 10) >= INT_MAX  ) return 0;
            rev = rev * 10 + lastDigit;
        }
    }
};
```

### Code walkthrough

| Code section | Purpose |
|---|---|
| Key variable / loop | Add why it is needed |
| Core operation | Add what it guarantees |
| Return condition | Add why the answer is correct |

---

## ⏱️ Complexity analysis

| Approach | Time complexity | Auxiliary space | Reason |
|---|---|---|---|
| Accepted solution | Add after review | Add after review | Base this on the submitted code |

## 🧯 Edge cases & validation

| Case | Expected behavior |
|---|---|
| Minimum valid input | Add result |
| Boundary or duplicate values | Add result |
| No-match / empty case, if allowed | Add result |

## ⚠️ Common mistakes

- Add the most likely off-by-one, duplicate-handling, or pointer-movement error.
- Add one high-value check before submitting.

## 🔁 Revision notes

<details open>
<summary><strong>30-second recap</strong></summary>

- **Pattern:** Math
- **Core idea:** Add one sentence after review.
- **Critical invariant:** Add what must remain true.
- **Complexity:** Add actual complexity.
- **Memory hook:** Add a recall phrase.

</details>

### Active recall

1. What clue suggests this pattern?
2. Why is the algorithm correct?
3. What are its time and auxiliary-space costs?
4. Which edge case is easiest to mishandle?

## 🔗 Related practice

Add only problems that genuinely reinforce the same pattern.

---

<div align="center">

**One problem. One pattern. One lesson retained.**

[← Back to CodeVault](https://github.com/sajeedkannoje/leetcode)

<sub>Made with ♥ by Sajeed Kannoje · CodeVault</sub>

</div>
