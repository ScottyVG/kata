def delete_nth(order,max_e):
    # code here
    # print(len(order))

    # if order == [1,1,1,1] and max_e == 2:
    #     return [1,1]
    if len(order) == 0:
        return []
    else:
        result = order
        check_if_popped = []
        # j_loop = len(order) - 1
        j_loop = len(order)
        count = 0
        # print("j_loop value:")
        # print(result)
        for i in range(0, len(order)):
            # count = 0
            # print("")
            # print("i loop running!!")
            j_loop = j_loop - 1
            # print(j_loop)
            check_if_popped_set = set(check_if_popped)
            if j_loop > 1:
                if order[i] in check_if_popped_set :
                    print("skip if order[i] in check_if_popped_set")
                else:
                    for j in range(0, j_loop):
                    # for j in range(1, j_loop):
                        if j == 0:
                            print("skip if j == 0")
                        else:
                            print("order[j]: " + str(order[j]) + "  order[i]: " + str(order[i]))
                            # print("result[j]: " + str(result[j]))
                            if order[j] == order[i]:
                                count += 1
                                print("count: " + str(count))
                                # if count >= max_e:
                                if count >= max_e - 1:
                                    print("result[j]: " + str(result[j]))
                                    print("result[i]: " + str(result[i]))
                                    print("order[i]: " + str(order[i]))
                                    check_if_popped.append(result[j])
                                    # print("result[j]: " + str(result[j]))
                                    # print("result[i - j]: " + str(result[i - j]))
                                    # result.remove(result[j])
                                    result.pop(order[j])
                                print(result)
                                print("")
        return result


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