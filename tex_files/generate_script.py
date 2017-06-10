# to be run from mac only
import os
filename = "main"

import sys
if len(sys.argv) > 1:
	filename = sys.argv[1]

cmd1 = "pdflatex "
os.system(cmd1+filename)

if (filename =="main") or (filename =="biblo"):
	cmd2 = "bibtex "
	os.system(cmd2+filename)

os.system(cmd1+filename)
os.system(cmd1+filename)

cmd3 = "mv "
destination = "../pdf_files/"
os.system(cmd3+filename+".pdf "+destination)

cmd4 = "rm "
extensions = filename+".aux "+filename+".log "+filename+".out "+filename+".bbl "+filename+".blg "+\
                    filename+".lof "+filename+".lot "+filename+".toc "+"*.gz "+filename+".dvi"
os.system(cmd4+extensions)