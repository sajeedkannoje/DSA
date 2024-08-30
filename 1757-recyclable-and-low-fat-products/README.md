<div align="center">

# 🧩 1908 · Recyclable and Low Fat Products

### A clear solution, a reusable pattern, and a lesson worth remembering.

[![LeetCode](https://img.shields.io/badge/LeetCode-Problem-FFA116?style=flat-square&logo=leetcode&logoColor=white)](https://leetcode.com/problems/recyclable-and-low-fat-products/) [![Topic](https://img.shields.io/badge/Topic-Database-0F766E?style=flat-square)](#-pattern-recognition) [![Language](https://img.shields.io/badge/Language-MySQL-2563EB?style=flat-square)](#-solution)

**Difficulty:** Easy · **Status:** Solved

</div>

---

## 🎯 Problem summary

<h2><a href="https://leetcode.com/problems/recyclable-and-low-fat-products/">1908. Recyclable and Low Fat Products</a></h2><h3>Easy</h3><hr><p>Table: <code>Products</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type (&#39;Y&#39;, &#39;N&#39;) where &#39;Y&#39; means this product is low fat and &#39;N&#39; means it is not.
recyclable is an ENUM (category) of types (&#39;Y&#39;, &#39;N&#39;) where &#39;Y&#39; means this product is recyclable and &#39;N&#39; means it is not.</pre>

<p>&nbsp;</p>

<p>Write a solution to find the ids of products that are both low fat and recyclable.</p>

<p>Return the result table in <strong>any order</strong>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
<strong>Output:</strong> 
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
<strong>Explanation:</strong> Only products 1 and 3 are both low fat and recyclable.
</pre>


### Given, return & examples

Use the original problem statement above as the source of truth. Add a representative example and the key constraints when reviewing this question.

## 📌 Constraints

- Add the constraints that influence the approach.
- Record any sortedness, uniqueness, or range guarantees.
- Explain what they tell you about a practical solution.

---

## 🧭 Pattern recognition

### Primary pattern: **Database**

**Related topics:** `Database`

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
| Submitted | 8/30/2024, 7:54:47 PM |
| Language | MySQL |
| Runtime | 417 ms · Beats 100.00% |
| Memory | 0B · Beats 100.00% |
| Runtime percentile | 100.00% |
| Memory percentile | 100.00% |

> Performance values come from this accepted submission and can vary between runs.

### My solution

```mysql
# Write your MySQL query statement below
select product_id from products where low_fats = "Y" AND recyclable = "Y";
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

- **Pattern:** Database
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
