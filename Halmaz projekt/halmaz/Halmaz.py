'''
    Halmaz (set):
    - rendezetlen (elemeknek nincs indexe)
    - egy elem csak egyszer szerepelhet
    - többféle típust tárolhat egyszerre is
    - a halmaz eleme maga nem változtatható meg
    '''
    
wr=open('H:\Halmaz projekt')

# halmaz létrehozása
wr.write("# halmaz létrehozása")
reggeli={'tea','vaj','pirítós'}
wr.write('reggeli={tea,vaj,pirítós}')
# üres halmaz létrehozása
# ebed = {}  <- SZÓTÁRT hoz létre!!!
wr.write("# üres halmaz létrehozása # ebed = {}  <- SZÓTÁRT hoz létre!!!")
ebed={}
wr.write('ebed={}')
# bejárható gyűjteményből, pl. listából
wr.write("# bejárható gyűjteményből, pl. listából")
ebed=set(['halászlé', 'kenyér', True])
wr.write("ebed=set(['halászlé', 'kenyér', True])")
reggeli.add('lekvár')
wr.write("reggeli.add('lekvár')")
reggeli.pop()
wr.write("reggeli.pop()")
reggeli.remove('sajt')
wr.write("reggeli.remove('sajt')")
reggeli.discard('sajt')
wr.write("reggeli.discard('sajt')")