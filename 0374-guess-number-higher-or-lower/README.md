<div align="center">

# 🧩 374 · Guess Number Higher or Lower

### A clear solution, a reusable pattern, and a lesson worth remembering.

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem-FFA116?style=flat-square&logo=leetcode&logoColor=white)](https://leetcode.com/problems/guess-number-higher-or-lower) [![Topic](https://img.shields.io/badge/Topic-Binary%20Search-0F766E?style=flat-square)](#-pattern-recognition) [![Language](https://img.shields.io/badge/Language-Python3-2563EB?style=flat-square)](#-solution)

**Difficulty:** Easy · **Status:** Solved

</div>

---

## 🎯 Problem summary

<h2><a href="https://leetcode.com/problems/guess-number-higher-or-lower">374. Guess Number Higher or Lower</a></h2><h3>Easy</h3><hr><p>We are playing the Guess Game. The game is as follows:</p>

<p>I pick a number from <code>1</code> to <code>n</code>. You have to guess which number I picked (the number I picked stays the same throughout the game).</p>

<p>Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.</p>

<p>You call a pre-defined API <code>int guess(int num)</code>, which returns three possible results:</p>

<ul>
	<li><code>-1</code>: Your guess is higher than the number I picked (i.e. <code>num &gt; pick</code>).</li>
	<li><code>1</code>: Your guess is lower than the number I picked (i.e. <code>num &lt; pick</code>).</li>
	<li><code>0</code>: your guess is equal to the number I picked (i.e. <code>num == pick</code>).</li>
</ul>

<p>Return <em>the number that I picked</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 10, pick = 6
<strong>Output:</strong> 6
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1, pick = 1
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 2, pick = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>1 &lt;= pick &lt;= n</code></li>
</ul>


### Given, return & examples

Use the original problem statement above as the source of truth. Add a representative example and the key constraints when reviewing this question.

## 📌 Constraints

- Add the constraints that influence the approach.
- Record any sortedness, uniqueness, or range guarantees.
- Explain what they tell you about a practical solution.

---

## 🧭 Pattern recognition

### Primary pattern: **Binary Search**

**Related topics:** `Binary Search` `Interactive`

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
| Submitted | 10/30/2026, 1:29:34 PM |
| Language | Python3 |
| Runtime | 45 ms · Beats 54.39% |
| Memory | 19.2 MB · Beats 60.89% |
| Runtime percentile | 54.39% |
| Memory percentile | 60.89% |

> Performance values come from this accepted submission and can vary between runs.

### My solution

```python3
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        left = 1
        right = n

        while right >= left:
            #this is our guess
            mid = left + (right - left ) // 2
            #call api for answer 
            guessAnswer = guess(mid)
            if guessAnswer == 0:
                return mid
            elif guessAnswer == -1:
                right = mid -1
            else:
                left = mid+1 
        return  -1 

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

- **Pattern:** Binary Search
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
