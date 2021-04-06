
# Lesson: strings to lists and back (str.split(), str.splitlines(), str.join())
"""
Often lists can be generated from other types of data.  Here we'll look at how
to make lists from strings (and vice-versa) by splitting and joining them on
seperators.

Examples:
>> "Jim, Mary, David".split(", ")  # str.split()
["Jim", "Mary", "David"]

>> "Welcome\nto the jungle".splitlines()  # str.splitlines()
["Welcome", "to the jungle"]

>> "-".join(["AB", "CD", "EF"])  # str.join()
"AB-CD-EF"
"""


# Exercise:  Scraping for Emails
"""
You are sent an email message with a list of email addresses to send out in an group email, 
one on each line, but prepended by extra unneeded information:
  1. Strip out the unneeded info into a list of emails 
  2. Join the emails into a comma-seperated string to be copy-pasted into the "To:" line of your group email.

Example:
orig_message = "This is my email: dg@gg.com. his boyfriend is: gd@dd.com"
new_message = "dg@gg.com, gd@dd.com"
""" 

# Raw Data: 
text = """
Joe's email is here: joe@saturn.de
Frederika can be reached at: freddi@usenet.fr
Monika: info@monika.com
I have two emails, but the one I check most is: superdawg1978@hotmail.com
"""

# Script (fill in here):

    
# Output:
# print(emails)
# print(to_text)


