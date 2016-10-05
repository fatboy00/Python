# program to Display a Chessboard
# 22 December 2015



# Define list variables
piececode = [] # King =1, Queen =2, Bishop =3, Knight =4, Rook=5, Pawn =6
colouris = [] #1=white, 0=none, -1=black
pieceis = [] # String representing piece "wr" = white rook.....

#-----------------------------------------
def drawchessboard (): # print Chessboard
	for y in range(0,9):
		for x in range(0,9):
			if y==0:
				if x==0:
					print "   ",
				else:
					print x, " ",
			else:
				if x==0:
					print y, "|",
				else:
					print "%s|" % pieceis[y][x],
		print ""
		print "   --- --- --- --- --- --- --- ---"

#-----------------------------------------
def movethepiece(xfrom,yrom,xto,yto, piececode, pieceis, colouris):  # move the piece
	piececode[yto][xto] = piececode[yfrom][xfrom]
	pieceis[yto][xto] = pieceis[yfrom][xfrom]
	colouris[yto][xto] = colouris[yfrom][xfrom]
	piececode[yfrom][xfrom] = 0
	pieceis[yfrom][xfrom] = "  "
	colouris[yfrom][xfrom] = 0 
	return colouris , pieceis , piececode

#-----------------------------------------
def askcoordinates(pieceis): # request coordinates

	print " enter coordinates of piece to move:"
	xfrom = input("X-Coordinate? :")
	yfrom = input("Y-Coordinate? :")

	print " enter coordinates to move to:"
	xto = input("X-Coordinate? :")
	yto = input("Y-Coordinate? :")

	print "you want to move %s from %d,%d to %d,%d " % (pieceis[yfrom][xfrom],xfrom,yfrom, xto,yto)
	return xfrom , yfrom , xto , yto
#-----------------------------------------
def blackorwhite(col): # return a string with the colour
	if col==1:
		return "white"
	elif col==2:
		return "black"
	else:
		return "none"

#-----------------------------------------
def setdeltas(xfrom,yfrom,xto,yto): # return deltas
	xstep=1
	ystep=1
	xdelta = xto - xfrom
	if xdelta<0:
		xstep=-1
	ydelta = yto - yfrom
	if ydelta<0:
		ystep=-1
	
	xdelta = xdelta * xdelta
	xdelta = xdelta ** 0.5
	ydelta = ydelta * ydelta
	ydelta = ydelta ** 0.5
	return xdelta , ydelta, xstep, ystep
#-----------------------------------------
def diagonal(xfrom,yfrom,xto,yto,colouris): # check diagonal move ok? 
	xdelta , ydelta, xstep, ystep = setdeltas(xfrom,yfrom,xto,yto)
	diagonalmove =1
	if xdelta <> ydelta:
		diagonalmove = 0
	else:
		j = yfrom
		for i in range (xfrom + xstep, xto + xstep , xstep):
			j = j + ystep
			if colouris[j][i]>0:
				diagonalmove = 0
			
	return diagonalmove
#-----------------------------------------
def straight(xfrom,yfrom,xto,yto,colouris): # check straight move ok? 
	xdelta , ydelta, xstep, ystep = setdeltas(xfrom,yfrom,xto,yto)
	straightmove = 1
	if xdelta > 0 and ydelta > 0: # Cannot move on both dimensions
		straightmove= 0
	else:
		if xdelta > 0: # if movement on x axis check nothing in way
			for i in range (xfrom + xstep , xto + xstep , xstep):
				if colouris[yfrom][i]>0:
					straightmove = 0					
		else:	# if movement on y axis check nothing in way
			for i in range (yfrom + ystep , yto + ystep , ystep):
				if colouris[i][xfrom]>0:
					straightmove = 0
			
	return straightmove
