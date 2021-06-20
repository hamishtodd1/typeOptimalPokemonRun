names = [] #add one to it every time you find a new one
assignments = []

alternative_set_of_assignments = []

num_names = 0

opponent_reading_into = 666

with open("assignments.txt" ) as walkthru:
	for line in walkthru:
		if line[0] == '	':
			if line[1] == '	': #an assignment
				already_got = 0
				for assignment in alternative_set_of_assignments:
					if assignment == line[:19]:
						already_got = 1
				if already_got == 0:
					alternative_set_of_assignments.append(line[:19])
			else: #it's a new opponent name
				if opponent_reading_into != 666:
					#have to deal with the last set of assignments
					if len(assignments[opponent_reading_into]) == 0: #check if it's new, i.e. empty
						assignments[opponent_reading_into] = alternative_set_of_assignments #hopefully this is assigned by parameter rather than reference
					else: #want to get the intersection - unless it turns out that this leaves us with nothing in some cases
						new_set_of_assignments = []
						for other_assignment in alternative_set_of_assignments:
							for assignment in assignments[opponent_reading_into]:
								if assignment == other_assignment:
									new_set_of_assignments.append(assignment)
						assignments[opponent_reading_into] = new_set_of_assignments
					alternative_set_of_assignments = []
			
				#ok moving onto this new opponent
				opponent_name = line.strip('	')
				opponent_name = opponent_name.strip(' ')
				already_got = 0
				for existing_opponent in names:
					if existing_opponent == opponent_name:
						already_got = 1
				if already_got == 0:
					names.append(opponent_name)
					assignments.append([])
				opponent_reading_into = names.index(opponent_name)

for name in names:
	print(name[:(len(name)-1)])
	for assignment in assignments[names.index(name)]:
		print(assignment)
	print("\n")