# - Widths: 5 values taken from a uniform repartition over [15, 250]
# - Amplitudes: 5 values taken from a uniform repartition over [128, 1024]
# - Trials fixed to 6
# - Number of repetitions of the experiment: 2 per person
# - Input device : Graphic tablet (for Dorian only) and Track pad

import random
from math import floor
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
dt_string = now.isoformat()

s = "Experimenter; Input device; Widths; Amplitudes; Trials\n"

l = []

for p in ("Dorian", "Clement"):
    for d in ("Graphic tablet", "Track Pad"):
        for _ in range(2):     
            widths = [floor(15+i*(250 - 15)/5) for i in range(4)] + [250]
            heights = [floor(128+i*(1024-128)/5) for i in range(4)] + [1024]
            l.append((p, d, widths, heights))

# draw a random permutation of l  
random.shuffle(l)
for (p, d, w, h) in l:
    s += (f"{p}; {d}; {w}; {h}; 6\n")
  
with open(f"{dt_string}_experiences.csv", "w") as out:
    out.write(s)    
