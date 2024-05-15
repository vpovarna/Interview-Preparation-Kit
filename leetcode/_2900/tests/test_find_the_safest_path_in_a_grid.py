from leetcode._2900._2812_find_the_safest_path_in_a_grid import Solution


def test_get_ones_coordinates() -> None:
    input_grid = [[1,0,0],[0,0,0],[0,0,1]]
    points = Solution().get_ones_locations(grid=input_grid)
    assert len(points) == 2


def test_get_distances_matrix() -> None:
    input_grid = [[1,0,0],[0,0,0],[0,0,1]]
    expected_target_grid = [[0, 1, 2], [1, 2, 1], [2, 1, 0]]
    target_grid = Solution().get_distances_matrix(grid=input_grid)
    assert expected_target_grid == target_grid