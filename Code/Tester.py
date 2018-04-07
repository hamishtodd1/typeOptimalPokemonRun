import sys

sillymoves = [	"Acid Armor", "Agility", "Amnesia", "Barrier", "Defense Curl", "Double Team", "Focus Energy", "Growth", "Harden", "Haze", "Light Screen", "Meditate","Metronome", "Mimic",
					"Minimize", "Mirror Move", "Mist", "Recover", "Rest", "Reflect", "Sharpen", "Softboiled", "Splash", "Substitute","Swords Dance", "Teleport", "Transform", "Withdraw", 
				"Dragon Rage", #It's a weird move, and the only dragon attack
				"Hypnosis", "Confuse Ray",
				
				"Conversion","Disable","Flash","Glare","Growl","Kinesis","Leer","Lovely Kiss","Poison Gas","PoisonPowder","Roar","Sand-Attack","Screech",
					"Sing","Sleep Powder","SmokeScreen","Spore","String Shot","Stun Spore","Supersonic","Tail Whip","Thunder Wave","Toxic","Whirlwind"
					]
#Hypnosis and Confuse Ray feel ok to concede because you don't get an "It's not very effective" message
#Replace confuse ray with leech life: concede to Lorelei's Lapras but use the right thing against zubat and golbat
#Polywag/whirl is the only reason hypnosis is a problem

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

def twoeffective(a, d1, d2 ):
	component1 = effective( a, d1 )

	if d2 == d1:
		component2 = 1
	else:
		component2 = effective( a, d2 )

	return effective( a, d1 ) * effective( a, d2 ) #hope this is true

#returns 0 if it's an inconsequential move
def move_to_type( move ):
	ptype = "nothing"
	movelength = len(move)
	with open("PokemonMoves.txt" ) as movelist:
		for line in movelist:
			if move == line[:movelength]:
				lineDeSpaced = line[movelength+2:].split(" ")
				for potentialtype in ptypelist:
					#have we gotten a recognized type out of the file?
					if lineDeSpaced[0] == potentialtype:
						ptype = potentialtype
				if ptype == "nothing":
					print("ERROR: type '%s' not found" % lineDeSpaced[0])
					#exit()
		if ptype == "nothing":
			print("ERROR: move '%s' not found" % move)
			#exit()
		if move in sillymoves:
			return 0
		else:
			return ptype
			
def print_failures( u ):
	u_failures = []
	for attacktype in ptypelist:
		if twoeffective( attacktype, u[0], u[1] ) > 0.5:
			u_failures.append(attacktype)
	print("	%s can't do	 %s" % (u,u_failures) )
	
		
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
	
def read_opponent_moves(line):
	ptypes = []
	unprocessed_moves = line[3:]
	unprocessed_moves = unprocessed_moves.rstrip()
	unprocessed_moves = unprocessed_moves.rstrip('\n')
	moves = unprocessed_moves.split(", ")

	newmovetype = move_to_type( moves[0])
	if newmovetype != 0:
		ptypes.append( move_to_type( moves[0]) )
	if len( moves ) > 1:
		newmovetype = move_to_type( moves[1])
		if newmovetype not in ptypes and newmovetype != 0:
			ptypes.append( newmovetype )
	if len( moves ) > 2:
		newmovetype = move_to_type( moves[2])
		if newmovetype not in ptypes and newmovetype != 0:
			ptypes.append( newmovetype )
	if len( moves ) > 3:
		newmovetype = move_to_type( moves[3])
		if newmovetype not in ptypes and newmovetype != 0:
			ptypes.append( newmovetype )
			
	#might be nothing but harden or whatever
	if len(ptypes) < 1:
		return 0
		
	#bulk it out
	while len(ptypes) < 4:
		ptypes.append(ptypes[0])
	return ptypes

def A_hypereffectiveagainst_B(
	Atype1, Atype2, Amove1,Amove2,Amove3,
	Btype1, Btype2, Bmove1,Bmove2,Bmove3,Bmove4): #if only one type, pass it twice. If fewer than 4 moves, pass the same move twice
	usable_move_string = ""
	if 	twoeffective(Amove1, Btype1, Btype2 ) > 1:
		usable_move_string = usable_move_string + Amove1 + " "
	if 	twoeffective(Amove2, Btype1, Btype2 ) > 1:
		usable_move_string = usable_move_string + Amove2 + " "
	if 	twoeffective(Amove3, Btype1, Btype2 ) > 1:
		usable_move_string = usable_move_string + Amove3 + " "
		
	
	if 	twoeffective(Bmove1, Atype1, Atype2 ) > 0.5 or twoeffective(Bmove2, Atype1, Atype2 ) > 0.5 or twoeffective(Bmove3, Atype1, Atype2 ) > 0.5 or twoeffective(Bmove4, Atype1, Atype2 ) > 0.5:
		return ""
	else: return usable_move_string
	
		
