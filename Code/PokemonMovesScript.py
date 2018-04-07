#todo: pokemon test script, which you can run things through

import sys

ptypelist = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon"]

#a for attacker, d for defender. 1, 2, 0.5, or 0
def effective( a, d ):
	h = 0.5
	
	t = 10
	e = 11
	w = 12
	i = 13
	if a == ptypelist[0]: #normal
		if d == ptypelist[0]: return 1
		if d == ptypelist[1]: return 1
		if d == ptypelist[2]: return 1 
		if d == ptypelist[3]: return 1 
		if d == ptypelist[4]: return 1 
		if d == ptypelist[5]: return 1 
		if d == ptypelist[6]: return 1
		if d == ptypelist[7]: return 1 
		if d == ptypelist[8]: return 1 
		if d == ptypelist[9]: return 1 
		if d == ptypelist[t]: return 1 
		if d == ptypelist[e]: return 1 
		if d == ptypelist[w]: return h 
		if d == ptypelist[i]: return 0
		if d == ptypelist[14]: return 1
	if a == ptypelist[1]: #fire
		if d == ptypelist[0]: return 1 
		if d == ptypelist[1]: return h 
		if d == ptypelist[2]: return h 
		if d == ptypelist[3]: return 1 
		if d == ptypelist[4]: return 2 
		if d == ptypelist[5]: return 2 
		if d == ptypelist[6]: return 1
		if d == ptypelist[7]: return 1 
		if d == ptypelist[8]: return 1 
		if d == ptypelist[9]: return 1 
		if d == ptypelist[t]: return 1 
		if d == ptypelist[e]: return 2 
		if d == ptypelist[w]: return h 
		if d == ptypelist[i]: return 1
		if d == ptypelist[14]: return h
	if a == ptypelist[2]: #water
		if d == ptypelist[0]: return 1 
		if d == ptypelist[1]: return 2 
		if d == ptypelist[2]: return h 
		if d == ptypelist[3]: return 1 
		if d == ptypelist[4]: return h 
		if d == ptypelist[5]: return 1 
		if d == ptypelist[6]: return 1
		if d == ptypelist[7]: return 1 
		if d == ptypelist[8]: return 2 
		if d == ptypelist[9]: return 1 
		if d == ptypelist[t]: return 1 
		if d == ptypelist[e]: return 1 
		if d == ptypelist[w]: return 2 
		if d == ptypelist[i]: return 1
		if d == ptypelist[14]: return h
	if a == ptypelist[3]: #electric
		if d == ptypelist[0]: return 1 
		if d == ptypelist[1]: return 1 
		if d == ptypelist[2]: return 2 
		if d == ptypelist[3]: return h 
		if d == ptypelist[4]: return h 
		if d == ptypelist[5]: return 1 
		if d == ptypelist[6]: return 1
		if d == ptypelist[7]: return 1 
		if d == ptypelist[8]: return 0 
		if d == ptypelist[9]: return 2 
		if d == ptypelist[t]: return 1 
		if d == ptypelist[e]: return 1 
		if d == ptypelist[w]: return 1 
		if d == ptypelist[i]: return 1
		if d == ptypelist[14]: return h
	if a == ptypelist[4]: #grass
		if d == ptypelist[0]: return 1 
		if d == ptypelist[1]: return h 
		if d == ptypelist[2]: return 2 
		if d == ptypelist[3]: return 1 
		if d == ptypelist[4]: return h 
		if d == ptypelist[5]: return 1 
		if d == ptypelist[6]: return 1
		if d == ptypelist[7]: return h 
		if d == ptypelist[8]: return 2 
		if d == ptypelist[9]: return h 
		if d == ptypelist[t]: return 1 
		if d == ptypelist[e]: return h 
		if d == ptypelist[w]: return 2 
		if d == ptypelist[i]: return 1
		if d == ptypelist[14]: return h
	if a == ptypelist[5]: #ice
		if d == ptypelist[0]: return 1 
		if d == ptypelist[1]: return 1 
		if d == ptypelist[2]: return h 
		if d == ptypelist[3]: return 1 
		if d == ptypelist[4]: return 2 
		if d == ptypelist[5]: return h 
		if d == ptypelist[6]: return 1
		if d == ptypelist[7]: return 1 
		if d == ptypelist[8]: return 2 
		if d == ptypelist[9]: return 2 
		if d == ptypelist[t]: return 1 
		if d == ptypelist[e]: return 1 
		if d == ptypelist[w]: return 1 
		if d == ptypelist[i]: return 1
		if d == ptypelist[14]: return 2
	if a == ptypelist[6]: #fighting
		if d == ptypelist[0]: return 2 
		if d == ptypelist[1]: return 1 
		if d == ptypelist[2]: return 1 
		if d == ptypelist[3]: return 1 
		if d == ptypelist[4]: return 1 
		if d == ptypelist[5]: return 2 
		if d == ptypelist[6]: return 1
		if d == ptypelist[7]: return h 
		if d == ptypelist[8]: return 1 
		if d == ptypelist[9]: return h 
		if d == ptypelist[t]: return h 
		if d == ptypelist[e]: return h 
		if d == ptypelist[w]: return 2 
		if d == ptypelist[i]: return 0
		if d == ptypelist[14]: return 1
	if a == ptypelist[7]: #poison
		if d == ptypelist[0]: return 1 
		if d == ptypelist[1]: return 1 
		if d == ptypelist[2]: return 1 
		if d == ptypelist[3]: return 1 
		if d == ptypelist[4]: return 2 
		if d == ptypelist[5]: return 1 
		if d == ptypelist[6]: return 1
		if d == ptypelist[7]: return h 
		if d == ptypelist[8]: return h 
		if d == ptypelist[9]: return 1 
		if d == ptypelist[t]: return 1 
		if d == ptypelist[e]: return 2 
		if d == ptypelist[w]: return h 
		if d == ptypelist[i]: return h
		if d == ptypelist[14]: return 1
	if a == ptypelist[8]: #ground
		if d == ptypelist[0]: return 1 
		if d == ptypelist[1]: return 2 
		if d == ptypelist[2]: return 1 
		if d == ptypelist[3]: return 2 
		if d == ptypelist[4]: return h 
		if d == ptypelist[5]: return 1 
		if d == ptypelist[6]: return 1
		if d == ptypelist[7]: return 2 
		if d == ptypelist[8]: return 1 
		if d == ptypelist[9]: return 0 
		if d == ptypelist[t]: return 1 
		if d == ptypelist[e]: return h 
		if d == ptypelist[w]: return 2 
		if d == ptypelist[i]: return 1
		if d == ptypelist[14]: return 1
	if a == ptypelist[9]: #flying
		if d == ptypelist[0]: return 1 
		if d == ptypelist[1]: return 1 
		if d == ptypelist[2]: return 1 
		if d == ptypelist[3]: return h 
		if d == ptypelist[4]: return 2 
		if d == ptypelist[5]: return 1 
		if d == ptypelist[6]: return 2
		if d == ptypelist[7]: return 1 
		if d == ptypelist[8]: return 1 
		if d == ptypelist[9]: return 1 
		if d == ptypelist[t]: return 1 
		if d == ptypelist[e]: return 2 
		if d == ptypelist[w]: return h 
		if d == ptypelist[i]: return 1
		if d == ptypelist[14]: return 1
	if a == ptypelist[10]: #psychic
		if d == ptypelist[0]: return 1 
		if d == ptypelist[1]: return 1 
		if d == ptypelist[2]: return 1 
		if d == ptypelist[3]: return 1 
		if d == ptypelist[4]: return 1 
		if d == ptypelist[5]: return 1 
		if d == ptypelist[6]: return 2
		if d == ptypelist[7]: return 2 
		if d == ptypelist[8]: return 1 
		if d == ptypelist[9]: return 1 
		if d == ptypelist[t]: return h 
		if d == ptypelist[e]: return 1 
		if d == ptypelist[w]: return 1 
		if d == ptypelist[i]: return 1
		if d == ptypelist[14]: return 1
	if a == ptypelist[11]: #bug
		if d == ptypelist[0]: return 1 
		if d == ptypelist[1]: return h 
		if d == ptypelist[2]: return 1 
		if d == ptypelist[3]: return 1 
		if d == ptypelist[4]: return 2 
		if d == ptypelist[5]: return 1 
		if d == ptypelist[6]: return h
		if d == ptypelist[7]: return 2 
		if d == ptypelist[8]: return 1 
		if d == ptypelist[9]: return h 
		if d == ptypelist[t]: return 2 
		if d == ptypelist[e]: return 1 
		if d == ptypelist[w]: return 1 
		if d == ptypelist[i]: return 1
		if d == ptypelist[14]: return 1
	if a == ptypelist[12]: #rock
		if d == ptypelist[0]: return 1 
		if d == ptypelist[1]: return 2 
		if d == ptypelist[2]: return 1 
		if d == ptypelist[3]: return 1 
		if d == ptypelist[4]: return 1 
		if d == ptypelist[5]: return 2 
		if d == ptypelist[6]: return h
		if d == ptypelist[7]: return 1 
		if d == ptypelist[8]: return h 
		if d == ptypelist[9]: return 2 
		if d == ptypelist[t]: return 1 
		if d == ptypelist[e]: return 2 
		if d == ptypelist[w]: return 1 
		if d == ptypelist[i]: return 1
		if d == ptypelist[14]: return 1
	if a == ptypelist[13]: #ghost
		if d == ptypelist[0]: return 0 
		if d == ptypelist[1]: return 1 
		if d == ptypelist[2]: return 1 
		if d == ptypelist[3]: return 1 
		if d == ptypelist[4]: return 1 
		if d == ptypelist[5]: return 1 
		if d == ptypelist[6]: return 1
		if d == ptypelist[7]: return 1 
		if d == ptypelist[8]: return 1 
		if d == ptypelist[9]: return 1 
		if d == ptypelist[t]: return 0 
		if d == ptypelist[e]: return 1 
		if d == ptypelist[w]: return 1 
		if d == ptypelist[i]: return 2
		if d == ptypelist[14]: return 1
	if a == ptypelist[14]: #dragon
		if d == ptypelist[0]: return 1 
		if d == ptypelist[1]: return 1 
		if d == ptypelist[2]: return 1 
		if d == ptypelist[3]: return 1 
		if d == ptypelist[4]: return 1 
		if d == ptypelist[5]: return 1 
		if d == ptypelist[6]: return 1
		if d == ptypelist[7]: return 1 
		if d == ptypelist[8]: return 1 
		if d == ptypelist[9]: return 1 
		if d == ptypelist[t]: return 1 
		if d == ptypelist[e]: return 1 
		if d == ptypelist[w]: return 1 
		if d == ptypelist[i]: return 1
		if d == ptypelist[14]: return 2
	print("got baaaaad inputs for effective: %s was attack, %s was defence" % (a, d))
	return 1

