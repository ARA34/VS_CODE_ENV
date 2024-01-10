n = int(input())

output = "+-+\n| |\n+-+"
for i in range(n):
    if i != n-1:
        # inside blocks
        output += "-+\n" + "  "*(i+1) + "| |\n" + "  "*(i+1) + "+-+" 

print(output)