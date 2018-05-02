✖ ︎For
vigenere.encrypt('BaRFoo', 'BaZ')

'CaQGon'
'BaZBoZ'

✖ ︎For
vigenere.encrypt('Sailing <3 ships thru br0ken harbors', 'NeilYoung')

You
should
have
returned
this:
'Feqwgba <3 fnvta effo ox0xiv syfvbxf'

But
you
actually
returned
this:
'NeqwYba <3 fnNta eYfo ox0Niv sYfvbxN'


('BaRFoo', 'BaZ')

text = "Sailing <3 ships thru br0ken harbors"
encryption_keyword = "NeilYoung"
print("Sailing <3 ships thru br0ken harbors")
print("Feqwgba <3 fnvta effo ox0xiv syfvbxf")

text = "BaRFoo"
encryption_keyword = "BaZ"
print("BaRFoo")
print("CaQGon")