'''You are given a complex . Your task is to convert it to polar coordinates.'''
import cmath
print(*cmath.polar(complex(input())), sep='\n')

# polar = [c for c in input() if c not in "+j"]
# indexes = [i for i in range(len(polar)) if polar[i] == '-']
# if len(polar) > 2:
#     polar = map(int, [c for c in polar if c not in "-"])
#     print(*polar)
#     polar = [-polar[i] for i in range(2) if indexes[i] == '-'] 
#     print(polar)
# polar = list(map(int, polar))
# print(polar)
# print(abs(complex(polar[0], polar[1])))
# print(cmath.phase(complex(polar[0], polar[1])))

