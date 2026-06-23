import sys
sys.stdout.reconfigure(encoding="utf-8")

with open(r"C:\Users\77307\Desktop\starpath-v3-desktop.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Show the full 1024px media query
print("=== @media 1024px ===")
in_media = False
depth = 0
for i, line in enumerate(lines):
    if "@media(min-width:1024px)" in line:
        in_media = True
    if in_media:
        print(f"{i+1}: {line.rstrip()}")
        depth += line.count("{") - line.count("}")
        if depth <= 0 and in_media and "{" in line:
            break

print("\n=== @media 1440px ===")
in_media = False
depth = 0
for i, line in enumerate(lines):
    if "@media(min-width:1440px)" in line:
        in_media = True
    if in_media:
        print(f"{i+1}: {line.rstrip()}")
        depth += line.count("{") - line.count("}")
        if depth <= 0 and in_media and "{" in line:
            break

# Show base .content CSS
print("\n=== base .content ===")
for i, line in enumerate(lines):
    if ".content{" in line and "class" not in line and "@media" not in line:
        for j in range(i, min(i+6, len(lines))):
            print(f"{j+1}: {lines[j].rstrip()}")

# Show base .bottom-nav CSS
print("\n=== base .bottom-nav ===")
for i, line in enumerate(lines):
    if ".bottom-nav{" in line and "class" not in line and "@media" not in line:
        for j in range(i, min(i+8, len(lines))):
            print(f"{j+1}: {lines[j].rstrip()}")
        break

# Show base .panel CSS
print("\n=== base .panel ===")
for i, line in enumerate(lines):
    if ".panel{" in line and "class" not in line:
        for j in range(i, min(i+3, len(lines))):
            print(f"{j+1}: {lines[j].rstrip()}")
        break

# Show the 1024px panel.active line
print("\n=== panel.active @1024 ===")
for i, line in enumerate(lines):
    if "panel.active" in line and "1024" in lines[max(0,i-5):i+1].__repr__():
        print(f"{i+1}: {line.rstrip()}")
