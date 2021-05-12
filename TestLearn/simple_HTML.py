'''
WEB SCRAPPING EXAMPLES
'''

from bs4 import BeautifulSoup

sample_html = ('\n'
               '<HTML>\n'
               '<HEAD>\n'
               '<TITLE>Your Title Here</TITLE>\n'
               '</HEAD>\n'
               '\n'
               '<BODY BGCOLOR="FFFFFF">\n'
               '<CENTER><IMG SRC="clouds.jpg" ALIGN="BOTTOM"> </CENTER>\n'
               '<HR>\n'
               '<a href="http://somegreatsite.com">Link Name</a>\n'
               'is a link to another nifty site\n'
               '<H1>This is a Header</H1>\n'
               '<H2>This is a Medium Header</H2>\n'
               'Send me mail at <a href="mailto:support@yourcompany.com">\n'
               'support@yourcompany.com</a>.\n'
               '<P> This is a new paragraph!\n'
               '<P> <B>This is a new paragraph!</B>\n'
               '<BR> <B><I>This is a new sentence without a paragraph break, in bold italics.</I></B>\n'
               '<HR>\n'
               '</BODY>\n'
               '\n'
               '</HTML>\n')

soup = BeautifulSoup(sample_html, 'html.parser')
print(soup.find('h1').string)
print(soup.find_all('p'))
