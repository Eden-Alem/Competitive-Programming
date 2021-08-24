def sockMerchant(n, ar):
    count = 0
    for i in set(ar):
        occurence = ar.count(i)
        if (occurence % 2 == 0):
            count += occurence // 2
        else:
            count += (occurence-1) // 2
    return count