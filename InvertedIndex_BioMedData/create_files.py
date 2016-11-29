#http://stackoverflow.com/questions/10978869/safely-create-a-file-if-and-only-if-it-does-not-exist-with-python#
import os
import errno
import numpy as np
import csv
import pandas as pd
import codecs
def create_file(name, data):
    flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
    try:
        file_handle = os.open(name, flags)
    except OSError as e:
        if e.errno == errno.EEXIST:  # Failed as the file already exists.
            pass
        else:  # Something unexpected went wrong so reraise the exception.
            raise
    else:  # No exception, so the file must have been created successfully.
        with os.fdopen(file_handle, 'w') as file_obj:
            # Using `os.fdopen` converts the handle to an object that acts like a
            # regular Python file object, and the `with` context manager means the
            # file will be automatically closed when we're done with it.
            file_obj.write(data)

def dataFromFile():
    df = pd.read_csv("sample200.csv")
    return df.Abstract

data = dataFromFile()
array = np.empty(200)
for number in range(200):
    array[number] = number
    name = str(int(array[number]))+".txt"
    text = data[number]
    create_file(name, text)
    # with codecs.open(name,'r',encoding='utf8') as f:
    #     texted = f.read()
    # # process Unicode text
    # with codecs.open(name,'w',encoding='utf8') as f:
    #     f.write(texted)



