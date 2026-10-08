<div align="center">

# 🧩 203 · Remove Linked List Elements

### A clear solution, a reusable pattern, and a lesson worth remembering.

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem-FFA116?style=flat-square&logo=leetcode&logoColor=white)](https://leetcode.com/problems/remove-linked-list-elements/) [![Topic](https://img.shields.io/badge/Topic-Linked%20List-0F766E?style=flat-square)](#-pattern-recognition) [![Language](https://img.shields.io/badge/Language-Python3-2563EB?style=flat-square)](#-solution)

**Difficulty:** Easy · **Status:** Solved

</div>

---

## 🎯 Problem summary

<h2><a href="https://leetcode.com/problems/remove-linked-list-elements/">203. Remove Linked List Elements</a></h2><h3>Easy</h3><hr><p>Given the <code>head</code> of a linked list and an integer <code>val</code>, remove all the nodes of the linked list that has <code>Node.val == val</code>, and return <em>the new head</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg" style="width: 500px; height: 142px;" />
<pre>
<strong>Input:</strong> head = [1,2,6,3,4,5,6], val = 6
<strong>Output:</strong> [1,2,3,4,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [], val = 1
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = [7,7,7,7], val = 7
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 50</code></li>
	<li><code>0 &lt;= val &lt;= 50</code></li>
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

**Related topics:** `Linked List` `Recursion`

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
| Submitted | 10/9/2026, 12:16:55 AM |
| Language | Python3 |
| Runtime | 0 ms · Beats 100.00% |
| Memory | 22.5 MB · Beats 43.05% |
| Runtime percentile | 100.00% |
| Memory percentile | 43.05% |

> Performance values come from this accepted submission and can vary between runs.

### My solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head 
        curr = dummy

        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next


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
