# Replacing in string:

url = input("URL: ").strip();

username = url.replace("https://google.com/", "");

print(f"username: {username}");

# aliter:
username2 = url.removeprefix("https://google.com/");
print(f"username: {username2}");

# above using regex:

# re.sub: Syntax: (pattern, repl,string, count=0, flags=0)

"""
sub means Substitute
"""
print("-----------------------------------");

import re;

username = re.sub(r"^(https?://)?(www\.)?google\.com/", "", url);
print(f"username: {username}");

# aliter: above re.search:

print("-------------------");
username = re.search(r"^(https?://)?(www\.)?google\.com/(\w+)$", url, re.IGNORECASE)

print(f"username: {username.group(0)} - line 1")
print(f"username: {username.group(1)} - line 2")
print(f"username: {username.group(2)} - line 3")
print(f"username: {username.group(3)} - line 4")

if(matches):
    print(f"username: {matches.group(1)}");


# now if we dont want to capture a group enclosed in (). we useL (?:) - 




