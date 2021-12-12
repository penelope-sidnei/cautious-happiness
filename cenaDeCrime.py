#“Telefonou para a vítima?”
# “Esteve no local do crime?”
# “Mora perto da vítima?”
# “Devia para a vítima?”
# “Já trabalhou com a vítima?”
# Se a pessoa responder positivamente a 2 questões ela deve ser
#classificada como “Suspeita”, entre 3 e 4 como “Cúmplice” e 5 como
#“Assassino”. Caso contrário, ele será classificado como “Inocente”.

soma=0

print("1 para sim e 0 para nao")

telefone=int (input("Telefonou para a vítima? "))
local=int (input("Esteve no local do crime? "))
morada=int (input("Mora perto da vítima? "))
devedor=int (input("Devia para a vítima? "))
colega=int (input("Já trabalhou com a vítima? "))

soma=telefone+local+morada+devedor+colega
if(soma==2):
    print("Suspeita")

if(soma==3 or soma==4):
    print("Cumplice")

if(soma==5):
    print("Assassino")
    
if(soma==0):
    print("Inocente")
