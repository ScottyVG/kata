def number(lines):
    #your code here
    result = []
    # print(len(lines))

    if lines == result:
        return result
    else:
        line_number = 0
        for i in range(0, len(lines)): 
            line_number = line_number + 1
            result_item = str(line_number) + ": " + str(lines[i])
            # print(result_item)
            result.append(result_item)
    return result

print(number([]))
print(number(["a", "b", "c"]))

'''
https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python

def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]
'''