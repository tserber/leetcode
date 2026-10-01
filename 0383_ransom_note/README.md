# 383. Ransom Note

Difficulty: Easy
Link: https://leetcode.com/problems/ransom-note/

## Problem

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be
constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

### Example 1

```
Input: ransomNote = "a", magazine = "b"
Output: false
```

### Example 2

```
Input: ransomNote = "aa", magazine = "ab"
Output: false
```

### Example 3

```
Input: ransomNote = "aa", magazine = "aab"
Output: true
```

### Constraints

- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters.

## Approach

Count the letter frequencies in `magazine` into a hash map. Then walk `ransomNote`,
decrementing the count for each letter needed; if a letter is unavailable (count `<= 0`
or missing), the note can't be built. Single pass over each string, `O(n + m)` time and
`O(1)` extra space (bounded by the 26-letter alphabet).
