def sign_up():
    print('SIGN UP')
    name = input('Full Name :')
    num = input('Number :')
    user = input('User Name :')
    pas = input('Create Password :')
    print('\n')
    print('Cheak information')
    print('Name :' + name + '.' )
    print('Number :' + num + '.' )
    print('User Name :' + user + '.' )
    print('Password:' + pas + '.')
    print('Sucessfuly Sign Up')
def calculator():
    def addition(x, y):
        return x + y

    def minus(x, y):
        return x - y

    def into(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "Cannot divide by zero"
            return x / y
    
    print('Mr.Error ! ')
    print("Leon Khan's Calculator 📲🧮\nSelect operation ☞")
    print("1. addition")
    print("2. Minus")
    print("3. into")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", addition(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", minus(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", into(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid Input")
        
def log_in():
    print('Enter User Name & Password')
    a = input('User Name :')
    b = input('Password :')
    if a == 'leonkhan08' and b == 'Leonkhan2424' :
        print('Secussfully Login\n')
        print(calculator())
    else :
        print('Incorract user name or passwoad')
def  start():
    print('Welcome to this page')
    print('1. Login \n2. Sign Up')
    a = input  ('Enter choice :') 
    if a == '2':
        print(sign_up())
    elif a == '1':
        print(log_in())      
    else :
        print('Invalid Input')
        
        
start()

    