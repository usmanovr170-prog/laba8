data = [1, 3, 2, 5, 7, 8, 6, 9]

segments = []
for i in range(0, len(data), 2):
    a, b = data[i], data[i+1]
    segments.append([min(a, b), max(a, b)])

segments.sort()

count = 1
L, R = segments[0]

for l, r in segments[1:]:
    if l <= R:
        R = max(R, r)
    else:
        count += 1
        L, R = l, r

print(count)