def twoeffective(a, d1, d2 ):
	component1 = effective( a, d1 )

	component2 = 1
	if d2 != d1:
		component2 = effective( a, d2 )

	return float(component1) * float(component2)

def read_opponent_type( line ):
	type1 = ""
	type2 = ""
	if "FIR" in line:
		assignment = "Fire"
		if type1 == "":
			type1 = assignment
		else:
			type2 = assignment
	if "NRM" in line:
		assignment = "Normal"
		if type1 == "":
			type1 = assignment
		else:
			type2 = assignment
	if "ELE" in line:
		assignment = "Electric"
		if type1 == "":
			type1 = assignment
		else:
			type2 = assignment
	if "PSN" in line:
		assignment = "Poison"
		if type1 == "":
			type1 = assignment
		else:
			type2 = assignment
	if "FGT" in line or "FTG" in line:
		assignment = "Fighting"
		if type1 == "":
			type1 = assignment
		else:
			type2 = assignment
	if "GRN" in line:
		assignment = "Ground"
		if type1 == "":
			type1 = assignment
		else:
			type2 = assignment
	if "GRS" in line:
		assignment = "Grass"
		if type1 == "":
			type1 = assignment
		else:
			type2 = assignment
	if "FLY" in line:
		assignment = "Flying"
		if type1 == "":
			type1 = assignment
		else:
			type2 = assignment
	if "GST" in line:
		assignment = "Ghost"
		if type1 == "":
			type1 = assignment
		else:
			type2 = assignment
	if "DRG" in line:
		assignment = "Dragon"
		if type1 == "":
			type1 = assignment
		else:
			type2 = assignment
	if "PSY" in line:
		assignment = "Psychic"
		if type1 == "":
			type1 = assignment
		else:
			type2 = assignment
	if "WTR" in line:
		assignment = "Water"
		if type1 == "":
			type1 = assignment
		else:
			type2 = assignment
	if "ICE" in line:
		assignment = "Ice"
		if type1 == "":
			type1 = assignment
		else:
			type2 = assignment
	if "BUG" in line:
		assignment = "Bug"
		if type1 == "":
			type1 = assignment
		else:
			type2 = assignment
	if "RCK" in line:
		assignment = "Rock"
		if type1 == "":
			type1 = assignment
		else:
			type2 = assignment

	if type2 == "":
		type2 = type1
	return type1, type2

