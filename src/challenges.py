"""Week 1 Homework: Evidence Desk Patterns.

Complete each function using the data structure pattern named in the docstring.

Rules:
- Python 3.11+
- Standard library only
- Do not change function names or parameters
- Run tests with: pytest -q
"""

from collections import deque


def count_evidence(evidence: list[str]) -> dict[str, int]:
    """Return a dictionary counting how many times each evidence label appears."""

    evidence_counts: dict[str, int] = {}

    for label in evidence:
        evidence_counts[label] = evidence_counts.get(label, 0) + 1

    return evidence_counts


def first_repeated_id(ids: list[str]) -> str | None:
    """Return the first suspect ID that appears a second time."""

    seen_ids: set[str] = set()

    for suspect_id in ids:
        if suspect_id in seen_ids:
            return suspect_id

        seen_ids.add(suspect_id)

    return None


def valid_tags(tags: str) -> bool:
    """Return True if all bracket-style evidence tags are balanced."""

    stack: list[str] = []

    matching_brackets = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    opening_brackets = {"(", "[", "{"}

    for character in tags:

        if character in opening_brackets:
            stack.append(character)

        elif character in matching_brackets:

            if not stack:
                return False

            if stack.pop() != matching_brackets[character]:
                return False

    return len(stack) == 0


def lookup_alias(
    aliases: dict[str, str],
    alias: str,
) -> str | None:
    """Return the real name connected to an alias."""

    return aliases.get(alias)


def process_reports(reports: list[str]) -> list[str]:
    """Return case reports in first-in, first-out processing order."""

    report_queue: deque[str] = deque(reports)
    processed_reports: list[str] = []

    while report_queue:
        processed_reports.append(report_queue.popleft())

    return processed_reports


def largest_time_gap(times: list[int]) -> int:
    """Return the largest gap between neighboring event times after sorting."""

    if len(times) < 2:
        return 0

    sorted_times = sorted(times)
    largest_gap = 0

    for index in range(1, len(sorted_times)):
        current_gap = sorted_times[index] - sorted_times[index - 1]

        if current_gap > largest_gap:
            largest_gap = current_gap

    return largest_gap