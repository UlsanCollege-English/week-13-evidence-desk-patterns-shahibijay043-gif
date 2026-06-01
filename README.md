[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cm6PS4yt)
# Week 1 Homework: Evidence Desk Patterns

## Student Name
Student Name

Shahi Bijay
Student ID: 2412083

Summary

In this homework, I practiced several important data structure patterns in Python. I used a dictionary for frequency counting in the evidence counter problem and a set to detect repeated suspect IDs efficiently. I also used a list as a stack to validate balanced evidence tags and a dictionary as a lookup table to find real names from aliases. While completing these problems, I learned how different data structures can solve specific tasks more effectively. This assignment also helped me improve my understanding of time and space complexity, testing, and handling edge cases.

Problem Notes
1.  Evidence Counter
Pattern

Frequency Counting

Data Structure

Dictionary

Approach
Step 1: Create an empty dictionary.
Step 2: Loop through each evidence label.
Step 3: Count how many times each label appears and store the result.
Complexity
Time: O(n)
Space: O(n)

Explain briefly:

I visit each evidence item once and store counts in a dictionary. The dictionary may store up to all unique items.

Edge Cases Checked
 Empty list
 One item
 Repeated items
 Different labels
2. Repeat Suspect ID
Pattern

Seen Before

Data Structure

Set

Approach
Step 1: Create an empty set called seen.
Step 2: Loop through each suspect ID.
Step 3: Return the ID when it appears a second time.
Complexity
Time: O(n)
Space: O(n)

Explain briefly:

The set provides fast membership checking, allowing repeated IDs to be detected efficiently.

Edge Cases Checked
 Empty list
 No repeated IDs
 First two IDs match
 Multiple repeated IDs
3. Evidence Tag Validator
Pattern

Stack Matching

Data Structure

List (used as a Stack)

Approach
Step 1: Create an empty stack.
Step 2: Push opening brackets onto the stack.
Step 3: Match closing brackets with the most recent opening bracket.
Complexity
Time: O(n)
Space: O(n)

Explain briefly:

Each character is processed once. The stack stores unmatched opening brackets.

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

Dictionary

Approach
Step 1: Check whether the alias exists in the dictionary.
Step 2: Return the corresponding real name or None.
Complexity
Time: O(1)
Space: O(1)

Explain briefly:

Dictionary lookups are performed in constant time on average.

Edge Cases Checked
 Known alias
 Unknown alias
 Empty dictionary
Assistance & Sources
AI Used?
 Yes
 No
If yes, what did AI help with?
Helped explain data structure concepts.
Helped review time and space complexity.
Helped improve README formatting and wording.
Other Sources
Course notes and lecture materials.
Python Documentation.
No other outside sources used.