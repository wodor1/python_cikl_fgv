# első feladat

nums = [3, 4, 9, 6, 2]

for num in nums:
    if num % 2 == 0:
        print(f"{num}: osztható")
    else:
        print(f"{num}: nem osztható")


# második feladat

players = ['Peter', 'Kate', 'John']

for i, player in enumerate(players, start=1):
    print(f"{i}. {player}")


# harmadik feladat

def check_types(lst):
    result = []
    for item in lst:
        if type(item) is str:
            result.append('string')
        elif type(item) is int:
            result.append('integer')
        elif type(item) is bool:
            result.append('boolean')
    return result


x = ['', 4, True]
print(check_types(x))
