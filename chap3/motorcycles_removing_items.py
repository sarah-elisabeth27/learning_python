motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1, 'ducati')

print(motorcycles)


too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive + " is too expensive for me.")