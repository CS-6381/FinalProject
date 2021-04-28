# Run this in CMD line terminal to convert .docx files to .md after installing Pandoc (https://pandoc.org/installing.html).

# Imports
import os
from pathlib import Path

# Establish directories.
directory = Path('../Documentation')

# Function to list all files in a directory                                                                                                                      
def listFiles(directory):                                                                                                  
    r = []                                                                                                            
    subdirs = [x[0] for x in os.walk(directory)]                                                                            
    for subdir in subdirs:                                                                                            
        files = os.walk(subdir).__next__()[2]                                                                             
        if (len(files) > 0):                                                                                          
            for file in files:                                                                                        
                r.append(os.path.join(subdir, file))                                                                         
    return r

# Convert all .docx files in directory to .md.
for f in directory.glob('**/*'):
    strFile = str(f)
    if '.docx' in strFile:
        fileName = strFile.split('.doc')[0]
        # os.system('pandoc -o ' + fileName + '.md ' + fileName + '.docx')
        # This command should work with tables.
        os.system('pandoc -f docx -t gfm ' + fileName + '.docx' + ' -o ' + fileName + '.md')