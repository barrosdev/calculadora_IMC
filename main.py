altura = float(input('Qual e a sua altura em cm: ')) 
peso = float(input('Qual e o seu peso em kg: '))

IMC = peso / (altura/100)**2

print(IMC)

if IMC < 18.5:
 print(f'seu IMC e de {IMC}, e é classificado como MAGREZA')


elif IMC >= 18.5 and IMC < 24.9:
  print(f'seu IMC e de {IMC}, e é classificado como NORMAL')


elif IMC >= 25 and IMC < 29.9:
  print(f'seu IMC e de {IMC}, e é classificado como SOBREPESO')

elif IMC >= 30 and IMC < 39.9:
  print(f'seu IMC e de {IMC}, e é classificado como OBESIDADE')


else:
   print("pode parar de comer e começar a malhar pois o négocio esta feio! OBESIDADE GRAVE ")

  

#MENOR QUE 18,5  	 MAGREZA	0
#ENTRE 18,5 E 24,9 NORMAL	0
#ENTRE 25,0 E 29,9 SOBREPESO	I
#ENTRE 30,0 E 39,9 OBESIDADE	II
#MAIOR QUE 40,0   OBESIDADE GRAVE	III