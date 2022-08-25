import os

src_file = 'tmp_01.py'
dest_file = 'dest_01.py'

# Method one
with open(src_file,'r') as infile:
    text = infile.read()
    with open(dest_file,'w') as outfile:
       outfile.write(text)
 
os.remove(dest_file)        
                      
# Method two
open(dest_file,'w').write(open(src_file,'r').read())        
