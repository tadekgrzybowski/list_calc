
def sort_asc(lista):
    return sorted(lista)

def sort_desc(lista):
    return sorted(lista,reverse=True)

def double(lista):
    return [x*2 for x in lista]

if __name__ == '__main__':
    lista = [4,7,2,3,4,8,9,10]
    print("------------------------------------")
    print(" --> Program wykonuje operacje na listach <----")
  
    while True:
        print("\n-----------------")
        print("Lista: "+str(lista))

        print(" 's' - sortuj malejąco")
        print(" 'S' - sortuj rosnąco")
        print(" '2 - pomnoz elementy * 2")
        print(" '+ - dodaj elementy")
        print(" 'm' - największy element")
        print(" 'q' - wyjscie")

        c = input(" Wybierz operację --> ")
        if c != 'q':
            if c == 's':
                lista = sort_desc(lista)
            elif c == 'S':
                lista = sort_asc(lista)
            elif c == '+':
                suma = sum(lista)
                print(f"Suma: {suma}")
            elif c == '2':  
                lista = double(lista) 
            elif c == 'm':
                print("Największy element: {}".format(max(lista)))
        else:
            break