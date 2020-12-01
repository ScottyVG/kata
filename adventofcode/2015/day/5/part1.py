def main():
    with open("input.txt", "r") as input_file:
    dimensions = input_file.re ad()

    def Convert(string): # Python code to convert string to list 
        li = list(string.split("\n"))
        for i in range(len(li)):
            if li[i] == ['']:
                del li[i]
            else:
                li[i] = list(li[i].split("x"))
        return li

if __name__ == "__main__":
    main()
