# Replacing in string:

url = input("URL: ").strip();

username = url.replace("https://google.com/", "");

print(f"username: {username}");

# aliter:
username2 = url.removeprefix("https://google.com/");
print(f"username: {username2}");

# above using regex:

# re.sub

# Syntax: (pattern, repl,string, count=0, flags=0)