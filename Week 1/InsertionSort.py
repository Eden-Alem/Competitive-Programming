def insertionSort(array):
    for i in range(1, len(array)):
        value = array[i]
        j = i - 1

        while (j >= 0 and value < array[j]):
            array[j+1] = array[j]
            j-=1

        array[j+1] = value

        