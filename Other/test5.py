N = 10
sum_squares = 0
i = 1
while i < N+1:
    sum_squares = sum_squares + (i * i)
    i = i + 1

print(f"The sum of the squares of numbers from 1 to {N} is {sum_squares}")