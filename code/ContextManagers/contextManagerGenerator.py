# Method2 - Generator
"""
Instead of the __enter__ and __exit__ methods, the generator along with the @contextlib.contextmanager decorator will run everything before the yield statement as if it were part of the __enter__ method. 
The yielded value may be the result that the __enter__ method would return.
After it, the code inside the with block will be run and as the last step the code after the yield statement will be run as if it were the __exit__ method.
"""
import contextlib

@contextlib.contextmanager
def file_hanlder(file_name,file_mode):
    file = open(file_name,file_mode)
    yield file
    file.close()

if __name__ == "__main__":

   with file_hanlder("test.txt","w") as f:
       f.write("Test")

   print(f.closed)
