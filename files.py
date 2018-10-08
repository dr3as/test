fw = open('sample.txt', 'w')
fw.write('Writing some stuff in to my file \n')
fw.write('Write something new on this line\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()