import pytest
from mentors import get_all_mentors, get_unique_names, mentors

def test_get_all_mentors():
    all_mentors = get_all_mentors(mentors)
    assert len(all_mentors) > 0

def test_get_unique_names():
    all_mentors = get_all_mentors(mentors)
    unique_names = get_unique_names(all_mentors)
    assert len(unique_names) > 0
    assert isinstance(unique_names, list)
    assert all(isinstance(name, str) for name in unique_names)

