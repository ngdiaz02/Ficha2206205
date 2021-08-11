def is_int(data):
    if type(data) == int:
        print("este numero es int ", end="")
        #return True
        
    elif type(data) == float:
        print("este numero es float", end="")
        #return False
    else:
        print("este un string")  
    return "no es int ni float ni string"

print(is_int(5))
#print(is_int(5.0))
print(is_int("5"))