from HTMLParser import HTMLParser
import os
from bs4 import BeautifulSoup
import pysentiment as ps

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
				
				
if __name__ == '__main__':
    print 'Starting...'
    cleaned = ""
    input_file = open("sect7_wtags.txt","r")
    output_file = open("sect7_wtags_CLEAN.txt","w")
    for line in input_file:
       # print strip_tags(line)
								
        soup = BeautifulSoup(line)
        cleaned = cleaned + " " + soup.get_text().rstrip('\r\n')
    
    output_file.write(cleaned.encode('utf8'))
				
    hiv4 = ps.HIV4()
    tokens = hiv4.tokenize(cleaned)
    score = hiv4.get_score(tokens)
    print score