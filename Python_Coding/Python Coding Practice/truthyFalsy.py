#Truth & Falsy

is_old = bool("Hello")
is_licensed  = bool(5)

print()
print(f"This is and Example of Truthy Using Strings -- is_Old == bool('Hello') == {is_old}")
print(f"This is and Example of Truthy Using Ints -- is_Old == bool(5) == {is_licensed}")

is_old = bool("")
is_licensed  = bool(0)

print()
print(f"This is and Example of Falsy Using Strings -- is_Old == bool('') == {is_old}")
print(f"This is and Example of Falsey Using Ints -- is_Old == bool(0) == {is_licensed}\n")

username = "Sami"
password = "2812"

if username and password:
    print(f'Attempting to log in {username}')
else:
    print("No Username or Password Detected")