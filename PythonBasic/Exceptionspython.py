IteamsInCart = 2

if IteamsInCart != 1:
    # raise Exception(" Condition not matching")
    pass
assert (IteamsInCart == 2)

# Try & Catch
try:
    with open('Gitpulltest', 'r') as reader:
        reader.read()
except:
    print("this is failed")

# Try & Catch (python error message)
try:
    with open('Gitpulltest', 'r') as reader:
        reader.read()
except Exception as s:
    print(s)

# Try & Catch (Finally)
try:
    with open('Gitpulltest', 'r') as reader:
        reader.read()
except Exception as s:
    print(s)

finally:
    print("The code execution passed")
