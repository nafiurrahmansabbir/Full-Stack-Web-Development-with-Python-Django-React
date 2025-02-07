def fun(*argument, **argumentVector):
    print(argument)
    print(argumentVector)

def main():
    print('Main Method')
    fun(a=20,b=30,c="Sabbir")
    
    
if __name__=='__main__':
    main()