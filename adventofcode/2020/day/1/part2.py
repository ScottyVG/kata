def main():
    with open("input.txt", "r") as input_file:
        input_data = input_file.read()

    li = list(input_data.split("\n"))

    print (li)
    for i in range(len(li)):
        for j in range(len(li)):
            for k in range(len(li)):
                if (int(li[i]) + int(li[j]) + int(li[k])) == 2020:
                    print(int(li[i]) * int(li[j]) * int(li[k]))
                    return(int(li[i]) * int(li[j]) * int(li[k]))

if __name__ == "__main__":
    main()

