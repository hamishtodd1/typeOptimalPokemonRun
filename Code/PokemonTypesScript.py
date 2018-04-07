
import sys

sillymoves = [	
				#doesn't affect you at all
				"Acid Armor", "Agility", "Amnesia", "Barrier", "Defense Curl", "Double Team", "Focus Energy", "Growth", "Harden", "Haze", "Light Screen", "Meditate","Metronome", "Mimic",
					"Minimize", "Mirror Move", "Mist", "Recover", "Rest", "Reflect", "Sharpen", "Softboiled", "Splash", "Substitute","Swords Dance", "Teleport", "Transform", "Withdraw", 
					
				#no damage
				"Conversion","Disable","Flash","Glare","Growl","Kinesis","Leer","Lovely Kiss","Poison Gas","PoisonPowder","Roar","Sand-Attack","Screech",
					"Sing","Sleep Powder","SmokeScreen","Spore","String Shot","Stun Spore","Supersonic","Tail Whip","Thunder Wave","Toxic","Whirlwind","Hypnosis", "Confuse Ray",
				
				#these moves aren't affected by your type; but they may cause the sound effect and message, who knows
				"Dragon Rage","Night Shade","SonicBoom","Seismic Toss","Leech Seed"
					]

ptypelist = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon"]

#a for attacker, d for defender. 1, 2, 0.5, or 0
def effective( a, d ):
	h = 0.5
	t = 10
	e = 11
	w = 12
	i = 13
	f = 14
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
		if d == ptypelist[f]: return 1
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
		if d == ptypelist[f]: return h
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
		if d == ptypelist[f]: return h
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
		if d == ptypelist[f]: return h
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
		if d == ptypelist[f]: return h
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
		if d == ptypelist[f]: return 2
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
		if d == ptypelist[f]: return 1
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
		if d == ptypelist[f]: return 1
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
		if d == ptypelist[f]: return 1
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
		if d == ptypelist[f]: return 1
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
		if d == ptypelist[f]: return 1
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
		if d == ptypelist[f]: return 1
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
		if d == ptypelist[f]: return 1
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
		if d == ptypelist[f]: return 1
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
		if d == ptypelist[f]: return 2

def twoeffective(a, d1, d2 ):
	component1 = effective( a, d1 )

	if d2 == d1:
		component2 = 1
	else:
		component2 = effective( a, d2 )

	return component1 * component2

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
	print("  %s	can't handle	%s" % (u,u_failures) )

#------------------------------------------------------------------------------
#main
#initial list set up
O = [] #O for opponents

master_opponent_names = []

last_pokemonname_read = ""
with open("PokemonTrainers.txt" ) as walkthru:
	if "Confuse Ray" in sillymoves:
		#Hitmonchan, venomoth, and that one butterfree
		problemcases = [set(['Fighting', 'Electric', 'Ice', 'Normal']), set(['Psychic', 'Bug']) ]
	elif "Leech Life" in sillymoves:
		#Lapras in addition to the above
		problemcases = [set(['Fighting', 'Electric', 'Ice', 'Normal']), set(['Psychic', 'Grass', 'Poison']), set(['Psychic', 'Grass', 'Poison']), set(['Ghost', 'Water', 'Ice', 'Normal'])]
	#problemcases.append(set(['Flying', 'Electric']))
	#problemcases.append(set(['Flying', 'Fire']))
	#problemcases.append(set(['Flying', 'Ice']))
	total_opponent_pokemon = 0
	for line in walkthru:
		if line[0] == "#":
			last_pokemonname_read = line[6:33]
		if line[0:3] == " ~ ":
			total_opponent_pokemon += 1
			ptypes = set([])
			unprocessed_moves = line[3:]
			unprocessed_moves = unprocessed_moves.rstrip()
			unprocessed_moves = unprocessed_moves.rstrip('\n')
			moves = unprocessed_moves.split(", ")

			newmovetype = move_to_type( moves[0])
			if newmovetype != 0:
				ptypes.add( move_to_type( moves[0]) )
			if len( moves ) > 1:
				newmovetype = move_to_type( moves[1])
				if newmovetype not in ptypes and newmovetype != 0:
					ptypes.add( newmovetype )
			if len( moves ) > 2:
				newmovetype = move_to_type( moves[2])
				if newmovetype not in ptypes and newmovetype != 0:
					ptypes.add( newmovetype )
			if len( moves ) > 3:
				newmovetype = move_to_type( moves[3])
				if newmovetype not in ptypes and newmovetype != 0:
					ptypes.add( newmovetype )

			walkthru.readlines

			#check it's not Bruno's Hitmonchan, or Sabrina's venomoth. Psychic and bug, what a combo. Sabrina doesn't have venomoth in Yellow
			newmovetypeset = 1

			for problemcase in problemcases:
				if ptypes == problemcase:
					print("we're going to ignore the pokemon that has this set of moves: %s" % unprocessed_moves)
					problemcases.remove(problemcase)
					newmovetypeset = 0

			#check we don't already have one like this
			for movetypeset in O:
				if ptypes <= movetypeset: #hopefully would also catch an empty movelist, i.e. a pokemon with only one, silly, move
					newmovetypeset = 0
					break #this movetypeset already exists, or there's an even harder version
				elif movetypeset < ptypes:
					#we have a superior option
					master_opponent_names.remove( master_opponent_names[ O.index(movetypeset) ] )
					O.remove( movetypeset )
			if newmovetypeset == 1:
				#print(last_pokemonname_read, ptypes)
				O.append( ptypes )
				master_opponent_names.append(last_pokemonname_read)

