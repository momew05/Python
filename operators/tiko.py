import sys

shelf = {
    "онигири": {"price": 85.55, "quantity": 100},
    "вода": {"price": 60.99, "quantity": 20},
    "жвачка": {"price": 52.67, "quantity": 50},
    "редбулл кокос": {"price": 1000, "quantity": 0},    
}

allowed_coupons = ["SALE20", "NEWYEAR", "VIP", "HELPME"]

class order:
    def __init__(self, shoplist, money, member, coupon):
        self.products = {}

        for item in shoplist.split(","):
            parts = item.strip().split()

            name = " ".join(parts[:-1])
            quantity = int(parts[-1])

            self.products[name] = quantity

        self.ismember = True if member.lower() == "да" or member.lower() == "yes" else False
        self.coupon = coupon
        self.money = int(money)
        
myorder = order(
    input("ЧТо вы хотите купить?\n").lower(),
    input("СКолько ВЫ готовы заплатить??\n"),
    input("вы MEMBER??\n"),
    input("УВАс ЕСТЬ купонкод??? надо ВвE$ти\n")
) #здесь как будто стало очевидно что класс был не нужен НО я не буду переписывать мне на что 32 гб оперативки правильно 

total = 0

for name in myorder.products:
    if name in shelf and shelf[name]["quantity"] >= myorder.products[name]:
        total += shelf[name]["price"] * myorder.products[name]
    elif name not in shelf:
        print(f'у нас нет товара {name}, уходиТЕ')
        sys.exit()
    else:
        print(f'у нас только {shelf[name]["quantity"]} товара {name}, уходиТЕ')
        sys.exit()

if myorder.money >= total:
    total = myorder.money

if myorder.coupon in allowed_coupons and total >= 1000:
    discount = (total*0.2)
    dtotal = total - discount
elif myorder.ismember:
    discount = (total*0.05)
    dtotal = total - discount
else:
    discount = 0
    dtotal = total

tax = (dtotal * 0.13)
tdtotal = dtotal + tax
bonus = (tdtotal * 0.01)//1 + len(myorder.products)**2

print(f'ВашЬ ЧекЪ')
for name in myorder.products:
    print(f'ТОвар: {str(name)}\n Цена за шТуку: {shelf[name]["price"]}\n КоличествО: {myorder.products[name]}')
print(f'Сумма до скидки: {total}\n Скидка: {discount}\n Сумма после скидки: {dtotal}\n Налог (13%): {tax}\n ИТОГО к оплате: {tdtotal}')
print(f'Начислено баллов: {bonus} (вкл. бонус за объем: {len(myorder.products)**2})')
print(f'Тип данных суммы: {type(tdtotal)}')
