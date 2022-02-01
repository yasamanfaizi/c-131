import csv 
rows = []
with open("main.csv", "r") as f:
    reader = csv.reader(f)
    for i in reader:
        rows.append(i)
header = rows[0]
data = rows[1:]

solar_system_count = {}
for i in data:
    if solar_system_count.get(i[11]):
        solar_system_count[i[11]]+=1
    else:
        solar_system_count[i[11]]=1
maxplanet = max(solar_system_count, key = solar_system_count.get)
print(maxplanet)
print(solar_system_count[maxplanet])
tempdata = list(data)
for a in tempdata:
  mass = a[3]
  if mass.lower() == "unknown":
    data.remove(a)
    continue
  else:
    mass_value = mass.split(" ")[0]
    mass_ref = mass.split(" ")[1]
    if mass_ref == "Jupiters":
      mass_value = float(mass_value) * 317.9
    a[3] = mass_value

  radius = a[7]
  if radius.lower() == "unknown":
    data.remove(a)
    continue
  else:
    radius_value = radius.split(" ")[0]
    radius_ref = radius.split(" ")[2]
    if radius_ref == "Jupiter":
      radius_value = float(radius_value) * 11.2
    a[7] = radius_value

    