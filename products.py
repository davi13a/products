products = []
while True:
    name = input('請輸入商品名稱（q為結束）： ')
    if name == 'q':
        break
    price = input('請輸入商品價格： ')
    #p = []
    #p.append(name)
    #p.append(price)
    p = [name, price]
    products.append(p)
    #products.append([name, price])
print(products)

#products[0][0]
#products[1][0]

for pp in products:
    print(pp[0], '的價格是', pp[1])

