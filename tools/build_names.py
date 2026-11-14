import csv, json, sys, os, re
src, out = sys.argv[1], sys.argv[2]
Y0, Y1 = 1880, 2025
data = {"g": {}, "b": {}}
top = {}
ok = re.compile(r"^[A-Za-z][A-Za-z'\- ]{0,20}$")
for y in range(Y0, Y1 + 1):
    p = os.path.join(src, str(y), f"girl_boy_names_{y}.csv")
    rows = list(csv.DictReader(open(p, encoding="utf-8")))
    assert 900 <= len(rows) <= 1000, (y, len(rows))
    top[y] = {"g": [], "b": []}
    for r in rows:
        rank = int(r["Rank"])
        for key, col in (("g", "Girl Name"), ("b", "Boy Name")):
            n = (r[col] or "").strip()
            if not n: continue
            assert ok.match(n), (y, n)
            data[key].setdefault(n, {})[y] = rank
            if rank <= 10: top[y][key].append(n)
# compact: name -> "startYear:r,r,r;startYear:r,..." (runs of consecutive years)
def enc(d):
    ys = sorted(d); runs = []; cur = None
    for y in ys:
        if cur and y == cur[0] + len(cur[1]): cur[1].append(d[y])
        else:
            cur = [y, [d[y]]]; runs.append(cur)
    return ";".join(f"{s}:{','.join(map(str, r))}" for s, r in runs)
res = {"y0": Y0, "y1": Y1, "g": {n: enc(d) for n, d in sorted(data["g"].items())}, "b": {n: enc(d) for n, d in sorted(data["b"].items())},
       "top": {str(y): top[y] for y in top}}
json.dump(res, open(out, "w", encoding="utf-8"), separators=(",", ":"), ensure_ascii=False)
print(len(res["g"]), len(res["b"]), os.path.getsize(out))
for n, k in [("Mary","g"),("Linda","g"),("Jennifer","g"),("Ashley","b"),("Ashley","g"),("Khaleesi","g"),("Arya","g"),("Leslie","b"),("Leslie","g"),("Theodore","b"),("Emma","g"),("Madison","g"),("Elsa","g"),("Hazel","g"),("Jason","b"),("Oliver","b")]:
    d = data[k].get(n, {})
    if d:
        best = min(d.values()); by = [y for y in d if d[y] == best]
        print(n, k, "years", len(d), "first", min(d), "last", max(d), "peak", best, by[0], by[-1])
    else: print(n, k, "absent")
print(top[1880], top[2025])
