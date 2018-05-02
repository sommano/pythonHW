

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."
#text = "aaa bbbb ccccc"
print(len(text))
counting_dictionary ={}

for i in text:
    if i not in counting_dictionary.keys():
        counting_dictionary.update({i: 0})
#print(counting_dictionary)

for i in text:
    if i in counting_dictionary.keys():
        counting_dictionary.update({i: counting_dictionary[i] + 1})

for k, v in sorted(counting_dictionary.items()):
        print(k, v)

#print(counting_dictionary)


#my_dict = {"cat":12, "dog":6, "elephant":23}
#for i in my_dict:
#    print(i,":",my_dict[i])














