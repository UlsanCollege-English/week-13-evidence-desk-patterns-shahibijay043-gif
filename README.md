[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cm6PS4yt)
# Week 1 Homework: Evidence Desk Patterns
 Student Name

Shahi Bijay

## Summary
This homework focuses on the implementation of fundamental data structures to solve algorithmic challenges typical of technical interviews and high-performance data processing. The tasks emphasize:Frequency Analysis: Utilizing hash maps for $O(N)$ counting.Set Theory: Implementing $O(1)$ membership tests for duplicate detection.Linear Structures: Managing Last-In, First-Out (Stack) and First-In, First-Out (Queue) processing.Computational Efficiency: Prioritizing time and space complexity ($Big-O$) to ensure scalability.

## How to Run Tests

From the repository root, run:

```bash
pytest -q

To run one test file:

pytest -q tests/test_challenges.py
Required Problems

Complete these functions in src/challenges.py:

count_evidence
first_repeated_id
valid_tags
lookup_alias
Optional Challenges

These are extra practice unless your instructor tells you otherwise:

process_reports
largest_time_gap

Optional tests are skipped by default. To run them, remove the @pytest.mark.skip(...) line above the optional test you want to check.

Problem Notes
1. Evidence Counter
Pattern

Frequency Counting

Data Structure

Dictionary (dict)

Approach
Step 1: Create an empty dictionary.
Step 2: Loop through each evidence item.
Step 3: Update the count for each item and return the completed dictionary.
Complexity
Time: O(n)
Space: O(n)

Explain briefly:

The function visits each evidence item once. In the worst case, every item is unique and must be stored in the dictionary.

Edge Cases Checked
 Empty list
 One item
 Repeated items
 Different labels
2. Repeat Suspect ID
Pattern

Seen Before

Data Structure

Set (set)

Approach
Step 1: Create an empty set to store seen IDs.
Step 2: Loop through each ID in the list.
Step 3: Return the first ID already in the set; otherwise add it and continue.
Complexity
Time: O(n)
Space: O(n)

Explain briefly:

Each ID is checked and added to the set at most once. Set lookups are generally constant time.

Edge Cases Checked
 Empty list
 No repeated IDs
 First two IDs match
 Multiple repeated IDs
3. Evidence Tag Validator
Pattern

Stack Matching

Data Structure

List used as a Stack

Approach
Step 1: Create an empty stack and bracket mapping dictionary.
Step 2: Push opening brackets onto the stack.
Step 3: Verify each closing bracket matches the most recent opening bracket.
Complexity
Time: O(n)
Space: O(n)

Explain briefly:

The function scans the string once. In the worst case, all opening brackets are stored in the stack.

Edge Cases Checked
 Empty string
 Correctly nested tags
 Mismatched tags
 Closing tag before opening tag
 Unclosed opening tag
 Non-bracket characters
4. Alias Directory
Pattern

Lookup Table

Data Structure

Dictionary (dict)

Approach
Step 1: Search for the alias in the dictionary.
Step 2: Return the real name if found; otherwise return None.
Complexity
Time: O(1)
Space: O(1)

Explain briefly:

Dictionary lookups are typically constant time and do not require additional memory.

Edge Cases Checked
 Known alias
 Unknown alias
 Empty dictionary
Assistance & Sources
AI Used?
 Yes
 No
If yes, what did AI help with?
Helped explain data structure patterns and complexity analysis.
Helped review Python syntax and function structure.
Helped improve README formatting and documentation.
Other Sources
Course notes and lecture materials.
GitHub Classroom assignment instructions.