print("\nOpponents length: %s looking for subsets narrowed down to %s. List:\n" % (total_opponent_pokemon,len( O ) ) )
#there were 30 in there before sillymoves.
for p in master_opponent_names:
	print(p, O[master_opponent_names.index(p)])
	
print("\n")



T = [] #T for team members
T_numbers = []
T_dealswith = []
for ptype1 in ptypelist:
	if ptype1 == "Ice": continue
	#single-typers get their type twice. 
	for ptype2 in ptypelist:
		if ptype2 == "Ice" or [ptype2, ptype1] in T:
			continue		
		T.append( [ptype1, ptype2] )
		T_numbers.append( 0 )
		T_dealswith.append([])

singularly_powerful_T = []
duolarly_powerful_T = [] #so elements n and n+1 will be able to bring someone down, where n is an even number
for o in O:
	o_number_found = 0
	for t in T:
		dealswithit = 1
		for a in o:
			effect = twoeffective( a, t[0], t[1] )
			if effect != 0 and effect != 0.5 and effect != 0.25:
				#this team member can't deal with this opponent
				dealswithit = 0
				break
		if dealswithit == 1:
			o_number_found += 1
			T_numbers[ T.index(t) ] += 1
			T_dealswith[ T.index(t) ].append( o )
			
			#if T_numbers[ T.index(t) ] > 3:
				#print T_numbers[ T.index(t) ]
			#if t == ['Water', 'Ghost'] or t == ['Ground', 'Rock'] or t == ['Psychic', 'Rock']:
				#print t #"%s can deal with %s" % (t, o)
	if o_number_found == 0:
		print("Fuck. %s has no team members to beat them(?)" % o)
	if o_number_found == 1:
		for t in T:
			if o in T_dealswith[ T.index(t) ]:
				singularly_powerful_T.append(t)
		print("%s can only be defeated by ONE team member: %s" % (o, singularly_powerful_T[len(singularly_powerful_T)-1])) #['Water', 'Ghost'] can uniquely do cloysters and shellders and Gary's Blastoise
	if o_number_found == 2:
		for t in T:
			if o in T_dealswith[ T.index(t) ]:
				duolarly_powerful_T.append(t)
		print("%s can only be defeated by TWO team members: %s and %s" % (o, duolarly_powerful_T[len(duolarly_powerful_T)-1], duolarly_powerful_T[len(duolarly_powerful_T)-2]))

#if something is singularly powerful, it doesn't matter if it is duolarly powerful, because it is a necessity anyway
for s in singularly_powerful_T:
	i = 0
	while i < len( duolarly_powerful_T ) / 2:
		if s == duolarly_powerful_T[i] or s == duolarly_powerful_T[i+1]:
			duolarly_powerful_T.pop(i)
			duolarly_powerful_T.pop(i+1)
		else:
			i += 1
			

