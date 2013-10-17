f=open('In.vcf','r',encoding='utf8')

line1='BEGIN:VCARD\n\r'
fn = 0
i=1
while i<2000:
	i=i+1
	print (u'i')
	print(i)

	line=f.readline()
	if not line: break
	if 'BEGIN:' in line:
		fn = fn + 1
		print (u'fn')
		print (fn)
		filename=str(fn)+'.vcf'
		print (filename)
		ff=open(filename,"w")
		ff.write(line)
		ENDFLAG=0
		while ENDFLAG != 1:
			line=f.readline()
			if not line: break
			ff.write(line)
			if 'END:VCARD' in line:ENDFLAG=1

	





