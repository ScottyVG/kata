# from collections import Counter

def delete_nth(order,max_e):
    # code here
    if not order or max_e < 1:
        return []

    counted_order = { x:0 for x in order }
    new_order = []

    for item in order:
        if counted_order[item] < max_e:
            counted_order[item] += 1
            new_order.append(item)

    return new_order
    # seen = {}
    # result = []
    # for i in order:
    #     if i not in seen:
    #         seen[i] = 0
    #     else:
    #         seen[i] += 1
    #     if seen[i] < max_e:
    #         result.append(i)
    #     return result
    # seen = set()
    # a = [-1, 1, 66.25, 333, 333, 1234.5]
    # result = order
    # return [item for item in result if item not in seen and not seen.add(item)]
    # [-1, 1, 66.25, 333, 1234.5]


    # # seen = set()
    # # [item for item in order if item not in seen and not seen.add(item)]
    # if order == []:
    #     return []
    # else:
    #     seen = set()
    #     return [item for item, count in collections.Counter(order).items if count == max_e]

    #     # return [item for item in order if item not in seen and not seen.add(item)]
    #     # # count = order.count(1)
    #     # # print(count)
    #     # result = order
    #     # for i in range(0, len(order)):
    #     #     count = order.count(order[i])
    #     #     print(count)
    #     #     if count >= max_e + 1:




print("test 1:")
print(delete_nth([], 1))
print("")
print("test 2:")
print(delete_nth([1,1,1,1],2))
print("")
print("test 3:")
print(delete_nth([20,37,20,21], 1))
print("")
print("test 4:")
print(delete_nth([1,1,3,3,7,2,2,2,2], 3))