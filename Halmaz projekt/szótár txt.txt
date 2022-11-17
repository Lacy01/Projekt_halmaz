
wr=open('H:\Halmaz projekt')
# üres szótár létrehozása
raktar = {}
print(raktar)
wr.write=("# üres szótár létrehozása")
wr.write=("raktar = {}")
wr.write=("print(raktar)")
# szótár létrehozása adatokkal 
diak = {'vezeteknev': 'Kiss', 'keresztnev': 'Péter', 'eletkor': 17, 'menza': True}
wr.write("# szótár létrehozása adatokkal ")
wr.write("diak = {'vezeteknev': 'Kiss', 'keresztnev': 'Péter', 'eletkor': 17, 'menza': True}" )
# szótár elemeinek elérése kulcs alapján
wr.write("# szótár elemeinek elérése kulcs alapján")
print(diak['eletkor'])
wr.write("print(diak['eletkor'])")
print(diak.get('eletkor'))
wr.write("print(diak.get('eletkor'))")

# nem létező kulcsra való hivatkozás -> KeyError
wr.write("# nem létező kulcsra való hivatkozás -> KeyError")
# print(diak['osztaly'])
wr.write("# print(diak['osztaly'])")
# nem létező kulcsra hivatkozunk a .get metódussal, 
wr.write("# nem létező kulcsra hivatkozunk a .get metódussal,")
# ilyenkor a megadott alapértékkel tér vissza
wr.write("# ilyenkor a megadott alapértékkel tér vissza")
print(diak.get('kollegista', 'nem'))
wr.write("print(diak.get('kollegista', 'nem'))")

# ellenőrzés, hogy létezik-e a kulcs
wr.write("# ellenőrzés, hogy létezik-e a kulcs")
print('keresztnev' in diak)
wr.write("print('keresztnev' in diak)")