import simplecrypt
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

# получим объект файла
file1 = open("passwords.txt", "r")

while True:
    # считываем строку
    line = file1.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    # выводим строку
    try:
        print(simplecrypt.decrypt(line.strip(), encrypted))
    except:
        print('no')

# закрываем файл
file1.close
