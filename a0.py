def blockdiag(n):
    # n is a positive integer
    output = ""
    top = "+-+"
    middle = "| |"
    bottom = "+-+-+"
    drop = "\n"
    tab = " "
    output += top + drop
    output += middle + drop
    for i in range(1,n):
        output += bottom + drop + (2*i) * tab
        output += middle + drop
        if i != n-1:
            output += (2*i) * tab
        else:
            output += (2*i) * tab + top
    return output

print(blockdiag(4))
    

# 0, 2, 4, 6
