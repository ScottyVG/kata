import itertools

def main():
    with open("input.txt", "r") as input_file:
        directions = input_file.read()

    def Convert(string): # Convert string to a list by every char
        list1=[] 
        list1[:0]=string 
        return list1 

    dlist = Convert(directions)
    
    stops = [[0,0]]
    gps_cords = [] # [+North -South, +East -West]
    ns = 0
    ew = 0

    for i in range(len(dlist)):
        if dlist[i] == '^':
            ns += 1
        elif dlist[i] == 'v':
            ns -= 1
        elif dlist[i] == '>':
            ew += 1
        elif dlist[i] == '<':
            ew -= 1
        gps_cords = [ns, ew]
        stops.append(gps_cords)

    stops.sort()
    unique_stops = list(stops for stops,_ in itertools.groupby(stops))

    print(len(unique_stops))

if __name__ == "__main__":
    main()
