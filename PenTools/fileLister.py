import pathlib

p = pathlib.Path("")

txt_files = p.glob("*.*")

print("*.*", list(txt_files))





