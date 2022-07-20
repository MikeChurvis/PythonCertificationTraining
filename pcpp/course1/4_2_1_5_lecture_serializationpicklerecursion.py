import pickle

lastref = []
originalref = lastref

for _ in range(498):
    newref = []
    lastref.append(newref)
    lastref = newref

# lastref.append(originalref)

print(pickle.loads(pickle.dumps(originalref)))  # This raises a RecursionError
