# Reinis Grīnbergs, 221rdb053


def parallel_processing(n, m, data):
    output = []
    t = [0] * n
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    for y in range(m):
        xMin = min(enumerate(threads), key=lambda x:x[1])
        output.append((xMin[0], t[xMin[0]]))
        t[xMin[0]] += data[y]


    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines

    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    # TODO: create the function
    result = parallel_processing(n,m,data)

    # TODO: print out the results, each pair in it's own line
    for y, laiks in result:
        print(y, laiks)
if __name__ == "__main__":
    main()