#-----------------------------------------
def movepawn(xfrom,yfrom,xto,yto,opponent): # move a pawn!
	move = 1 # set move legal
	xdelta , ydelta, xstep, ystep = setdeltas(xfrom,yfrom,xto,yto)

	# check first move
	if ystep > 0 and yfrom == 2:
		firstmove=  1
	elif ystep < 0  and yfrom == 7:
		firstmove =1
	else:
		firstmove = 0


	if firstmove == 1:
		if ydelta > 2: # checked havent moved more than two "y" cell
			move = 0
	elif ydelta > 1:  # checked havent moved more than one "y" cell
		move = 0

	# check take opponent or move to space
	if move == 1 and opponent > 0:
		if xdelta <> 1 or ydelta <> 1:
			move = 0
	elif move == 1 and xdelta <> 0:
		move = 0
	if move == 0:
		print "illegal pawn move"
	return move
	
#-----------------------------------------

def moveknight(xfrom,yfrom,xto,yto): # move a knight
	move = 1 # set move legal
	xdelta , ydelta, xstep, ystep = setdeltas(xfrom,yfrom,xto,yto)

	if ((xdelta * xdelta) + (ydelta * ydelta)) <> 5:
		move = 0
	elif (xdelta * xdelta) >=5:
		move = 0
	elif (ydelta * ydelta) >=5:
		move = 0

	if move == 0:
		print "illegal knight move"
	return move
#-----------------------------------------
def moverook(xfrom,yfrom,xto,yto,colouris): # move a rook 
	move = straight(xfrom,yfrom,xto,yto,colouris)

	if move == 0:
		print "illegal rook move"		
	return move

#-----------------------------------------
def movebishop(xfrom,yfrom,xto,yto,colouris): # move a bishop 
	move = diagonal(xfrom,yfrom,xto,yto,colouris)

	if move == 0:
		print "illegal bishop move"		
	return move

#-----------------------------------------
def movequeen(xfrom,yfrom,xto,yto,colouris): # move a queen
	xdelta , ydelta, xstep, ystep = setdeltas(xfrom,yfrom,xto,yto)
	if xdelta == 0 or ydelta == 0:
		move = straight(xfrom,yfrom,xto,yto,colouris)	
	else:
		move = diagonal(xfrom,yfrom,xto,yto,colouris)

	if move == 0:
		print "illegal queen move"		
	return move
#-----------------------------------------
def moveking(xfrom,yfrom,xto,yto,colouris): # move a king
	xdelta , ydelta, xstep, ystep = setdeltas(xfrom,yfrom,xto,yto)
	if xdelta == 0 or ydelta == 0:
		move = straight(xfrom,yfrom,xto,yto,colouris)	
	else:
		move = diagonal(xfrom,yfrom,xto,yto,colouris)
	
	if xdelta > 1 or ydelta > 1:
		move = 0

	if move == 0:
		print "illegal king move"		
	return move

#-----------------------------------------


###  start the execution ###
# setup the board
# Append empty lists to first eight indexes
for y in range(0,9):
	pieceis.append([])
	piececode.append([])
	colouris.append([])

# Define blank starting pieces on chessboard
for y in range(0,9):
	for x in range(0,9):
		pieceis[y].append("  ")	
		colouris[y].append(0)
		piececode[y].append(0)

