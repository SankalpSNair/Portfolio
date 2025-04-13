def max_thieves_caught(arr, k):
    policemen = []
    thieves = []
    caught = 0

    # Collect positions of policemen and thieves
    for i in range(len(arr)):
        if arr[i] == 'P':
            policemen.append(i)
        elif arr[i] == 'T':
            thieves.append(i)

    # Process the positions to catch thieves
    while policemen and thieves:
        # If the policeman can catch the thief
        if abs(policemen[0] - thieves[0]) <= k:
            caught += 1
            policemen.pop(0)
            thieves.pop(0)
        # If the policeman is too far left, remove him
        elif policemen[0] < thieves[0]:
            policemen.pop(0)
        # If the thief is too far left, remove him
        else:
            thieves.pop(0)

    return caught

# Input
n = int(input("Enter the size:"))
arr = input("Enter the elements: ").split()
k = int(input("Enter the value of K:"))

# Output
print(arr)
print(max_thieves_caught(arr, k))
