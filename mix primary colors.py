first_color = input('select a primary color:')
second_color = input('select anouther primary  color:')

if first_color == 'red' and second_color == 'blue' or first_color == 'blue' and second_color == 'red':
    print ('purple')
elif first_color == 'red' and second_color ==  'yellow' or first_color == 'yellow' and second_color == 'red':
    print ('orange')
elif first_color == 'blue' and second_color == 'yellow' or first_color == 'yellow' and second_color == 'blue':
    print ('green')
else:
    print ('you havent selected two primary colors')