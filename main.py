import math
import random
import os, sys


try:
    # if the filename is passed, use that
    library_file = sys.argv[1:][0]
except:
    # otherwise use the default
    PATH = os.path.dirname(os.path.abspath(__file__))
    library_file = PATH + "/prompt_library.txt"

prompts = []

try:
    f = open(library_file, "r")
except:
    print ("error: filename in argument not found- use full path to file")
    exit()

for l in f:
    if l.startswith("-"):
        prompts.append(l[2:])

f.close()

i = math.floor(random.random()*len(prompts))

prompt = prompts[i]

print ("## _Journal Prompt_: " + prompt.strip() + " #journal")
