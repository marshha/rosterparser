import sys
import json
import rp

with open(sys.argv[1], 'r') as fp:
    entries = rp.parse(fp)

rp.sql_dump("test.db", entries)
