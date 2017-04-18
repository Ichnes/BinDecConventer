#from decimal to binary
def converter_binary(number):
    a = []
    #print(number)
    while number > 0:
        a.append(number % 2)
        number = int(number / 2)
    print_backward(a)
    print (" 2")

#from binary to decimal
def converter_decimal(number):
    decimal = 0
    for digit in str(number):
        decimal = decimal*2 + int(digit)
    print (decimal, "10")

#to write function backward
def print_backward(table):
    length = len(table) - 1
    while length >= 0:
        print(table[length], end='')
        length -= 1

while True:
    def main():
        type_number = print (""" Welcome in binary/decimal to and fro converter
        Type number than space and 2 or 10. For example : 10101 2 --> you write number 10101
        in binary system. Program convert that number into decimal. """)
        input_read = input()
        try:
            input_read = input_read.split()
            number = int(input_read[0])
            system = int(input_read[1])
            if system == 10:
                converter_binary(number)
            elif system == 2:
                converter_decimal(number)
        except IndexError:
            print("Please, use only corret form.")

    main()
    ask = ""
    while not (ask == 'YES' or ask== 'NO'):                                
        ask = input("Do you want to try again? (YES/NO) ").upper()
    if ask == 'NO':
        break
