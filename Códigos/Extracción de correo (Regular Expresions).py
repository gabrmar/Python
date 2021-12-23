import re

"""
To demonstrate a sample usage of regular expressions, lets create a program to extract email addresses from a string.
Suppose we have a text that contains an email address:
"""


str = "Please contact info@sololearn.com for assistance"

"""
Our goal is to extract the substring "info@sololearn.com".
A basic email address consists of a word and may include dots or dashes. This is followed by the @ sign and the domain name (the name, a dot, and the domain name suffix).
This is the basis for building our regular expression.
"""
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

"""
[\w\.-]+ matches one or more word character, dot or dash.
The regex above says that the string should contain a word (with dots and dashes allowed),
followed by the @ sign, then another similar word, then a dot and another word.
"""

"""
Our regex contains three groups:
1 - first part of the email address.
2 - domain name without the suffix.
3 - the domain suffix.
"""


match = re.search(pattern, str)
if match:
   print(match.group())

"""
n case the string contains multiple email addresses,
we could use the re.findall method instead of re.search, to extract all email addresses
"""
