def digit_root(digit):

    str_digit = str(digit)
    result = sum([int(x) for x in str_digit])
    if result > 9:
        return digit_root(result)
    else:
        return result


print(digit_root(19999889987))
