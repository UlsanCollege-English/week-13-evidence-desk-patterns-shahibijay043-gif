NAME : Bijay shahi



This homework helped me practice using common data structures in Python. I used dictionaries for counting and lookups, a set for finding duplicates, and a list as a stack for matching brackets. I also learned how to analyze time and space complexity and test different edge cases.

How to Run Tests
pytest -q

To run only one test file:

pytest -q tests/test_challenges.py
Required Problems
1. Evidence Counter

Pattern: Frequency Counting

Data Structure: Dictionary

Approach:

Create an empty dictionary.
Count how many times each evidence label appears.
Return the dictionary.

Complexity:

Time: O(n)
Space: O(n)

Edge Cases Checked:

Empty list

One item

Repeated items

Different labels

2. Repeat Suspect ID

Pattern: Seen Before

Data Structure: Set

Approach:

Create an empty set.
Check whether an ID has already been seen.
Return the first repeated ID.

Complexity:

Time: O(n)
Space: O(n)

Edge Cases Checked:

Empty list

No repeated IDs

First two IDs match

Multiple repeated IDs

3. Evidence Tag Validator

Pattern: Stack Matching

Data Structure: List (Stack)

Approach:

Push opening brackets onto a stack.
Match closing brackets with the top item.
Return True if all brackets are balanced.

Complexity:

Time: O(n)
Space: O(n)

Edge Cases Checked:

Empty string

Correctly nested tags

Mismatched tags

Closing tag before opening tag

Unclosed opening tag

Non-bracket characters

4. Alias Directory

Pattern: Lookup Table

Data Structure: Dictionary

Approach:

Search for the alias in the dictionary.
Return the real name if found.
Return None if not found.

Complexity:

Time: O(1)
Space: O(1)

Edge Cases Checked:

Known alias

Unknown alias

Empty dictionary

Optional Challenges
Dispatch Queue

Pattern: Queue Processing

Data Structure: Deque

Complexity:

Time: O(n)
Space: O(n)
Timeline Gap Finder

Pattern: Sorting + Scan

Data Structure: List

Complexity:

Time: O(n log n)
Space: O(n)
Assistance & Sources
AI Used?

Yes

No

If yes, what did AI help with?
Understanding data structure patterns.
Reviewing complexity analysis.
Improving README organization.
Other Sources
Course notes
Python Documentation
Class examples