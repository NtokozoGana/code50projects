def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0:2].isalpha():
        return False
    if not s.isalnum():
        return False
    seen_number = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not seen_number:
                seen_number = True
                if char == "0":
                    return False
            if not s[i:].isdigit():
                return False
    return True

if __name__ == "__main__":
    main()
