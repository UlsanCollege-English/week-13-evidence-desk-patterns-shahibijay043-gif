from collections import deque


def count_evidence(evidence: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}

    for item in evidence:
        counts[item] = counts.get(item, 0) + 1

    return counts


def first_repeated_id(ids: list[str]) -> str | None:
    seen: set[str] = set()

    for suspect_id in ids:
        if suspect_id in seen:
            return suspect_id

        seen.add(suspect_id)

    return None


def valid_tags(tags: str) -> bool:
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
    return aliases.get(alias)


def process_reports(reports: list[str]) -> list[str]:
    queue = deque(reports)
    processed: list[str] = []

    while queue:
        processed.append(queue.popleft())

    return processed


def largest_time_gap(times: list[int]) -> int:
    if len(times) < 2:
        return 0

    sorted_times = sorted(times)
    largest_gap = 0

    for index in range(1, len(sorted_times)):
        gap = sorted_times[index] - sorted_times[index - 1]

        if gap > largest_gap:
            largest_gap = gap

    return largest_gap