O = [] #for opponents
with open("PokemonTrainers.txt" ) as walkthru:
	for line in walkthru:
		last_four_chars = line[len(line) - 5 : len(line) - 1]
		if line[0] == "#" and last_four_chars != "Exp.":
			#if last_four_chars != "Exp.":
				#if line[len(line) - 9]!= "%":
					#print("funny line: %s 		our last four: %s" % (line[: len(line) - 1],last_four_chars))
					
			type1, type2 = read_opponent_type( line )
			
			if type1 == "" or type2 == "":
				print("bad input:", line)
			ptypes = set([])
			ptypes.add(type1)
			ptypes.add(type2)

			alreadygotit = 0
			for typeset in O:
				if ptypes == typeset:
					alreadygotit = 1
					#and have something to say how many there are of each type!
			if alreadygotit == 1:
				continue
			#print(line[6:17], ptypes)
			O.append(ptypes)

#check for "if a move can take out this kind, it can take out THIS kind"
#but HMMM we may well be interested in moves that can only take out a subset? It might be the only subset we need
'''i1 = 0
while i1 < len(O):
	strong_against_i1 = set([])
	for attacktype in ptypelist:
		if len( O[i1] ) == 2:
			if twoeffective( attacktype, list(O[i1])[0], list(O[i1])[1] ) >= 2:
				strong_against_i1.add(attacktype)
		elif twoeffective( attacktype, list(O[i1])[0], list(O[i1])[0] ) >= 2:
			strong_against_i1.add(attacktype)
	i2 = i1+1
	while i2 < len(O):
		strong_against_i2 = set([])
		for attacktype in ptypelist:
			if len( O[i2] ) == 2:
				if twoeffective( attacktype, list(O[i2])[0], list(O[i2])[1] ) >= 2:
					strong_against_i2.add(attacktype)
			elif twoeffective( attacktype, list(O[i2])[0], list(O[i2])[0] ) >= 2:
				strong_against_i2.add(attacktype)
		if strong_against_i2 <= strong_against_i1:
			print("if you've got one of these moves %s that can take care of %s, then you can also take care of %s, which requires these moves %s" % (strong_against_i1,O[i1],O[i2],strong_against_i2) )
			O.pop(i2)
		else:
			i2 = i2 + 1
	i1 = i1 + 1'''
	
