def particiona(arr: list, lo: int, hi: int) -> int:
"""
Reorganiza arr[lo..hi] usando partición de Lomuto.
Postcondición:
- arr[p] == pivot
- arr[lo..p-1] <= arr[p]
- arr[p+1..hi] >= arr[p]

Retorna el índice final del pivote.
"""

pivot = arr[hi]
i = lo - 1

for j in range(lo, hi):
if arr[j] <= pivot:
i += 1
arr[i], arr[j] = arr[j], arr[i]

arr[i + 1], arr[hi] = arr[hi], arr[i + 1]

return i + 1
Prueba:

A = [3, 6, 8, 10, 1, 2, 1]
p = particiona(A, 0, 6)

assert A[p] == 1
assert all(v <= 1 for v in A[:p])
assert all(v >= 1 for v in A[p + 1:])

print(f"Partición correcta: {A}, pivote en índice {p}")
