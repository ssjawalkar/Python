def find_pairs_with_sum(arr, k):
    count = 0
    freq = {}

    for num in arr:
        complement = k - num
        

        if complement in freq:
            count += freq[complement]
        

        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    return count

arr = [1, 2, 3, 4, 5]
k = 6



pair_count = find_pairs_with_sum(arr, k)

print(f"Pair count: {pair_count}")
