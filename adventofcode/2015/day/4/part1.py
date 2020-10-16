from hashlib import md5

def main():
    test = md5(('abcdef' + str(609043)).encode()).hexdigest()
    print(test)

    test2 = md5(('pqrstuv' + str(1048970)).encode()).hexdigest()
    print(test2)

    for i in range(10000000):
        hash = md5(('yzbqklnj' + str(i)).encode()).hexdigest()
        #print(hash)
        if hash[:5] == '00000':
            print(hash)
            print(i)
            break

if __name__ == "__main__":
    main()
