import pytest
from courses import get_common_mentors, courses, mentors

def test_get_common_mentors():
    pairs, common_names_sorted = get_common_mentors(courses, mentors)
    assert len(pairs) > 0
    assert len(common_names_sorted) > 0

