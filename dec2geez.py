digits = {
    0: "", 1: "፩", 2: "፪", 3: "፫", 4: "፬", 5: "፭",
    6: "፮", 7: "፯", 8: "፰", 9: "፱", 10: "፲",
    20: "፳", 30: "፴", 40: "፵", 50: "፶",
    60: "፷", 70: "፸", 80: "፹", 90: "፺",
    100: "፻", 10000: "፼"
}

def dec2geez(number):
    if number < 10:
        return digits[number]

    if number < 100:
        tens, ones = divmod(number, 10)
        return digits[tens * 10] + digits[ones]

    for divisor, symbol in [(10000, digits[10000]), (100, digits[100])]:
        if number >= divisor:
            quotient, remainder = divmod(number, divisor)
            return (dec2geez(quotient) if quotient > 1 else "") + symbol + (dec2geez(remainder) if remainder else "")

    return ""

#for i in range(1,1000001):
#    print(f"{i};{dec2geez(i)}")

if __name__ == "__main__":
    import sys
    try:
        input_number = int(sys.argv[1])
        if input_number < 0:
            print("Please enter a number greater than or equal to zero.")
        elif input_number == 0:
            print("Zero is not represented in Geez numerals.")
        else:
            print(dec2geez(input_number))
    except IndexError:
        print("Please enter a number as an argument when running the script.")
    except ValueError:
        print("Please enter a valid integer.")
