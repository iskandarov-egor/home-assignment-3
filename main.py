from calculator import calc

if __name__ == '__main__':
    while True:
        try:
            p = raw_input('enter expression or press enter to exit:')
            if p == '':
                break
            print 'answer is: ' + str(calc(p))
        except ZeroDivisionError:
            print 'cannot divide by zero'
        except (ValueError, IndexError):
            print 'invalid expression'