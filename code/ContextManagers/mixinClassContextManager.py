# Method3 - Function Decorator
class file_handler_mixin(ContextDecorator):
    def __init__(self,file_name, file_mode):
        self._file_name = file_name
        self._file_mode = file_mode
        self._file = None

    def __enter__(self):
        print(f"Enter Method: File Name {self._file_name}")
        self._file = open(self._file_name, self._file_mode)
        return self._file

    def __exit__(self,exc_type,exc_value,exc_traceback):
        print(f"Exit Method: File Mode {self._file_mode}")
        self._file.close()

@file_handler_mixin("test.txt","w" )
def write_to_file():
    print("Not access to the value returned by the __enter__ method")

if __name__ == "__main__":
    write_to_file()