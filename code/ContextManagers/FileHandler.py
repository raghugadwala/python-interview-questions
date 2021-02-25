# Method1 - Class based
"""
In the below program, it is mandatory to implement the __enter__ and the __exit__ methods. 
After the __enter__ method ends, the code in the with block will be executed. Finally, the Context Manager will call the __exit__ method.
"""

class FileHandler():

    def __init__(self, file_name, file_mode):
        self._file_name = file_name
        self._file_mode = file_mode

    def __enter__(self):
        self._file = open(self._file_name, self._file_mode)
        return self._file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._file.close()


if __name__ == "__main__":
    with FileHandler('test.txt', 'w') as f:
        f.write('Test')
