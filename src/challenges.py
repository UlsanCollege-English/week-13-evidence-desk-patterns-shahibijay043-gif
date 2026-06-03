"""Week 1 Homework: Evidence Desk Patterns."""

from collections import deque


def count_evidence(evidence: list[str]) -> dict[str, int]:
    """Return a dictionary counting how many times each evidence label appears."""
    counts: dict[str, int] = {}

    for item in evidence:
        counts[item] = counts.get(item, 0) + 1

    return counts


def first_repeated_id(ids: list[str]) -> str | None:
    """Return the first suspect ID that appears a second time."""
    seen: set[str] = set()

    for suspect_id in ids:
        if suspect_id in seen:
            return suspect_id

        seen.add(suspect_id)

    return None


def valid_tags(tags: str) -> bool:
    """Return True if all bracket-style evidence tags are balanced."""
    stack: list[str] = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for char in tags:
        if char in "([{":
            stack.append(char)

        elif char in pairs:
            if not stack:
                return False

            if stack.pop() != pairs[char]:
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
    queue = deque(reports)
    processed: list[str] = []

    while queue:
        processed.append(queue.popleft())

    return processed


def largest_time_gap(times: list[int]) -> int:
    """Return the largest gap between neighboring event times after sorting."""
    if len(times) < 2:
        return 0

    sorted_times = sorted(times)
    largest_gap = 0

    for i in range(1, len(sorted_times)):
        gap = sorted_times[i] - sorted_times[i - 1]

        if gap > largest_gap:
            largest_gap = gap

    return largest_gap