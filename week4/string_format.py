def C_to_F(celcius):
    return (celcius * 9/5) + 32

def main():
    list_celcius = [20.4, 30.5, 40.6, 50.7, 60.8, 70.9]
    print('{0:-<9} | {1:->11}'.format('Celcius', 'Farenheit')) 
    # {value:[padding_char][alignment][width].precision}
    for cel in list_celcius:
        print('{0:<9} | {1:11.5f}'.format(cel, C_to_F(cel)))

if __name__ == '__main__':
    main()

