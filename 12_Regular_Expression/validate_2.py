# regex contd.

import re;

email = input("Enter your email: ").strip();

if re.search("@",email):
    print("valid email");
else:
    print("invalid");


# printing patterns in reg ex:


if re.search(".*@.*", email):
    print("valid");
else:
    print("invalid")



# in above we have .*@.* therefore even if we write ayush@, email valid.



if re.search(".+@.+", email):
    print("valid");
else:
    print("invalid")

# how to create above notion using *:

if re.search("..*@..*", email):
    print("valid");
else:
    print("invalid");

# creating more conditions pattern:

# in below if i write that, regex thinks that edu is the separator on whose lhs and rhs pattern is there
"""
if re.search(".+@.+.edu", email):
    print("valid");
else:
    print("invalid");
"""

if re.search(r".+@.+\.edu", email):
    print("valid");
else:
    print("invalid");

# in normal python, \ is escape character.so we use r"pattern" before pattern which means raw string. --> r"\n" means 2 characters bcz in regex we will use a lot of \.

if re.search(r"^.+@.+\.edu$", email):
    print("valid");
else:
    print("invalid");

