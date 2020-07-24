'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # TBC
    count = 0
    if len(word) > 1:
        if word[:2] == "th":
            count += 1
            return count + count_th(word[2:])
        else:
            return count + count_th(word[1:])
    return count


print(count_th('that this then there'))
