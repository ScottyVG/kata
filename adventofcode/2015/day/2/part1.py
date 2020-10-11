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
    total_square_feet_of_wrapping_paper = 0

    for i in range(len(dlist)):
        if dlist[i] == ['']:
            del dlist[i]
        else:
            slack = 0
            dlist_total_square_feet = 0
            l = int(dlist[i][0])
            w = int(dlist[i][1])
            h = int(dlist[i][2])
            lw = 2*(l*w)
            wh = 2*(w*h)
            hl = 2*(h*l)
            if (lw <= wh and lw <= hl):
                slack = lw/2
            elif (wh <= lw and wh <= hl):
                slack = wh/2
            elif (hl <= lw and hl <= wh):
                slack = hl/2
            dlist_item_square_feet = lw + wh + hl + slack
            total_square_feet_of_wrapping_paper += dlist_item_square_feet

    print(int(total_square_feet_of_wrapping_paper))

if __name__ == "__main__":
    main()

