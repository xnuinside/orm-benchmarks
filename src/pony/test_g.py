import time

from models import Journal
from pony.orm import db_session, select

LEVEL_CHOICE = [10, 20, 30, 40, 50]
start = time.time()


count = 0

with db_session():
    for _ in range(10):
        for level in LEVEL_CHOICE:
            res = [obj.to_dict() for obj in select(j for j in Journal if j.level == level)]
            count += len(res)

now = time.time()

print(f'Pony ORM, G: Rows/sec: {count / (now - start): 10.2f}')
