def main():
    with open("input.txt", "r") as input_file:
        input_data = input_file.read()

    li = list(input_data.split("\n"))

    print (li)
    for i in range(len(li)):
        for j in range(len(li)):
            if int(li[i]) + int(li[j]) == 2020:
                print(int(li[i]) * int(li[j]))
                return(int(li[i]) * int(li[j]))

if __name__ == "__main__":
    main()