#------------------------------------------------------------------------------
#main
#One of the rocks, and psychic/ghost, NEEDS to have electric or grass for goldeen and golduck. Onix on a "water pokemon??"
A1 = ["Water","Rock",		"Fighting","Water","Rock"]
A2 = ["Psychic","Ghost",	"Flying","Bug","Electric"]
A3 = ["Ground","Rock",		"Ground", "Ice","Grass"]
A4 = ["Flying","Ghost",		"Psychic","Ice","Rock"]
A5 = ["Water","Ghost",		"Psychic","Grass","Rock"]


#go through every combination of 2 moves, all 225 of them
#go through the game, get the ones that only one member of your team can deal with. Of those 225, rule out the ones not containing a move to deal with their destined foes.
#that might be enough to get you a long way but then you could take every battle for which they are one of two
#  so you'd have "one of these two needs this move". 
#  You could try every combination going through the game but just
#	 if THISMOVE not in THISPOKEMONSMOVESET and THISMOVE not in THATPOKEMONSMOVESET:
#		continue
#could remove venonat and hitmonchan and stop as soon as you find a kowtow

'''
We might also be interested in "three moves, two of them legal"
Find the moves that are objectively worse than others and rule them out. Like dragon. Then you'
ice > dragon, flying = poison. Could go through the game and work out groups that each is super effective against, identify subsets
'''

T = [A1,A2,A3,A4,A5]
T_nums = [0,0,0,0,0]
T_singulars = [0,0,0,0,0]

for t in T:
	for p in t:
		if p not in ptypelist:
			print("type error!")
			
only_show_failures = 0
num_kowtows = 0

last_pokemon_name = ""
last_opponenttype_1 = ""
last_opponenttype_2 = ""
with open("PokemonTrainers.txt" ) as walkthru:
	if "Confuse Ray" in sillymoves:
		#Hitmonchan, venomoth, and that one butterfree (it can be defeated in yellow!)
		problemcases = [set(['Fighting', 'Electric', 'Ice', 'Normal']), set(['Psychic', 'Grass', 'Bug', 'Poison']), set(['Psychic', 'Grass', 'Poison'])]
	elif "Leech Life" in sillymoves:
		#Lapras in addition to the above
		problemcases = [set(['Fighting', 'Electric', 'Ice', 'Normal']), set(['Psychic', 'Grass', 'Poison']), set(['Psychic', 'Grass', 'Poison']), set(['Ghost', 'Water', 'Ice', 'Normal'])]
	for line in walkthru:
		if line[:8] == "Trainer:" and only_show_failures == 0:
			print("")
			print(line[9:43])
		if line[0] == "#":
			last_pokemon_name = line[6:17]
			last_opponenttype_1,last_opponenttype_2 = read_opponent_type( line )
		if line[0:3] == " ~ ":
			movetypes = read_opponent_moves(line)
			
			if movetypes != 0:
				if only_show_failures == 1:
					got_one = 0
					for t in T:
						if A_hypereffectiveagainst_B(
							t[0],t[1],									t[2],t[3],t[4], #the types, then the moves
							last_opponenttype_1,last_opponenttype_2,	movetypes[0],movetypes[1],movetypes[2],movetypes[3]
						): got_one = 1
					if got_one == 0:
						print(last_pokemon_name, last_opponenttype_1,last_opponenttype_2,	movetypes[0],movetypes[1],movetypes[2],movetypes[3])
				else:
					print("	" + last_pokemon_name)
					
					num_options = 0
					most_recent_successful_t = 5
					
					for i in range(5):
						usable_move_string = A_hypereffectiveagainst_B(
							T[i][0],T[i][1],									T[i][2],T[i][3],T[i][4],
							last_opponenttype_1,last_opponenttype_2,	movetypes[0],movetypes[1],movetypes[2],movetypes[3] )
							
						if usable_move_string != "":
							T_nums[i] = T_nums[i] + 1
							num_options = num_options + 1
							most_recent_successful_t = i
							
							recommendation_string = "		" + T[i][0] + ", " + T[i][1] + " -"
							while len(recommendation_string) < 19:
								recommendation_string = recommendation_string + " "
							recommendation_string = recommendation_string + usable_move_string
							print(recommendation_string)
						
					if num_options == 1:
						T_singulars[most_recent_successful_t] = T_singulars[most_recent_successful_t] + 1
					if num_options == 0:
						print("		KOWTOW")
						num_kowtows = num_kowtows + 1
							
							
print(" ")
if only_show_failures == 0:
	for i in range(5):
		print( "%s has the option to do %s, and can uniquely do %s" % (T[i],T_nums[i], T_singulars[i]) )
		
print("number we kowtow to: %s" % num_kowtows)