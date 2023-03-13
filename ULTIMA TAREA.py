# (1)Lista al cubo
#def elevar_al_cubo(lista):
   # res = []
    #for item in lista:
       # res.append(item ** 3)
    #return res

# casos de prueba
# print(elevar_al_cubo([1, 2, 3, 4, 5]))
# print(elevar_al_cubo([1, 242, 578, 757354873]))
# print(elevar_al_cubo([]))
# print(elevar_al_cubo([3]))

# Usando lambda para elevar al cubo
#nums = [1, 2, 3, 4, 5]
 
#num_3 = list(map(lambda x: pow(x,3),nums))
 
#print(num_3)

# (2)Eliminar los repetidos de una lista
#test_list = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7]
#test_list2 = ["pa", "pa", "pe", "pi"]
#def eliminar_reps(list):
   # res = []
    #for item in list:
        #if item not in res:
            #res.append(item)
    #return res
#print(eliminar_reps(test_list2))
#print(eliminar_reps([]))
#print(eliminar_reps([3,3,3,3,3,3,3]))

# Usando filter para eliminar repetido el (1)

#myList = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7]
#myList = list(filter((1).__ne__, myList))
#print(myList)

# (3)strings intercaladas
def intercalar_strings(str1, str2):
    if len(str1) != len(str2):
        return "Las strings deben ser del mismo largo"
    res = ""
    for i in range(0, len(str1)):
        res += str1[i] + str2[i]
    return res
# str1 = input("Ingrese la primera palabra \n")
# str2 = input("Ingrese la segunda palabra \n")
# print(intercalar_strings(str1, str2))
#interacciones intercaladas
#str1=["sandro"]
#str2=["ugalde"]
#str3=["rojas"]
#str1=list(map(lambda x:x[::-1],str1))
#str2=list(map(lambda x:x[::-1],str2))
#str3=list(map(lambda x:x[::-1],str3))
#print(str1)
#print(str2)
#print(str3)

# (4)Eliminar los pares de una lista
#test_list = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7]
#test_list2 = ["pa", "pa", "pe", "pi"]
#def eliminar_reps(list):
   # res = []
    #for item in list:
        #if item not in res:
            #res.append(item)
    #return res
#print(eliminar_reps(test_list2))
#print(eliminar_reps([]))
#print(eliminar_reps([3,3,3,3,3,3,3]))

# Usando filter y lambda para eliminar pares ()
#lst = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7]
#odd = filter(lambda x: x%2, lst)
#print(list(odd))
