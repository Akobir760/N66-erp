import csv, os

class FileManager:
    def __init__(self, file_path):
        self.path = f"data/{file_path}"

    
    def read(self):
        if os.path.exists(self.path):
            with open(file = self.path, mode="r", encoding="UTF-8") as file:
                return list(csv.reader(file))
        else:
            print("File can not find!")

        
    def write(self, data):
        with open(file=self.path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
            
    
    def append(self, data):
        if os.path.exists(self.path):
            with open(file=self.path, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(data)
        else:
            print("File can not find!")

        