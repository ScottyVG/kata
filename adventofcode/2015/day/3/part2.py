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
    real_gps_cords = [] # [+North -South, +East -West]
    robo_gps_cords = [] # [+North -South, +East -West]
    real_santa_ns = 0
    real_santa_ew = 0
    robo_santa_ns = 0
    robo_santa_ew = 0

    for i in range(len(dlist)):
        if (i % 2 == 0):
            if dlist[i] == '^':
                robo_santa_ns += 1
            elif dlist[i] == 'v':
                robo_santa_ns -= 1
            elif dlist[i] == '>':
                robo_santa_ew += 1
            elif dlist[i] == '<':
                robo_santa_ew -= 1
            robo_gps_cords = [robo_santa_ns, robo_santa_ew]
            stops.append(robo_gps_cords)
        elif (i % 2 != 0):
            if dlist[i] == '^':
                real_santa_ns += 1
            elif dlist[i] == 'v':
                real_santa_ns -= 1
            elif dlist[i] == '>':
                real_santa_ew += 1
            elif dlist[i] == '<':
                real_santa_ew -= 1
            real_gps_cords = [real_santa_ns, real_santa_ew]
            stops.append(real_gps_cords)

    stops.sort()
    # find unique items in a list of lists
    unique_stops = list(stops for stops,_ in itertools.groupby(stops))
    print(len(stops))
    print(len(unique_stops))

if __name__ == "__main__":
    main()
