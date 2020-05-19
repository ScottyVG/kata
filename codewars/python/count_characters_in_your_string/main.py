def count(string):
    # The function code should be here
    result = {}

    if len(string) == 0:
        return result
    else:
        for element in range(0, len(string)): 
            count = 0
            count = string.count(string[element])
            result.update( {string[element]: count} )
    return result