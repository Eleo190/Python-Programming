#PROBLEM 2

#PART A
list_a = [(a,b,c,d) for a in range (1,11) for b in range (1,11) for c in range (1,11) for d in range (1,11) if len({a,b,c,d}) == 4 and a**2 + b**2 == c**2 + d**2]

#PART B
string_list = ['One', 'SEVEN', 'three', 'two', 'Ten']
list_b = [((item).lower(), len(item)) for item in string_list if len(item) < 5]

#PART C
names = ['Christopher Ashton Kutcher', 'Elizabeth Stamatina Fey']
list_c = [f"{item.split()[0]} {item.split()[1][0]}. {item.split()[2]}" for item in names]

#PART D
lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
lst2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]
list_d = [(wrd1, wrd2) for wrd1 in lst1 for wrd2 in lst2 if sorted(wrd1.lower()) == sorted(wrd2.lower())]

#PART E
s = ['one', 'two', 'three']
dict_e = {word : len(word) for word in s}

#PART F
text = "The quick brown fox jumps over the lazy dog"
dict_f = {i:c for i,c in enumerate(text) if c.lower() in "aeiou"}
print(list_a)
print(list_b)
print(list_c)
print(list_d)
print(dict_e)
print(dict_f)
print("ERIC LEOCADIO, Z23712790")