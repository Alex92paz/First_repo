N = 10

def function(n):
    sum_squares = 0
    i = 1
    while i <= n:
        sum_squares = sum_squares + i * i
        i = i + 1
    return sum_squares

result = function(N)
print(result)
