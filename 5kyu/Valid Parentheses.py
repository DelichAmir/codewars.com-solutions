# Write a function called that takes a string of parentheses, and determines
# if the order of the parentheses is valid. The function should return true
# if the string is valid, and false if it's invalid.
#
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true

# Constraints
# 0 <= input.length <= 100
#
# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters.
# Furthermore, the input string may be empty and/or not contain any parentheses at all.
# Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).


def valid_parentheses(string: str) -> bool:
    # First solution
    # check, s = 0, [i for i in string if i in '()']
    #
    # for i in s:
    #     if i == '(':
    #         check += 1
    #     if i == ')':
    #         if check > 0:
    #             check = check - 1
    #         else:
    #             return False
    # if check == 0:
    #     return True
    # else:
    #     return False

    # Second solution
    s = ''.join(i for i in string if i in '()')
    while '()' in s:
        s = s.replace('()', '')
    return not s


# Test cases:
assert valid_parentheses("())vrle((kty()s)l(y)") == False
assert valid_parentheses("ww(dy)zwxjrk(dw)q)e(") == False
assert valid_parentheses("  (") == False
assert valid_parentheses(")test") == False
assert valid_parentheses("") == True
assert valid_parentheses("hi())(") == False
assert valid_parentheses("hi(hi)()") == True
assert valid_parentheses("zoj()u(oexpkoxwo)uq") == True
assert valid_parentheses("(naybuot)ly((d)(smd)myqzqk(msisdt()k") == False
assert valid_parentheses("oia(aw()sa)") == True
assert valid_parentheses("(()n)rugt") == True
assert valid_parentheses("j(kvhxflauwjlze)hnu(zekegjwvuu(dolc))s(nbm)rxi") == True
