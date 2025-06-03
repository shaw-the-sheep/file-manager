import os
from sql.sql_manager import SQLManager

class StoreManager:
    def __init__(self):
        self.connection = SQLManager('files.db')
        self.create_table()
    
    def create_table(self):
        if not self.connection.check_table_exists('files'):
            columns = {
                'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
                'pathname': 'TEXT NOT NULL',
                'directory': 'TEXT NOT NULL',
                'filename': 'TEXT NOT NULL',
                'extension': 'TEXT NOT NULL',
                'size': 'INTEGER NOT NULL',
            }
            self.connection.create_table("files", columns)
            print("Created table 'files' successfully.")
    
    def process_file(self, filepath):
        name = filepath.split('/')[-1]
        extension = name.split('.')[-1]
        size = os.path.getsize(filepath)
        directory = os.path.dirname(filepath).split('/')[-1]
        columns = {
            'pathname': filepath,
            'directory': directory,
            'filename': name,
            'extension': extension,
            'size': size
        }
        return columns
    
    def add_file(self, filepath):
        if not self.connection.check_row_exists('files', f"pathname = '{filepath}'"):
            columns = self.process_file(filepath)
            self.connection.insert('files', columns)

    def delete_file(self, filepath):
        try:
            if self.connection.check_row_exists('files', f"pathname = '{filepath}'"):
                self.connection.delete('files', f"pathname = {filepath}")
        except Exception as e:
            print(e)
        
    def move_file(self, old_path, new_path):
        self.connection.update('files', {'pathname': new_path}, f"pathname = '{old_path}'")

    def get_files(self):
        tree = {}
        data = self.connection.select('files', ['pathname'])
        paths_dict = [x[0] for x in data]
        print(paths_dict)
        for path in paths_dict:
            parts = path.split("\\")
            current = tree
            for part in parts:
                current = current.setdefault(part, {})
        return tree
    
    def close_connection(self):
        self.connection.close()

        
    

