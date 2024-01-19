def count_positives_sum_negatives(arr):
    if arr:
        l = [0,0]
        for x in arr:
            if x >= 1:
                l[0] += 1
            else:
                l[1] += x
        return l
    else:
        return []

print( count_positives_sum_negatives([]))