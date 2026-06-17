


def main():
    counts = {}
    words = get.words("address.txt")
    lowercase_words = [word.lower() for word in words]

    for word in lowercase_words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    save_counts(counts)


main()
