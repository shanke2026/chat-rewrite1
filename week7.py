from pathlib import Path
for p in Path(".").glob("*.py"):
    print(p.name)
    print(p.stat().st_size)