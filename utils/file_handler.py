import json


def load_files(input_path):

    with open("multigenomic\gene.json") as myFile:
        data = myFile.read()
        for i in data:
            print(i)
            print(input_path)


