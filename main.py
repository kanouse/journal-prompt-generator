import random

prompts = []

f = open("prompt_library.txt", "r")
for l in f:
    if l.startswith("#") or len(l.strip()) == 0:
        continue
    prompts.append(l)
f.close()

i = int(random.random()*len(prompts))

prompt = prompts[i]

f = open("prompt.txt", "w")
f.write(prompt)
f.close()