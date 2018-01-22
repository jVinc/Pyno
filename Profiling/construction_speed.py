""" The purpose of this file is to generate a performance timing of the
html construction to hedge against new features severely degrading performance unknowingly
"""
import git
import time
import shelve


repo = git.Repo(search_parent_directories=True)
sha = repo.head.object.hexsha


from Examples.bootstrap_example import *

start = time.time()
for _ in range(100000):
    constructed_output = H.BootstrapStarterTemplate(H.h1('Hello world!'))
end = time.time()


with shelve.open('performancelog') as db:
    db[sha] = end-start

with shelve.open('performancelog') as db:
    for key, value in db.items():
        print(key, value)