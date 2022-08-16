def main():
    
    while True:
        st = input()
        st = int(st)
        if st == 0:
            break
        st = str(st)
        if st == st[::-1]:
            print("yes")
        else:
            print("no")
    
if __name__=="__main__":
    main()
