import random

sample = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]

def main():
    print("Steam Code Generator V1.0 by @acidum#0230")
    print("Give me some upvotes!")

    try:
        codesToGenerate = int(input("Please enter the number of codes you want to generate. (NUMBERS HIGHER THAN TEN MILLION CAN CAUSE ISSUES!)\n"))
    except Exception:
        print("Invalid input. Must be a whole, positive integer.\n")
        main()

    fileToWrite = input("Please enter a filename you would like to write to. (Will write to a .txt file)")

    confirm = input("Are you sure you want to continue? y/n\n")

    if confirm == "y":
        print("Generating...\n")
    else:
        main()

    f = open(fileToWrite + ".txt", "a")

    for loop in range(codesToGenerate):
        
        code = ""
        countOfDashes = 0

        for loop in range(3):
            for loop in range(5):
                char = random.choice(sample)
                code += char

            if countOfDashes != 2:
                code += "-"
                countOfDashes += 1

        f.write("\n{}".format(code))
        
    print("Done!\n")
    f.close()
    main()

if __name__ == "__main__":
    main()
