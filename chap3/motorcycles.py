motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)


motorcycles.insert(0, 'ducati')
print(motorcycles)


popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)


last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned + ".")


first_owned = motorcycles.pop(0)
print("The first motorcycle I got was a " + first_owned + ".")

print(motorcycles[-1])