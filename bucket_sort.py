def bucket_sort(array, bucket_count):
    if len(array) == 0 or len(array) == 1:
        return array

    answer = []

    # Determine minimum and maximum values
    min_value = array[0]
    max_value = array[0]
    for i in range(1, len(array)):
        if array[i] < min_value:
            min_value = array[i]
        elif array[i] > max_value:
            max_value = array[i]


    # Make a list of buckets
    buckets = []
    for i in range(0, bucket_count + 1):
        buckets.append([])

    bucket_size = (max_value - min_value) // bucket_count

    # Distribute input array values into buckets
    for i in range(0, len(array)):
        buckets[(array[i] // bucket_size)].append(array[i])


    for i in buckets:
        for e in range(len(i)):
            for f in range(len(i)-1-e):
                if i[f] > i[f + 1]:
                    i[f], i[f + 1] = i[f + 1], i[f]

    for i in range(len(buckets)):
            answer = answer + buckets[i]

    print(answer)


bucket_sort(my_arr, 6)
