def main():
    time = input("What is the time? ")
    f = convert(time)
    if 7 <= f <= 8:
        print("breakfast time")
    elif 12 <= f <= 13:
        print("lunch time")
    elif 18 <= f <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    f = float(hours) + float(minutes) / 60
    return f



if __name__ == "__main__":
    main()
