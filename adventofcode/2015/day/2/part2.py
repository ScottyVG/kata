def main():
    with open("input.txt", "r") as input_file:
        dimensions = input_file.read()

    def Convert(string): # Python code to convert string to list 
        li = list(string.split("\n"))
        for i in range(len(li)):
            if li[i] == ['']:
                del li[i]
            else:
                li[i] = list(li[i].split("x"))
        return li

    dlist = Convert(dimensions)
    feet_of_ribbon = 0 
    for i in range(len(dlist)):
        if dlist[i] == ['']:
            del dlist[i]
        else:
            shortest_distance_around_its_sides = 0
            cubic_volume = 0
            l = int(dlist[i][0])
            w = int(dlist[i][1])
            h = int(dlist[i][2])
            cubic_volume = l*w*h
            lwh = [l, w, h]
            shortest_distance_around_its_sides = (2 * sorted(lwh)[0]) + (2 * sorted(lwh)[1])
            feet_of_ribbon += (shortest_distance_around_its_sides + cubic_volume)

    print(int(feet_of_ribbon))

if __name__ == "__main__":
    main()

