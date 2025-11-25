# ...existing code...
from PIL import Image
import sys
# ...existing code...

# --- HIDE ---
key = input("Enter key to edit (Security Key): ")
msg = input("Enter text to hide: ")

try:
    img = Image.open("input.png").convert("RGB")
except FileNotFoundError:
    print("input.png not found in", ".")
    sys.exit(1)

px = img.load()

# simple capacity check (we only write along y=0)
if 1 + len(key) + len(msg) > img.width:
    print("Image is too narrow to hide that much text. Width:", img.width)
    sys.exit(1)

# put key length + message length + chars into FIRST PIXEL ONLY
px[0, 0] = (len(key), len(msg), 0)

# put the characters into next pixels
x = 1
for c in (key + msg):
    px[x, 0] = (ord(c) & 0xFF, 0, 0)
    x += 1

img.save("output.png")
print("Data hiding in image completed successfully.")

# --- EXTRACT ---
if input("Enter 1 to extract data from Image: ") == "1":
    key2 = input("Re-enter key to extract text: ")
    try:
        img = Image.open("output.png").convert("RGB")
    except FileNotFoundError:
        print("output.png not found.")
        sys.exit(1)

    px = img.load()

    klen, mlen, _ = px[0, 0]

    text = ""
    for x in range(1, 1 + klen + mlen):
        r, g, b = px[x, 0]
        text += chr(r)

    if text[:klen] == key2:
        print("Decrypted text was:", text[klen:])
    else:
        print("Wrong key!")
# ...existing code...
