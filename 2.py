katetA,katetB,gepotenuzaC = float(input('Катет A = ')),float(input('Катет B = ')) ,float(input('Гипотенуза = ')) 
print('Площадь треугольника = ',katetA*katetB/2) if katetA**2 + katetB**2 == gepotenuzaC**2 else print('Ошибка, данный треугольник не является прямоугольным')
print( 'Периметр треугольника = ',katetA + katetB + gepotenuzaC)
