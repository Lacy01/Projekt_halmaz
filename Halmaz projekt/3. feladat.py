halmaz3=set(['l','k','j'])
halmaz3.clear()
print (halmaz3)
halmaz=set(['egy','kettő','három','a','b','c'])
halmaz2=set(['egy','kettő','három','négy'])
print(halmaz3)
print(halmaz.difference(halmaz2))
halmaz3.difference_update(halmaz,halmaz2)
print(halmaz.intersection(halmaz2))
halmaz.intersection_update
print(halmaz.isdisjoint(halmaz2))#True, ha nincs megegyező elem a két halmaz közt pl: a={'a','b','c'} b={'d','e','f'}
print(halmaz.issubset(halmaz2)) #True, ha a halmaz minden eleme benne van a halmaz 2-ben a={'a','b','c'} b={'d','e','f','a','b','c'}
asd=halmaz.symmetric_difference(halmaz2)# Kiírja azokat az elemeket amelyek csak az eggyik halmazban vannak benne
print(asd)

