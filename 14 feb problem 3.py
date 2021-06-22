def stock_availability (sh, parametar, *args):

    shop = sh

    if parametar == "delivery":
        for i in args:
            shop.append(i)
    elif parametar == "sell":
        if args:
            for j in args:
                if type(j) == int:
                    for k in range(j):
                        shop.pop()
                else:
                    if j in shop:
                        how_itaims = shop.count(j)
                        for h in range(how_itaims):

                            shop.remove(j)
        else:
            shop.remove(shop[0])


    return shop
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))