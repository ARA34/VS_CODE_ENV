from pathlib import Path
# D - directory followed by directory --> only files under specific directory
# R - recursive followed by directoru --> files under the specific directory and more

# input: directory ->

user_in = input().lower()

while user_in != "d" or "r":
    print("ERROR")
    user_in = input().lower()

if user_in == "d":
    #directory
    pass

elif user_in == "r":
    # recursive
    pass
