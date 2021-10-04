# ลบtext (file)
import os
try:
    if os.path.exists("student.txt"):
        os.remove("student.txt")
    else:
        print("No file")
except Exception as a:
    print(a)