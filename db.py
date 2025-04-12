class MiniDB:
    def __init__(self, colums, path):
        self.colums = list(colums)
        self.data =[]
    def load_from_file(self, path):
        with open(path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(';')

                if len(parts) != len(self.colums):
                    raise ValueError(f"не відповідає кількості колонок: {line}")
                record = {self.colums[i]:parts[i] for i in range(len(self.colums))}
                self.data.append(record)
            
    def save_to_file(self, path):
        with open(path, 'w') as f:
            for record in self.data:
                line = ';'.join(str(record[col]) for col in self.colums)
                f.write(line+'\n')
    
    def add(self, values):
        if len(values) != len(self.colums):
            raise ValueError(f"не відповідає кількості колонок: {values}")
        record = {self.colums[i]:values[i] for i in range(len(self.colums))}
        self.data.append(record)