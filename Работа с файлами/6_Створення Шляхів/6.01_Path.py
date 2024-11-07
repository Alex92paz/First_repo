from pathlib import Path

p = Path("example.txt")
p.write_text("Hello, world!")
print(p.read_text()) 
print("Exists:", p.exists()) 
