"""Week 1 Homework: Evidence Desk Patterns.

Complete each function using the data structure pattern named in the docstring.

Rules:
- Python 3.11+
- Standard library only
- Do not change function names or parameters
- Run tests with: pytest -q
"""

"""Week 1 Homework: Evidence Desk Patterns.

Expert implementation using optimized Python 3.11+ patterns.
"""

from collections import deque, Counter
from itertools import pairwise


def count_evidence(evidence: list[str]) -> dict[str, int]:
    """Pattern: Frequency counting. Data Structure: Dictionary/Counter."""
    # Counter is the professional standard for frequency mapping.
    return dict(Counter(evidence))


def first_repeated_id(ids: list[str]) -> str | None:
    """Pattern: Seen before. Data Structure: Set."""
    seen_ids: set[str] = set()
    for suspect_id in ids:
        if suspect_id in seen_ids:
            return suspect_id
        seen_ids.add(suspect_id)
    return None


def valid_tags(tags: str) -> bool:
    """Pattern: Stack matching. Data Structure: List as Stack."""
    stack: list[str] = []
    pairs = {")": "(", "]": "[", "}": "{"}
    opening = set(pairs.values())

    for char in tags:
        if char in opening:
            stack.append(char)
        elif char in pairs:
            # Pop and validate in a single logic gate
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack


def lookup_alias(aliases: dict[str, str], alias: str) -> str | None:
    """Pattern: Lookup table. Data Structure: Dictionary."""
    return aliases.get(alias)


def process_reports(reports: list[str]) -> list[str]:
    """Pattern: Queue processing. Data Structure: deque."""
    # Deque is used because popleft() is O(1), whereas list.pop(0) is O(n).
    report_queue = deque(reports)
    processed_reports = []
    while report_queue:
        processed_reports.append(report_queue.popleft())
    return processed_reports


def largest_time_gap(times: list[int]) -> int:
    """Pattern: Sorting + Scan. Data Structure: List."""
    if len(times) < 2:
        return 0

    # sorted() ensures the original input is not mutated.
    sorted_times = sorted(times)
    
    # pairwise(sorted_times) yields (a, b), (b, c)... for an elegant O(n) scan.
    return max(after - before for before, after in pairwise(sorted_times))