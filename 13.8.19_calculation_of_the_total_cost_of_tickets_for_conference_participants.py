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
        print('please enter int_type')

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
    print('Sum to be paid RUB with a 10% discount on the full cost for registration more than 3 people: ', price_common)
else:
    print('Sum to be paid RUB: ', price_common)  