# Define starting pieces on chessboard
for y in range(1,9):
		
	for x in range(1,9):
		if y==1:
			colouris[y][x]=1
			if x==1:
				pieceis[y][x]= "wr"
				piececode[y][x]=5
			elif  x==2:
				pieceis[y][x]= "wk"
				piececode[y][x]=4
			elif  x==3:
				pieceis[y][x]= "wb"
				piececode[y][x]=3
			elif  x==4:
				pieceis[y][x]= "wQ"
				piececode[y][x]=2
			elif  x==5:
				pieceis[y][x]= "wK"
				piececode[y][x]=1
			elif  x==6:
				pieceis[y][x]= "wb"
				piececode[y][x]=3
			elif  x==7:
				pieceis[y][x]= "wk"
				piececode[y][x]=4
			elif  x==8:
				pieceis[y][x]= "wr"
				piececode[y][x]=5
		elif y==2:
			colouris[y][x]=1
			pieceis[y][x]= "wp"
			piececode[y][x]=6
			
		elif y==7:
			colouris[y][x]=2
			pieceis[y][x]= "bp"
			piececode[y][x]=6
		elif y==8:
			colouris[y][x]=2
			if x==1:
				pieceis[y][x]= "br"
				piececode[y][x]=5
			elif  x==2:
				pieceis[y][x]= "bk"
				piececode[y][x]=4
			elif  x==3:
				pieceis[y][x]= "bb"
				piececode[y][x]=3
			elif  x==4:
				pieceis[y][x]= "bQ"
				piececode[y][x]=2
			elif  x==5:
				pieceis[y][x]= "bK"
				piececode[y][x]=1
			elif  x==6:
				pieceis[y][x]= "bb"
				piececode[y][x]=3
			elif  x==7:
				pieceis[y][x]= "bk"
				piececode[y][x]=4
			elif  x==8:
				pieceis[y][x]= "br"
				piececode[y][x]=5	
					
# draw the chessboard
drawchessboard()
# initialize
colourtomove=1 # set colour to white
legalmove = 1 # reset legal move variable to legal
keepplaying = "Y"
#-----------------------------------------

###  start the game ###

while keepplaying == "Y" or keepplaying == "y":

	# ask which piece to move
	xfrom,yfrom,xto,yto = askcoordinates(pieceis)


	# is this a legitimate move?

	# 1.  is there a piece at starting location?
	if legalmove==1:
		if colouris[yfrom][xfrom] == 0:
			legalmove=0
			print "no piece at start location!"

	# 2.  is move on the board?
	if legalmove==1:
		if xto < 1 or xto >8:
			legalmove=0
			print "move is off the board!"
		if yto < 1 or yto >8:
			legalmove=0
			print "move is off the board!"

	# 3.  is this the right colour to move next?
	if legalmove==1:
		if colouris[yfrom][xfrom] <> colourtomove:
			legalmove=0
			print "wrong colour, move %s" % blackorwhite(colourtomove)

	# 4.  is destination cell empty?
	if legalmove==1:
		if colouris[yto][xto] == colourtomove:
			legalmove=0
			print "cannot move to square with your own piece"

	# 5.  Is this move allowed for this piece (including is a piece in the way)
	# pawn first
	if legalmove==1 and piececode[yfrom][xfrom] == 6:
		legalmove = movepawn(xfrom,yfrom,xto,yto, colouris[yto][xto])
	 
	# knight 
	if legalmove==1 and piececode[yfrom][xfrom] == 4:
		legalmove = moveknight(xfrom,yfrom,xto,yto)

	# rook
	if legalmove==1 and piececode[yfrom][xfrom] == 5:
		legalmove = moverook(xfrom,yfrom,xto,yto,colouris)

	# bishop
	if legalmove==1 and piececode[yfrom][xfrom] == 3:
		legalmove = movebishop(xfrom,yfrom,xto,yto,colouris)

	# queen
	if legalmove==1 and piececode[yfrom][xfrom] == 2:
		legalmove = movequeen(xfrom,yfrom,xto,yto,colouris)

	# king
	if legalmove==1 and piececode[yfrom][xfrom] == 1:
		legalmove = moveking(xfrom,yfrom,xto,yto,colouris)

	if legalmove == 0:
		print "you cannot make this move"	
		xto=xfrom
		yto=yfrom
	else:
		# move the piece
		colouris, pieceis, piececode = movethepiece(xfrom,yfrom,xto,yto,piececode, pieceis, colouris)
		# reset the colour
		if colourtomove == 1:
			colourtomove =2
		else:
			colourtomove = 1


	### ----------####
	# move over - reset everything:
	# redraw the board
	drawchessboard()
	# reset move legality
	legalmove = 1
	
	keepplaying = raw_input("Keep Playing (Y/N)?")

print " well played ....goodbye"