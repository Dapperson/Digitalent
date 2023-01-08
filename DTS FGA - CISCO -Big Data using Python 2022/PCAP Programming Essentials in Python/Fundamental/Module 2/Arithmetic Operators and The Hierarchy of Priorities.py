# Penjumlahan (+)
print(2+2)
print()

# Selisih (-)
print(4-2)
print()

print(-4 + 4)
print(-4. + 8)
print(-4 - 4)
print(4. - 8)
print(-1.1)
print(+2)
print()

# Eksponential / Pangkat (**)
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
print()

# Perkalian (*)
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)
print()

# Pembagian (/)
print(6 / 3) # walaupun kedua bilangan integer, tetap hasilnya float karena pembagian
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
print()

# Pembagian dibulatkan kebawah (//)
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
print()

print(6 // 4)
print(6. // 4)
print()

print(-6 // 4)
print(6. // -4)
print()

# Modulus / Sisa Bagi (%)
print(14 % 4)
print(12 % 4.5)

#Exponensasi
print(2 ** 2 ** 3) # penghitungan dilakukan dari kanan ke kiri (2**(2**3))

#Operator Prioritas
'''
tanda kurung dikerjakan terlenih dahulu "()"
dan dari kiri ke kanan bila tingkat prioritas sama
1. **
2. / // * %
3. + -
'''
print(2 * 3 % 5)
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2 ** 3 ** 2))