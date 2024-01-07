def operasi(op):
    def sisagold(a,b):
        return a - b
    if op == '-':
        return sisagold

sisagold = operasi('-')
print(f"hasil = {sisagold(2,3)}")