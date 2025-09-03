import sys
import math

def haversine(lon1, lat1, lon2, lat2):
    R = 6371  
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2)
    c = 2 * math.asin(math.sqrt(a))
    return R * c

lon = float(input().replace(',', '.'))
lat = float(input().replace(',', '.'))
n = int(input())

closest_defibrillator = None
min_distance = float('inf')

for i in range(n):
    defib = input().split(';')
    name = defib[1]
    def_lon = float(defib[4].replace(',', '.'))
    def_lat = float(defib[5].replace(',', '.'))
    
    distance = haversine(lon, lat, def_lon, def_lat)
    
    if distance < min_distance:
        min_distance = distance
        closest_defibrillator = name

print(closest_defibrillator)
