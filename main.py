"""Copy entry.txt to the output directory for the make.fun entry.

The entry is a single word describing the human we work for,
at most 30 characters.
Relentless: the human never stops, never sleeps on a task, and
never accepts the first version. One word, and it says everything
about who signs off on the work.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
