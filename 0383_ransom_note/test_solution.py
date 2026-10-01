import pytest

from solution import Solution


@pytest.mark.parametrize(
    "ransom_note, magazine, expected",
    [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("abc", "abc", True),
        ("ab", "xyzab", True),
        ("aab", "ab", False),
        ("a", "a", True),
    ],
)
def test_can_construct(ransom_note, magazine, expected):
    assert Solution().canConstruct(ransom_note, magazine) == expected
