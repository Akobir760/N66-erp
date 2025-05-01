import csv, os
    
def read(path):
    if os.path.exists(path):
        with open(file = path, mode="r", encoding="UTF-8") as file:
            return list(csv.reader(file))
    else:
        print("File can not find!")

    
def write(path, data):
    with open(file=path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
        

def append(path, data):
    if os.path.exists(path):
        with open(file=path, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)
    else:
        print("File can not find!")

        