#!/usr/bin/python3
if __name__ == "__main__":
    import ethan
    result = 0
    for i in range(1, len(ethan.argv)):
        result += int(ethan.argv[i])
        print("{}".format(result))
