import argparse
import sys

parser = argparse.ArgumentParser(description='Cut big *.vcf file to mani small vcfs')
parser.add_argument('--file','-f',dest='fi',help='name of cutted file')
args = parser.parse_args()

if not args.fi:
  print(u'you are not enter filename (option -f)')
  sys.exit(0)
print (u'args.fi:',args.fi)
f=open(args.fi,'r',encoding='utf8')

fn = 0
stop = 0
while stop != 1:
  line=f.readline()
  if not line: break

  #find begin of card
  if 'BEGIN:VCARD' in line:
    fn = fn + 1
    filename=str(fn)+'.vcf'
    print (u'create file: ',filename)
    ff=open(filename,"w")
    ff.write(line)
    ENDFLAG=0
    while ENDFLAG != 1:
      line=f.readline()
      if not line: 
        stop = 1
        break
      ff.write(line)
      # find end of card
      if 'END:VCARD' in line:ENDFLAG=1

