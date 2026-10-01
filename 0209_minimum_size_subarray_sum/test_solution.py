import pytest

from solution import Solution


@pytest.mark.parametrize(
    "target, nums, expected",
    [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
        (15, [1, 2, 3, 4, 5], 5),
        (100, [1, 2, 3], 0),
        (5, [5], 1),
        (3, [1, 1], 0),
    ],
)
def test_min_sub_array_len(target, nums, expected):
    assert Solution().minSubArrayLen(target, nums) == expected
