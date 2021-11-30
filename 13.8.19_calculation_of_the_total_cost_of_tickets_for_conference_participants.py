# Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов. Программа должна работать следующим образом:

# 1. В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.

# 2. Далее для каждого билета запрашивается возраст посетителя, в соответствии со значением которого выбирается стоимость:
#   - Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
#   - От 18 до 25 лет — 990 руб.
#   - От 25 лет — полная стоимость 1390 руб.

# 3. В результате программы выводится сумма к оплате. При этом, если человек регистрирует больше трёх человек на конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.


price_common = 0
while True:
    try:
        Nr_Tickets = int(input("please enter which number of tickets do you need: "))
        if type(Nr_Tickets) == int:
            break
    except ValueError:
        print('Введите целое число')

for i in range (Nr_Tickets):                         
    age_for_ticket = int(input("For which age is a needed Ticket №{i}? : "))
    while True:
        if age_for_ticket < 18:
            print('entry free of cost')
            break
        elif 18 <= age_for_ticket < 25:
            print('your costs are 990 RUB per Ticket')
            price_common += 990
            break
        elif 25 < age_for_ticket:
            price_common += 1390
            print('your costs are 1390 RUB per Ticket')
            break
    continue

if Nr_Tickets > 3:
    price_common = price_common - (price_common * (10 / 100))
    print('Сумма к оплате руб. с 10%-ой скидкoй на полную стоимость заказа за регистрацию больше 3-и человек: ', price_common)
else:
    print('Сумма к оплате руб.: ', price_common)  


