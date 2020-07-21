def index_all(arr, num):
    indices = list()
    for i in range(len(arr)):
        if arr[i] == num:
            indices.append([i])
        elif isinstance(arr[i], list):
            for index in index_all(arr[i], num):
                indices.append([i]+index)
        print(indices)


index_all([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2)
