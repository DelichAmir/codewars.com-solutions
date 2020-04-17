# You are given a function that should insert an asterisk (*) between every pair of even digits in the given input, and return it as a string. If the input is a sequence, concat the elements first as a string.
#
# Input
# The input can be an integer, a string of digits or a sequence containing integers only.
#
# Output
# Return a string.
#
# Examples
# 5312708     -->  "531270*8"
# "0000"      -->  "0*0*0*0"
# [1, 4, 64]  -->  "14*6*4"
# Have fun!


def asterisc_it(n):
    # First solution
    if type(n) == list:
        n_str = ''
        out, key = '', []
        for i in [str(i) for i in n]:
            n_str += i
        n = n_str
    else:
        out, key, n = '', [], str(n)

    for i in n:
        if int(i) % 2 == 0 and len(key) == 0:
            key.append(1)
            out += i + '*'

        elif int(i) % 2 == 0 and len(key) > 0:
            key.pop()
            out += i + '*'

        elif len(key) > 0:
            key.pop()
            out = out[0:-1] + i
        else:
            if len(out) > 1:
                if out[-1] == '*':
                    out = out[0:-1] + i
                else:
                    out += i
            else:
                out += i

    if out[-1] == '*':
        return out[0:-1]

    return out


    # # Second solution
    # import re
    #
    # if isinstance(n, int):
    #     n = str(n)
    # elif isinstance(n, list):
    #     n = ''.join(map(str, n))
    # return re.sub(r'(?<=[02468])(?=[02468])', '*', n)
    #
    #
    # # Third solution
    # if type(n) == list: n = "".join(str(i) for i in n)
    # if type(n) == int: n = str(n)
    # return "".join([a+"*" if int(a)%2==0 and int(b)%2 == 0 else a for a,b in zip(n,n[1:])]) + n[-1]


# Test cases:
assert asterisc_it(5312708) == '531270*8'
assert asterisc_it(9682135) == '96*8*2135'
assert asterisc_it(2222) == '2*2*2*2'
assert asterisc_it(1111) == '1111'
assert asterisc_it(9999) == '9999'
assert asterisc_it('0000') == '0*0*0*0'
assert asterisc_it(8) == '8'
assert asterisc_it(2) == '2'
assert asterisc_it(0) == '0'
assert asterisc_it([1, 4, 64, 68, 67, 23, 1]) == '14*6*4*6*8*67231'