#also, moves that are objectively inferior to other moves? eg normal and everything else?
#That may not exist though. A may be strong against all that B is and more, but B may have more weakenesses
		
print("distinct opponents: %s" % O)

for movetype1 in ptypelist:
	#we need a bug for our psychic, fighting, and ground
	for movetype2 in ptypelist:
		if ptypelist.index( movetype2 ) <= ptypelist.index( movetype1 ): continue
		for movetype3 in ptypelist:
			if ptypelist.index( movetype3 ) <= ptypelist.index( movetype2 ): continue
			for movetype4 in ptypelist:
				if ptypelist.index( movetype4 ) <= ptypelist.index( movetype3 ): continue
				
				knockouts = 0
				
				for o in O:
					something_is_super_effective = 0
					for attacktype in [movetype1, movetype2, movetype3, movetype4 ]:
						if len( o ) == 2:
							if twoeffective( attacktype, list(o)[0], list(o)[1] ) >= 2:
								something_is_super_effective = 1
						elif twoeffective( attacktype, list(o)[0], list(o)[0] ) >= 2:
							something_is_super_effective = 1
					if something_is_super_effective == 1:
						knockouts += 1
						
				if knockouts >= 27: #change this number if you want to be less strict 
					nonknockouts = []
					for o in O:
						something_is_super_effective = 0
						for attacktype in [movetype1, movetype2, movetype3, movetype4 ]:
							if len( o ) == 2:
								if twoeffective( attacktype, list(o)[0], list(o)[1] ) >= 2:
									something_is_super_effective = 1
							elif twoeffective( attacktype, list(o)[0], list(o)[0] ) >= 2:
									something_is_super_effective = 1
						if something_is_super_effective == 0:
							nonknockouts.append(o)
					#if {'Fighting'} not in nonknockouts: #can use this to make sure a few aren't printed
					print("we have a big one: %s, %s, %s, %s although it can't do %s" % (movetype1, movetype2, movetype3, movetype4, nonknockouts))

					
'''
How to interpret these results?
One thing to do would be to look at which ones are unable to do obscure types that you can attach to a specific pokemon. There might be subsets though!

Our anti-normals
Grass, Fighting, Bug, Rock although it can't do [{'Electric'}, {'Fighting'}, {'Dragon'}]
Ice, Fighting, Bug, Rock although it can't do [{'Electric'}, {'Fighting'}, {'Water'}]
- so find one in your team that's NOT STRONG to these types, they are your anti-normals.
Unlikely scenario: there is an electric or fighting type that doesn't HAVE any of those moves, and actually has lots of moves that can only be defended against by this weak-to-fighting type


Double Kick 30
Low Kick 50
Rolling Kick 60
Jump Kick 70
Submission 80
Hi Jump Kick 85

Leech life 20
Pin Missile 14
Twineedle 25

Rock Throw 50
Rock Slide 75

Peck 35
Wing Attack 35
Fly 70
Drill Peck 80
Sky Attack 140

Bone club 65
Dig 100
Earthquake 100

aurora beam 65
ice punch 75
ice beam 95
blizzard 120

absorb 20
vine whip 35
mega drain 40
razor leaf 55
petal dance 70
solar beam 120

confusion 50
psybeam 65
psychic 90




'''