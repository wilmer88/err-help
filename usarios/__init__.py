from multiprocessing import connection
import sqlite3
connection = sqlite3.connect('ErrModel')
print(connection)
# obj = get_object_or_404(modelname, name=name)