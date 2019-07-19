def odd(x):
    return x % 2


def odd2(x):
    return x % 2


temp = range(10)
s = list(temp)
show = filter(odd2, [0,1, 2, 3, 4, 5, 6, 7, 8, 9])
#show =filter(lambda x:x%2,list(range(10)))
print(list(show))
