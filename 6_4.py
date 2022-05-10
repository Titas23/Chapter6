# def power(r, n):
#     value = 1 
#     for i in range(1, n + 1):
#         value = r * value
#     return value
   

# print(power(2, 3))

def power(r, n):
    if n == 1:
        return r
    else:
        return r * power(r, n -1)
print(power(2, 3))
