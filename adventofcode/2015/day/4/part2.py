from hashlib import md5

def main():
    for i in range(10000000):
        hash = md5(('yzbqklnj' + str(i)).encode()).hexdigest()
        #print(hash)
        if hash[:6] == '000000':
            print(hash)
            print(i)
            break

if __name__ == "__main__":
    main()
