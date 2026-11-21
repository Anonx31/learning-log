# Count failed login attempts per IP address.

attempts = [
    ("192.168.1.1", "failed"),
    ("192.168.1.2", "failed"),
    ("192.168.1.1", "failed"),
    ("192.168.1.3", "success"),
    ("192.168.1.1", "failed"),
    ("192.168.1.2", "success"),
    ("192.168.1.4", "failed"),
]

# Count failed attempts per IP
failed_counts = {}

for ip, status in attempts:
    if status == "failed":
        if ip in failed_counts:
            failed_counts[ip] += 1
        else:
            failed_counts[ip] = 1

# Print results
for ip, count in failed_counts.items():
    print(f"{ip}: {count} failed attempt(s)")