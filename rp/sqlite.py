import sqlite3

def sql_dump(filename, entries):
    con = sqlite3.connect(filename)
    cur = con.cursor()

    cols = set()
    for e in entries:
        for k in e:
            cols.add(k)

    cols = list(cols)

    cur.execute("DROP TABLE IF EXISTS ca_roster")

    sql = " CREATE TABLE ca_roster ("
    sql += ",".join([" `{}` string ".format(c) for c in cols])
    sql += ");"

    cur.execute(sql)

    sql = " INSERT INTO ca_roster ("
    sql += ",".join([" \"{}\" ".format(c) for c in cols])
    sql += ")"
    sql += " VALUES ("
    sql += ",".join(["?" for c in cols])
    sql += ")"

    vals = []
    for e in entries:
        ev = ()
        for c in cols:
            ev += (e.get(c),)

        vals.append(ev)

    cur.executemany(sql, vals)

    con.commit()
    con.close()

