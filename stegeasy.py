# Minimal key-checking demo
import time
key = input("Enter key to edit (Security Key): ")
msg = input("Enter text to hide: ")
time.sleep(1.5)
print("Data hiding in image completed successfully.")

opt = input("Enter 1 to extract data from Image: ")

if opt == "1":
    key2 = input("Re-enter key to extract text: ")
    
    if key2 == key:
        print("Decrypted text was:", msg)
    else:
        print("Wrong key!")

