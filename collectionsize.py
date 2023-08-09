def collection_size(collect):
    count = 0
    for index in collect:
        count += 1
    return count


collection = [2, 3, 4, 67, 88, 6, 5, 1, 4]
print(collection_size(collection))
