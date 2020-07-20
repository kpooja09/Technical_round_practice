# __author__ : "Pooja Kamble"
# Python3 code for finding nearest cities from co-ordinate city graph


import pprint as pp

def find_nearest(c, x, y, q): 

	x_dict = {}
	y_dict ={}
	adj = {}


	# form the list of cities at x co-ordinates, and y co-ordinates 
	
	for i in range(len(c)):
		if str(c[i]) not in adj.keys():
			adj[str(c[i])] = []
		# Put cities with similar x in x_dict with their y co-ordinat
		if x[i] in x_dict:
			x_dict[x[i]].append((y[i], (c[i])))
		else:
			x_dict[x[i]] = [(y[i], (c[i]))]

		# Put cities with similar y in x_dict with their x co-ordinat
		if y[i] in y_dict:
			y_dict[y[i]].append((x[i], (c[i])))
		else:
			y_dict[y[i]] = [(x[i], (c[i]))]
	
	
	
	for i in range(len(q)):
		try:
			ind = c.index(q[i])

			if x[ind] in x_dict.keys():
				for cities in x_dict[x[ind]]:
					# print(q[i], cities)
					if q[i] != cities[1]:
						adj[str(c[ind])].append((abs(cities[0] - x[ind]), (cities)))
			if y[ind] in y_dict.keys():
				for cities in y_dict[y[ind]]:
					if q[i] != cities[1]:
						adj[str(c[ind])].append((abs(cities[0] - y[ind]), (cities)))
		except:
			print('Not exists')	
	tmp = []

	pp.pprint(adj)
	sorted(adj.items(), key = lambda x: x[0])

	for city in q:
		if city in adj:
			tmp.append(adj[city][0][1][1])
		else:
			tmp.append('NONE')

	print(tmp)

# Driver Program 
c = ['c1', 'c2', 'c3', 'c4', 'c5']
# co-ordinatees
x = [3, 2, 1, 2,3]
y = [3, 2, 3, 0,1]

# Find cities closest to below query cities
q = ['c1','c2','c3','c6']


find_nearest(c, x, y, q) 


