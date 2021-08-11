# Exercise: Convert following string to html

markdown_string = """
# Important packages 

- requests
- numpy
- sqlalchemy
"""

#mySol

#from html import HTML

#h = HTML()

#h.p(markdown_string)

#print(h)

# Doesnt work. doesnt import html. not doable via script like this
#also terminal shows error. now to follow musterlösung


import markdown 

html_string = markdown.markdown(
    markdown_string
)

print(html_string)


