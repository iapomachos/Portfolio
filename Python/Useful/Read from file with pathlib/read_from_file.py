#I had to import pathlib since relative paths weren't working on windows (os.getcwd() was showing my home directory)
#related stackoverflow article: https://stackoverflow.com/questions/71811330/python-searching-for-image-in-wrong-directory
import pathlib

with open(pathlib.Path(__file__).parent / "file.txt") as data:
            score = int(data.read())


print(score)