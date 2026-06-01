from pathlib import Path
import sys
import pytest

# Ensure source is in path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from challenges import (
    count_evidence,
    first_repeated_id,
    largest_time_gap,
    lookup_alias,
    process_reports,
    valid_tags,
)

# ... [Previous tests remain unchanged] ...

# -----------------------------------------------------------------------------
# Optional Challenge 1: process_reports (SKIPS REMOVED)
# -----------------------------------------------------------------------------

def test_process_reports_returns_reports_in_arrival_order() -> None:
    reports = ["burglary", "traffic stop", "missing wallet", "noise complaint"]
    assert process_reports(reports) == reports

def test_process_reports_handles_empty_list() -> None:
    assert process_reports([]) == []

# -----------------------------------------------------------------------------
# Optional Challenge 2: largest_time_gap (SKIPS REMOVED)
# -----------------------------------------------------------------------------

def test_largest_time_gap_sorts_and_finds_largest_neighbor_gap() -> None:
    assert largest_time_gap([1300, 915, 1600, 945]) == 355

def test_largest_time_gap_handles_short_lists() -> None:
    assert largest_time_gap([]) == 0
    assert largest_time_gap([1200]) == 0

def test_largest_time_gap_does_not_mutate_input() -> None:
    times = [1300, 915, 1600, 945]
    largest_time_gap(times)
    assert times == [1300, 915, 1600, 945]

# -----------------------------------------------------------------------------
# REQUIRED: Custom Test (Expert Addition)
# -----------------------------------------------------------------------------

def test_valid_tags_complex_interleaved_text() -> None:
    """Expert addition: ensures logic handles mixed text and deep nesting."""
    complex_input = "Evidence(ID: [A-12]){Status: [Secure]}"
    assert valid_tags(complex_input) is True
    
    malformed_input = "Evidence(ID: [A-12]){Status: [Secure)]}"
    assert valid_tags(malformed_input) is False