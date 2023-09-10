with open('17_9840.txt') as f:
    A = [int(i) for i in f]
max_num = 0
for i in sorted(A)[::-1]:
    if len(str(i)) == 4 and i % 100 == 39:
        max_num = i
        break
B = []
for i in range(len(A) - 1):
    s = (len(str(abs(A[i]))) == 4) + (len(str(abs(A[i + 1]))) == 4)
    if s == 1 and (A[i] + A[i + 1]) ** 2 <= max_num ** 2:
        B.append(A[i] + A[i + 1])
print(len(B), max(B))