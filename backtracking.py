def permute(s, l, r):
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r+1):
            s[l], s[i] = s[i], s[l]   # swap
            permute(s, l+1, r)        # recursive call
            s[l], s[i] = s[i], s[l]   # backtrack (undo swap)

string = "ABC"
permute(list(string), 0, len(string)-1)
