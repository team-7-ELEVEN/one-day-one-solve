def main():
    N = int(input())
    
    cnt = 0
    start = 665

    while True:

        start+=1
        
        if '666' in str(start):
            cnt+=1

        if cnt == N:
            break

    print(start)        
    
if __name__=="__main__":
    main()