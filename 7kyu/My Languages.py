# You are given a dictionary/hash/object containing some languages and your test results in the given languages. Return the list of languages where your test score is at least 60, in descending order of the results.
#
# Note: the scores will always be unique (so no duplicate values)
#
# Examples
# {"Java": 10, "Ruby": 80, "Python": 65}    -->  ["Ruby", "Python"]
# {"Hindi": 60, "Dutch" : 93, "Greek": 71}  -->  ["Dutch", "Greek", "Hindi"]
# {"C++": 50, "ASM": 10, "Haskell": 20}     -->  []


def my_languages(results):
    return [list(results.keys())[list(results.values()).index(v)] for v in sorted(results.values()) if v >= 60][::-1]


# Test cases:
assert my_languages({"Java": 10, "Ruby": 80, "Python": 65}) == ["Ruby", "Python"]
assert my_languages({"Hindi": 60, "Dutch": 93, "Greek": 71}) == ["Dutch", "Greek", "Hindi"]
assert my_languages({"C++": 50, "ASM": 10, "Haskell": 20}) == []