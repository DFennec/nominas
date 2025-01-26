letrasNIF={0:"T",1:"R",2:"W",3:"A",4:"G",5:"M",6:"Y",7:"F",8:"P",9:"D",10:"X",
          11:"B",12:"N",13:"J",14:"Z",15:"S",16:"Q",17:"V",18:"H",19:"L",20:"C",
          21:"K",22:"E"}
letrasNIE={"X":"0","Y":"1","Z":"2"}#suma de cara a al clave de la letraNIF
checksum=0
from math import trunc
opcion=""
def nifNie(documento):
    if documento=="":
        documento=input("Introduce un NIF/NIE:").replace(" ", "")
        
    if len(documento)==9:
        numeroDocumento=documento[0:8]
        
        if not documento[0].isnumeric() and documento[0].upper() in letrasNIE:
            numeroDocumento=letrasNIE[documento[0].upper()]+documento[1:8]
        elif not documento[0].isnumeric() and not documento[0].upper() in letrasNIE:
            return print("ERROR - documento no válido: letra NIE no válida")
        
        numeroDocumento=int(numeroDocumento)
        checksum=numeroDocumento-trunc(numeroDocumento/23)*23
        
        if letrasNIF[checksum]!=documento[8]:
            return print("ERROR - documento no válido: código de control no coincidente")
    else:
        return print("ERROR - documento no válido: longitud inapropiada")
def naf(documento):
    if documento=="":
        documento=input("Introduce un NAF:").replace(" ", "")
        
    A=documento[0:2]
    
    if len(documento)==12:
        B=documento[2:10]
        C=documento[10:12]
        AB=A+B
        
        if int(C)!=int(AB)%97:
            return print("ERROR - documento no válido: código de control no coincidente")
        else:
            return
            
    if len(documento)==11:
        B=documento[2:9]
        C=documento[9:11]
        
        if int(C)!=(int(B)+int(A)*10000000)%97:
            return print("ERROR - documento no válido: código de control no coincidente")
        else:
            return
    else:
        return print("ERROR - documento no válido: longitud inapropiada")
def ccc(documento):
    if documento=="":
        documento=input("Introduce un CCC:")
    if len(documento)==20:
        entidad=documento[0:4]
        sucursal=documento[4:8]
        dControl=documento[8:10]
        cCuenta=documento[10:20]
        
        dc1=(int(entidad[0])*4+int(entidad[1])*8+int(entidad[2])*5+int(entidad[3])*10)+(int(sucursal[0])*9+int(sucursal[1])*7+int(sucursal[2])*3+int(sucursal[3])*6)
        dc1=11-(dc1%11) if 11-(dc1%11)!=10 else 1
        dc2=(int(cCuenta[0])*1+int(cCuenta[1])*2+int(cCuenta[2])*4+int(cCuenta[3])*8+int(cCuenta[4])*5+int(cCuenta[5])*10+int(cCuenta[6])*9+int(cCuenta[7])*7+int(cCuenta[8])*3+int(cCuenta[9])*6)
        dc2=11-(dc2%11) if 11-(dc2%11)!=10 else 1
        
        dc=str(dc1)+str(dc2)
        if dc!=dControl:
            return print("ERROR - documento no válido: Código de control no coincidente")
    else:
        return print("ERROR - documento no válido: longitud inapropiada")
        
def princ(opcion):    
    opcion=opcion.upper().replace(" ","")
    if opcion=="NIF" or opcion=="NIE":
        nifNie("")
    elif opcion=="NAF":
        naf("")
    elif opcion=="CCC":
        ccc("")
    elif opcion=="SALIR":
        return "Has salido del programa."
    else:
        if len(opcion)==9:
            nifNie(opcion)
        elif len(opcion)==11 or len(opcion)==12:
            naf(opcion)
        elif len(opcion)==20:
            ccc(opcion)
        else:
            return "ERROR - documento no válido: longitud inapropiada"
        