
mountain = [
          "^^^^^^        ",
          " ^^^^^^^^     ",
          "  ^^^^^^^     ",
          "  ^^^^^       ",
          "  ^^^^^^^^^^^ ",
          "  ^^^^^^      ",
          "  ^^^^        "
        ]  

def list_to_str(list):
    st = ''
    for i in list:
        st += i
        st += '\n'
    return st

def del_and_add_str(st,id,num):
    return st[:id] + str(num) + st[id+1:]

def sum_str(list):
    sum = 0
    for i in list:
        if i in ['1','2','3','4','5','6','7','8','9','0']:
            sum += int(i)
    return sum

def peak_height(mountain:list, n):
    mountain.insert(0,'              \n')
    mountain.append('              ')


    cont = 1
    while cont >= 1:
        cont = 0
        for i in range(len(mountain)):
            for j in range(len(mountain[i])):
                if mountain[i][j] == '^':
                    neighbors =[mountain[i+1][j],mountain[i-1][j],mountain[i][j+1],mountain[i][j-1]]
                    n = 0
                    while n < len(neighbors):
                        if neighbors is None:
                            break
                        elif neighbors[n] == ' ':
                            mountain[i] = del_and_add_str(mountain[i],j,1)
                            neighbors.pop(n)
                            n -= 1
                        elif neighbors[n] == '^':
                            neighbors.pop(n)
                            n -= 1
                        n += 1
                    if mountain[i][j] != '1' and sum_str(neighbors)<6:
                        mountain[i] = del_and_add_str(mountain[i],j,2)
                    print(list_to_str(mountain))
                    
                    cont += 1
    

    k = 2
    while k <= n:
        for i in range(len(mountain)):
            for j in range(len(mountain[i])):
                if mountain[i][j] not in [' ', '1', '\n'] and mountain[i][j] not in [str(i) for i in range(k-1)]:
                    neighbors =[mountain[i+1][j],mountain[i-1][j],mountain[i][j+1],mountain[i][j-1]]
                    if set([str(i) for i in range(k)]) - set(neighbors) is None:
                        self_max = (sum_str(neighbors)//4)+1
                    else:
                        self_max = int(min(neighbors))+1
                    mountain[i] = del_and_add_str(mountain[i],j,self_max)
        k += 1            
                





    return mountain
                    
                    
print(list_to_str(peak_height(mountain,3)))