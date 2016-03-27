#convert game record in text format (just moves) to .sgf
#usage:  python filename.py < blah.txt > blah.sgf

import sys
color = 'WB'
movenumber = 0

outstring = '(;AP[HexGui:0.9.GIT]FF[4]GM[11]SZ[13]\n'

for L in sys.stdin:
  for move in L.split():
    movenumber += 1
    outstring +=  ';' + color[movenumber%2] + '[' + move + ']'
    if movenumber%10 == 0: outstring += '\n'
print outstring + ')'
