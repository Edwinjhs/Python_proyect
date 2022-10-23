def num_primo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            

def resultado():
    num = int(input("Ingresa un numero:"))
    result = num_primo(num)

    if result is True:
        print("El numero ",num ,"es primo")
    else:
        print("El numero ", num ,"no es primo")
resultado ()
