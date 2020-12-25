guest_list = ['Angie', 'Cynthia', 'Amelie']

guest_list.insert(0, 'Toni')
guest_list.insert(2, 'Sophie')
guest_list.append('Lilli')

print(guest_list)


print("Unfortunately, the venue is over-booked, only three of you can come by.")
not_in_1 = guest_list.pop(1)

print(not_in_1 + ", there's no space for you at the dinner table, sorry.")

not_in_0 = guest_list.pop(0)
print(not_in_0 + ", you can't come either, you eat too much. I can't afford that.")

not_in_2 = guest_list.pop()
print(not_in_2 + ", you were the last one invited, that's what disqualifices you from joining.")

print(guest_list)

guest_list.remove('Sophie')

print(guest_list)

del guest_list[1]

print(guest_list)

del guest_list[0]

print(guest_list)