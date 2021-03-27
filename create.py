import sys
import rp

with open(sys.argv[1], 'r') as fp:
    entries = rp.parse(fp)

rp.sql_dump(sys.argv[2], entries)
