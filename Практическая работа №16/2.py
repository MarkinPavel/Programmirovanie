allowed_ids = set(map(int, input().split()))

incoming_ids = list(map(int, input().split()))

for id in incoming_ids:
   if id in allowed_ids:
       print("OK")
   else:
       print("ADDED")
       allowed_ids.add(id)
