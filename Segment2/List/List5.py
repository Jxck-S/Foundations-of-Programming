# Lists in Python

def main():

    names = ["Chewy", "Spock", "Hermione", "Storm", "Rex"]
    photos = [45, 12, 33, 24, 106]
    total = 0

    for n in range(0, len(names)):
        print(names[n] + " took " + str(photos[n]) + " photos.")
        total = total + photos[n]

    print("Total photos taken: " + str(total))

main()