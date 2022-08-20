def main():
    N = int(input())
    data = []
    for _ in range(N):
        x=input()
        data.append(x)
    
    data=list(set(data))

    data_set=[]
    for i in data:
        data_set.append((i,len(i)))


    solve = sorted(data_set , key = lambda x : (x[1],x[0]))

    for i in range(len(solve)):
        print(solve[i][0])

if __name__=="__main__":
    main()