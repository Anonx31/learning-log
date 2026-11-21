# Remove duplicates from a list while preserving original order.

original = [1, 2, 2, 3, 3, 3]

unique = []   # result list
seen = set()  # tracks values already added

for item in original:
    if item not in seen:
        unique.append(item)
        seen.add(item)

print(unique)