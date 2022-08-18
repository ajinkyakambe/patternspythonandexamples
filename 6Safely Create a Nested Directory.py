# 6. Python Program to Safely Create a Nested Directory

from pathlib import Path
path = Path("C:/Users/hp/PycharmProjects/patternspythonandexamples/samplefolder1")
try:
    path.mkdir()
except OSError:
    print("Failed to make nested directory")
else:
    print("Nested directory made")