print("=== Trip Summary Check ===")

with open("Trip_Summary.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

if len(lines) > 5:
    print("PASS: File has enough content")
else:
    print("FAIL: File is too short")