'''for t in T:
	dealswithit = 1
	#if these are all ineffective for the 
	for a in ["Bug", "Normal"]:
		effect = twoeffective( a, t[0], t[1] )
		if effect != 0 and effect != 0.5 and effect != 0.25:
			#this team member can't deal with this opponent
			dealswithit = 0
			break
	if dealswithit == 1:
		print "%s can deal with zubat and golbat" % t'''

old_T_len = len(T)
#some t's are objectively superior to others
#if you remove an item of the list, item that takes its place will be skipped
#This is another place we could make things more 'plausible' - if i and j are the same, you could throw away the implausible one
i = 0
j = 0
while i < len(T) - 1:
	dont_increment_i = 0
	j=i+1
	while j < len(T):
		dont_increment_j = 0
		#if T_dealswith[ i ] == T_dealswith[ j ]: #if you are interested in plausibility, though it doesn't seem to rule out any usable pokemon
			#print("we're about to get rid of %s because it's inferior to %s" % (T[j],T[i]))
		if T_dealswith[ i ] >= T_dealswith[ j ]:
			T_dealswith.pop( j )
			T_numbers.pop( j )
			T.pop(j)
			dont_increment_j = 1
		elif T_dealswith[ i ] < T_dealswith[ j ]:
			T_dealswith.pop( i )
			T_numbers.pop( i )
			T.pop(i)
			dont_increment_i = 1
			#so we DON'T increment i because we need to do its index again
			break
		if dont_increment_j == 0:
			j += 1
	if dont_increment_i == 0:
		i += 1

print("\nfrom the %s combinations of types we have identified %s useful ones\n" % (old_T_len,len(T)) )

'''for o in O:
	if o in T_dealswith[T.index(['Water', 'Ghost']) ]:
		print "%s is dealt with by water/ghost" % o
	elif o in T_dealswith[T.index(['Ground', 'Rock']) ]:
		print "%s is dealt with by ground/rock" % o
	else:
		print "%s isn't dealt with!" % o'''

for u in T:
	if T.index(u) == T.index(['Water', 'Ghost']):
		continue
	for v in T:
		if T.index(v) == T.index(['Water', 'Ghost']) or T.index(v) <= T.index(u):
			continue
		for t in T:
			if T.index(t) == T.index(['Water', 'Ghost']) or T.index(t) <= T.index(v):
				continue
			for w in T:
				if T.index(w) == T.index(['Water', 'Ghost']) or T.index(w) <= T.index(t):
					continue

				dealtwith = []

				for s in singularly_powerful_T:
					for o in T_dealswith[ T.index(s) ]:
						if o not in dealtwith:
							dealtwith.append(o)

				for o in T_dealswith[ T.index(u) ]:
					if o not in dealtwith:
						dealtwith.append(o)
				for o in T_dealswith[ T.index(v) ]:
					if o not in dealtwith:
						dealtwith.append(o)
				for o in T_dealswith[ T.index(t) ]:
					if o not in dealtwith:
						dealtwith.append(o)
				for o in T_dealswith[ T.index(w) ]:
					if o not in dealtwith:
						dealtwith.append(o)

				teambroken = 0
				for o in O:
					if o not in dealtwith:
						teambroken = 1 #this team won't work
						break
				if teambroken == 0:
					print("\nA good team: %s, %s, %s, %s" % (u, v, w, t))
					print_failures(u)
					print_failures(v)
					print_failures(w)
					print_failures(t)
	if len(T) >30:
		print('done all combinations with pokemon number %s in slot 1' % T.index(u))
		
print("\nthe teams above must have added to them the singularly powerful pokemon: ")
for p in singularly_powerful_T:
	print_failures(p)

'''outputs!
this one would also work with the replacement of Confuse Ray with Leech Life and the ignoring of Lapras
['Water', 'Electric'], ['Ground', 'Rock'], ['Psychic', 'Rock'], ['Flying', 'Ghost'], ['Water', 'Ghost']
But we go for this because it's closest to being real:
['Water', 'Rock'], ['Ground', 'Rock'], ['Psychic', 'Ghost'], ['Flying', 'Ghost'], ['Water', 'Ghost']
Kabutops, Geodude/rhydon/onix, Hoopa or Jynx(psychic/ghost), Drifblim or Haunter (ghost/flying), Jellicent or Tentacruel (looks water/ghostly)

'''









