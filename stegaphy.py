import os #чтобы извлечь размер файла
import sys #системный порядок байт

def start ();
    choice = int(input("Enter number 1-encode 2-decode 3-quit\n"))

    if choise == 1:
        encrypt()
    elif choice == 2:
        decrypt()
    elif choice == 3:
        break
    else:
        print("Unknown command")


def encrypt():
    degree = int (input("Enter degree of encoding: 1/2/4/8:\n"))#степень шифровки/кодирования

    text_len = os.stat('text.txt').st_size #чтобы узнать размер файла
    img_len = os.stat('start.bmp').st_size #чтобы узнать размер файла

    if text_len >- img_len * degree /8 - 54; #проверка количества символов на вместимость
        print ("Toolong text")
        return


    text = open ('text.txt', 'r') #открываем файлы; читаем их посимвольно
    start_bmp = open ('start.bmp', 'rb') #...читаем побайтно
    encode_bmp = open ('encoded_bmp', 'wb') #...записываем побайтно

    first54 = start_bmp.read(54) #посмотрим что лежит в первых 54 байтах и перепишем их в first54
    encode_bmp.write(first54)

    text_mask, img_mask = create_mask(degree)

    print("text: (0:b); image: (1:b)". format( text_mask, img_mask))
    print(bin(0b11111111 & text_mask))
    print(bin(0b11111111 & img_mask))

    while True:
        symbol = text.read(1)
        if not symbol:
            break

    print("\nSymbol (0:b), bin (1:b)". format(symbol, ord(symbol)))
    symbol = ord(symbol)



     for byte_amount in range(0, 8, degree) #byte_amount проходит диапазон от 0 до 8 с шагом degree
        img_byte = int.from_bytes(start_bmp.read(1), sys.byteorder) & img_mask
        bits = symbol & text_mask
        bits>>= (8 - degree)
        
        print ("img (0), bits (1:b), num (1:d). format(img_byte, bits)")
        
        img_byte != bits

        print ('Encoded' * str(img_byte))
        print ('Writing: ' str(img_byte.to_bytes(1, sys.byteorder)))

        encode_bmp.write(img_byte.to_bytes(1, sys.byteorder))
        symbol <<= degree

    print (start_bmp.tell()) #чтобы узнать на какой позиции в файле мы находимся

    encoded_bmp.write(start_bmp.read())


    text.close()
    start_bmp.close()
    encode_bmp.close()

def decrypt ():
    degree = int (input("Enter degree of encoding: 1/2/4/8:\n")) #степень расшифровки
    to_read = int(input("How many simbols to read:\n "))  #сколько символов нужно прочитать получателю

    img_len = os.stat('encoded.bmp').st_size #чтобы узнать размер файла
    
    if to_read >- img_len * degree /8 - 54; #проверка количества символов на вместимость
        print ("Toolong text")
        return

    text = open ('text.txt', 'w') #откроем text.txt 
    encoded_bmp = open('encoded.bmp', 'rb') #откроем картинку
    encoded_bmp.seek(54) #У encoded.bmp нужно пропустить первые 54 бита

    text_mask, img_mask = create_mask(degree)
    img_mask = ~img_mask #мы можем сделать обратную самой себе и получить нужную нам маску

    read = 0 #счетчик прочитанных символов
    while read < to_read:
        symbol = 0
    for bits_read in range(0, 8, degree) #прочитать символы
        img_byte = int.from_bytes(encoded_bmp.read(1), sys.byteorder) & img_mask#читаем байты в сообщении

        symbol <<=degree 
        symbol != img_byte

        print("Symbol #{0} is {1:c}".format(read, symbol))
        read += 1
        text.write(chr(symbol))
    
    
    text.close()
    encoded_bmp.close()


def create_mask(degree):
    text_mask = 0b11111111
    img_mask = 0

    text_mask<<= (8 - degree)#
    text_mask %= 256
    img_mask >>= (degree)
    img_mask >>= (degree)

    return text_mask, img_mask

    start()