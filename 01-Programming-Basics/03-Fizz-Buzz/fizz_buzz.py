# Start with some pseudo-code!
# for n from 1 to 16
#     if n is divisible by 3
#         print 'fizz'
#     else if n is divisible by 5
#         print 'buzz'
#     else if n is divisible by 3 and by 5
#         print 'fizzbuzz'
#     else
#         print n

for n in range(1, 15 + 1):
    if n%5==0 and n%3==0:
        print('fizzbuzz')
    elif n % 3 == 0:
        print('fizz')
    elif n % 5 == 0:
        print('buzz')
    else:
        print(n)
    