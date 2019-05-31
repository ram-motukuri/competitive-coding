s = 'MKSabc'
def swap(c, i, j):
    c = list(c)
    c[i], c[j] = c[j], c[i]
    return  ''.join(c)

