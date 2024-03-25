def anyOperation(callback, x, y):
    return callback(x, y)

def add(x, y):
    return x + y

result = anyOperation(add, 3, 4)
print("Result of addition:", result)
