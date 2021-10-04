# set operator
#union
animal={"cat","dog","bear"}
animal2={"bird","monkey","dolphin","cat"}

#animalgroup=animal.union(animal2)
#print(animalgroup)
#animal.update(animal2)
#print(animal)

#intersection เอาที่เหมือนกัน
#intersec=animal.intersection(animal2)
#animal.intersection_update(animal2)
#print(intersec)
#print(animal)

#difference ที่เหมือนกัน ออก
diff=animal.difference(animal2)
print(diff)
animal.difference_update(animal2)
print(animal)