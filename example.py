def make_partition(lengths, n, partition=[]):
    if sum(partition) == n:
        return [partition]

    partitions = []
    for length in lengths:
        remaining_lengths = [l for l in lengths if l != length]
        if sum(partition) + length <= n:
            new_partition = partition + [length]
            partitions += make_partition(remaining_lengths, n, new_partition)

    return partitions

# Example usage:
lengths = [1, 2, 3, 4, 5]
target_sum = 5
result = make_partition(lengths, target_sum)

print(result)
