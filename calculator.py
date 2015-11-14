minus_replacement = 'm'
plus_replacement = 'p'
operators = '/*' + minus_replacement + plus_replacement
numbers = '1234567890'


def replace_operator(s, operator, replacement):
    """ used to convert -1-2 to -1m2
        and +1+-2 to +1p-2
    """

    if s.find(replacement) != -1:
        # string contains replacement character before we added it
        raise ValueError
    res = s[0]
    to_the_right = numbers + '.-+'
    to_the_left = numbers + '.'
    for i in range(1, len(s) - 1):
        if s[i - 1] in to_the_left and s[i + 1] in to_the_right and s[i] == operator:
            res += replacement
        else:
            res += s[i]
    res += s[-1]
    return res


def bin_calc(s):
    s = replace_operator(s, '-', minus_replacement)
    s = replace_operator(s, '+', plus_replacement)

    operator_pos = [i for i in range(1, len(s)) if s[i] in operators]
    if len(operator_pos) != 1:
        raise ValueError()

    operator = s[operator_pos[0]]
    left = float(s[:operator_pos[0]])
    right = float(s[operator_pos[0] + 1:])

    if operator == plus_replacement:
        return left + right
    elif operator == minus_replacement:
        return left - right
    elif operator == '*':
        return left * right
    else:
        return left / right


def contains_numbers_separated_by_spaces(s):
    while s.find('  ') != -1:
        s = s.replace('  ', ' ')
    for i in range(1, len(s) - 1):
        if s[i] == ' ' and s[i - 1] in numbers and s[i + 1] in numbers:
            return True
    return False


def remove_spaces(s):
    if contains_numbers_separated_by_spaces(s):
        raise ValueError
    return s.replace(' ', '')


def calc(s):
    if not isinstance(s, basestring):
        raise TypeError
    if s == '':
        raise ValueError
    s = remove_spaces(s)
    if s[0] == '|' and s[-1] == '|':
        return abs(float(s[1:-1]))
    else:
        return bin_calc(s)


