def main():
    with open("input.txt", "r") as input_file:
        directions = input_file.read()

    floor = 0
    
    def Convert(string): # Convert string to a list by every char
        list1=[] 
        list1[:0]=string 
        return list1 

    dlist = Convert(directions)

    for i in range(0, len(dlist)):
        if dlist[i] == "(":
            floor += 1
        elif dlist[i] == ")":
            floor -= 1
    
    print(floor)

if __name__ == "__main__":
    main()

