def main():
    while True:
        try:
            fraction = input("Enter a fraction as x/y: ")
            x, y = map(int, fraction.split("/"))
            if y == 0 or x > y:
                continue
            percentage = (x / y) * 100
        except ZeroDivisionError:
                print("Cannot divide by zero")
                continue
        except ValueError:
                print("Fraction must be formatted as x/y")
                continue
        if percentage <=1:
            print("E")
        elif percentage >=99:
            print("F")
        else:
            print(f"{round(percentage)}%")
        break

main ()


