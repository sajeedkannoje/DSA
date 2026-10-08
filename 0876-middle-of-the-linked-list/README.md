<div align="center">

# 🧩 908 · Middle of the Linked List

### A clear solution, a reusable pattern, and a lesson worth remembering.

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem-FFA116?style=flat-square&logo=leetcode&logoColor=white)](https://leetcode.com/problems/middle-of-the-linked-list/) [![Topic](https://img.shields.io/badge/Topic-Linked%20List-0F766E?style=flat-square)](#-pattern-recognition) [![Language](https://img.shields.io/badge/Language-Python3-2563EB?style=flat-square)](#-solution)

**Difficulty:** Easy · **Status:** Solved

</div>

---

## 🎯 Problem summary

<h2><a href="https://leetcode.com/problems/middle-of-the-linked-list/">908. Middle of the Linked List</a></h2><h3>Easy</h3><hr><p>Given the <code>head</code> of a singly linked list, return <em>the middle node of the linked list</em>.</p>

<p>If there are two middle nodes, return <strong>the second middle</strong> node.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg" style="width: 544px; height: 65px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [3,4,5]
<strong>Explanation:</strong> The middle node of the list is node 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg" style="width: 664px; height: 65px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5,6]
<strong>Output:</strong> [4,5,6]
<strong>Explanation:</strong> Since the list has two middle nodes with values 3 and 4, we return the second one.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 100]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 100</code></li>
</ul>


### Given, return & examples

Use the original problem statement above as the source of truth. Add a representative example and the key constraints when reviewing this question.

## 📌 Constraints

- Add the constraints that influence the approach.
- Record any sortedness, uniqueness, or range guarantees.
- Explain what they tell you about a practical solution.

---

## 🧭 Pattern recognition

### Primary pattern: **Linked List**

**Related topics:** `Linked List` `Two Pointers`

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
| Submitted | 10/9/2026, 12:17:42 AM |
| Language | Python3 |
| Runtime | 0 ms · Beats 100.00% |
| Memory | 19.3 MB · Beats 20.36% |
| Runtime percentile | 100.00% |
| Memory percentile | 20.36% |

> Performance values come from this accepted submission and can vary between runs.

### My solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
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

- **Pattern:** Linked List
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
