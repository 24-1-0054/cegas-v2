# For recording purposes only. Do not grade. 
# Do not consider as a part of the CEGAS.

import os
this = os.path.dirname(__file__)
cwd = os.path.abspath(this)
os.chdir(cwd)

with open("../seed.sql") as f:
    writefile = None
    writelines = []

    for file in os.listdir("."):
        if ".csv" in file:
            os.remove(file)
        
    for line in f:
        if "INSERT INTO" in line:
            if writefile != None:
                writefile.close()
            writefilename = line.split("(")[0][11:].strip() + ".csv" # from: INSERT INTO student(student_id, ...) VALUES,
            
            writefile = open(writefilename, "a") 
            continue  
        writefile.write(line[1:-3].replace(', ', ',') + '\n')

    writefile.close()