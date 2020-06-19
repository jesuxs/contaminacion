sin_confirmar=["marco","chata","andrea"]
confirmar=[]
while sin_confirmar:
    personas_confirmando=sin_confirmar.pop()
    confirmar.append(personas_confirmando)
    
del confirmar[1]

print(confirmar)
