# BEGIN (write your solution here)
def transposed(matrix):
    result = []
    zip_m = map(list, zip(*matrix))
    for i in zip_m:
        result.extend([i])
    return result
# END
transposed([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ])