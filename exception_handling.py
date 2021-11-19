file_name = "DATA/wombats.txt"
try:
    with open(file_name) as file_in:
        pass
except (FileNotFoundError, PermissionError) as err:
    print(err)


values = [0, 5, 0, 12, 19, 3, 22]
index = 8

try:
    print(values[index])
except IndexError as err:
    print(err)
#    logging.warning(err)
    # with open(....)
    #    file.write(err)
    #    file.write(blah blah)


for v in values:
    try:
        result = 22 / v
    except ZeroDivisionError as err:
        print(err)
    else:
        print(result)


import pymysql

conn = None



try:
    conn = pymysql.connect(
        host="localhost",
        db="presidents",
        user="scripts",
        passwd="scripts",
    )
except Exception as err:
    print("UH-OH", err)
    exit()
else:
    cursor = conn.cursor()
    cursor.execute('select firstname, lastname from presidents where party = "Whig"')
    for row in cursor.fetchall():
        print(row)
finally:
    print("Cleaning up...")
    if conn is not None:
        conn.close()


class MyCustomException(Exception):
    pass

def spam():
    for i in range(10):
        if i == 7:
            raise MyCustomException("We are in trouble")
        print(i)

try:
    spam()
except MyCustomException as err:
    print(err)

print("Done.")


