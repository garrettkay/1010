import random
import copy

pieces = []
pieceWeights = [["H2",3],["H3",3],["H4",2],["H5",2],["V2",3],["V3",3],["V4",2],["V5",2],["B1",2],["B2",6],["B3",2],["L2UL",2],["L2UR",2],["L2DL",2],["L2DR",2],["L3UL",1],["L3UR",1],["L3DL",1],["L3DR",1]]
attributeWeights = []
board = [	[False,False,False,False,False,False,False,False,False,False],
			[False,False,False,False,False,False,False,False,False,False],
			[False,False,False,False,False,False,False,False,False,False],
			[False,False,False,False,False,False,False,False,False,False],
			[False,False,False,False,False,False,False,False,False,False],
			[False,False,False,False,False,False,False,False,False,False],
			[False,False,False,False,False,False,False,False,False,False],
			[False,False,False,False,False,False,False,False,False,False],
			[False,False,False,False,False,False,False,False,False,False],
			[False,False,False,False,False,False,False,False,False,False]]
score = 0

def generatePieces():
	global pieces
	pieces = random.choices(["H2","H3","H4","H5","V2","V3","V4","V5","B1","B2","B3","L2","L3","R2","R3","T2","T3","J2","J3"], weights = (3,3,2,2,3,3,2,2,2,6,2,2,1,2,1,2,1,2,1), k = 3)

def printBoard():
	print("  0 1 2 3 4 5 6 7 8 9")
	for r in range(10):
		print(r,end="")
		for c in range(10):
			if board[r][c]:
				print(" ■",end="")
			else:
				print("  ",end="")
		print("")

def move(piece,location):
	global pieces
	global score
	if location < 0 or location >= 100:
		return "INVALID LOCATION"
	if piece in pieces:
		r = location // 10
		c = location % 10
		match piece:
			case "H2":
				if c >= 9:
					return "INVALID LOCATION"
				if board[r][c] == False and board[r][c + 1] == False:
					board[r][c] = True
					board[r][c + 1] = True
					pieces.remove(piece)
					score += 2
					return "SUCCESS"
				else:
					return "INVALID PLAY"
			case "H3":
				if c >= 8:
					return "INVALID LOCATION"
				if board[r][c] == False and board[r][c + 1] == False and board[r][c + 2] == False:
					board[r][c] = True
					board[r][c + 1] = True
					board[r][c + 2] = True
					pieces.remove(piece)
					score += 3
					return "SUCCESS"
				else:
					return "INVALID PLAY"
			case "H4":
				if c >= 7:
					return "INVALID LOCATION"
				if board[r][c] == False and board[r][c + 1] == False and board[r][c + 2] == False and board[r][c + 3] == False:
					board[r][c] = True
					board[r][c + 1] = True
					board[r][c + 2] = True
					board[r][c + 3] = True
					pieces.remove(piece)
					score += 4
					return "SUCCESS"
				else:
					return "INVALID PLAY"
			case "H5":
				if c >= 6:
					return "INVALID LOCATION"
				if board[r][c] == False and board[r][c + 1] == False and board[r][c + 2] == False and board[r][c + 3] == False and board[r][c + 4] == False:
					board[r][c] = True
					board[r][c + 1] = True
					board[r][c + 2] = True
					board[r][c + 3] = True
					board[r][c + 4] = True
					pieces.remove(piece)
					score += 5
					return "SUCCESS"
				else:
					return "INVALID PLAY"
			case "V2":
				if r >= 9:
					return "INVALID LOCATION"
				if board[r][c] == False and board[r + 1][c] == False:
					board[r][c] = True
					board[r + 1][c] = True
					pieces.remove(piece)
					score += 2
					return "SUCCESS"
				else:
					return "INVALID PLAY"
			case "V3":
				if r >= 8:
					return "INVALID LOCATION"
				if board[r][c] == False and board[r + 1][c] == False and board[r + 2][c] == False:
					board[r][c] = True
					board[r + 1][c] = True
					board[r + 2][c] = True
					pieces.remove(piece)
					score += 3
					return "SUCCESS"
				else:
					return "INVALID PLAY"
			case "V4":
				if r >= 7:
					return "INVALID LOCATION"
				if board[r][c] == False and board[r + 1][c] == False and board[r + 2][c] == False and board[r + 3][c] == False:
					board[r][c] = True
					board[r + 1][c] = True
					board[r + 2][c] = True
					board[r + 3][c] = True
					pieces.remove(piece)
					score += 4
					return "SUCCESS"
				else:
					return "INVALID PLAY"
			case "V5":
				if r >= 6:
					return "INVALID LOCATION"
				if board[r][c] == False and board[r + 1][c] == False and board[r + 2][c] == False and board[r + 3][c] == False and board[r + 4][c] == False:
					board[r][c] = True
					board[r + 1][c] = True
					board[r + 2][c] = True
					board[r + 3][c] = True
					board[r + 4][c] = True
					pieces.remove(piece)
					score += 5
					return "SUCCESS"
				else:
					return "INVALID PLAY"
			case "B1":
				if board[r][c] == False:
					board[r][c] = True
					pieces.remove(piece)
					score += 1
					return "SUCCESS"
				else:
					return "INVALID PLAY"
			case "B2":
				if c >= 9 or r >= 9:
					return "INVALID LOCATION"
				if board[r][c] == False and board[r][c + 1] == False and board[r + 1][c] == False and board[r + 1][c + 1] == False:
					board[r][c] = True
					board[r][c + 1] = True
					board[r + 1][c] = True
					board[r + 1][c + 1] = True
					pieces.remove(piece)
					score += 4
					return "SUCCESS"
				else:
					return "INVALID PLAY"
			case "B3":
				if c >= 8 or r >= 8:
					return "INVALID LOCATION"
				if board[r][c] == False and board[r][c + 1] == False and board[r][c + 2] == False and board[r + 1][c] == False and board[r + 1][c + 1] == False and board[r + 1][c + 2] == False and board[r + 2][c] == False and board[r + 2][c + 1] == False and board[r + 2][c + 2] == False:
					board[r][c] = True
					board[r][c + 1] = True
					board[r][c + 2] = True
					board[r + 1][c] = True
					board[r + 1][c + 1] = True
					board[r + 1][c + 2] = True
					board[r + 2][c] = True
					board[r + 2][c + 1] = True
					board[r + 2][c + 2] = True
					pieces.remove(piece)
					score += 9
					return "SUCCESS"
				else:
					return "INVALID PLAY"
			case "L2":
				if c >= 9 or r >= 9:
					return "INVALID LOCATION"
				if board[r][c] == False and board[r + 1][c] == False and board[r + 1][c + 1] == False:
					board[r][c] = True
					board[r + 1][c] = True
					board[r + 1][c + 1] = True
					pieces.remove(piece)
					score += 3
					return "SUCCESS"
				else:
					return "INVALID PLAY"
			case "L3":
				if c >= 8 or r >= 8:
					return "INVALID LOCATION"
				if board[r][c] == False and board[r + 1][c] == False and board[r + 2][c] == False and board[r + 2][c + 1] == False and board[r + 2][c + 2] == False:
					board[r][c] = True
					board[r + 1][c] = True
					board[r + 2][c] = True
					board[r + 2][c + 1] = True
					board[r + 2][c + 2] = True
					pieces.remove(piece)
					score += 5
					return "SUCCESS"
				else:
					return "INVALID PLAY"
			case "R2":
				if c >= 9 or r >= 9:
					return "INVALID LOCATION"
				if board[r][c] == False and board[r][c + 1] == False and board[r + 1][c] == False:
					board[r][c] = True
					board[r][c + 1] = True
					board[r + 1][c] = True
					pieces.remove(piece)
					score += 3
					return "SUCCESS"
				else:
					return "INVALID PLAY"
			case "R3":
				if c >= 8 or r >= 8:
					return "INVALID LOCATION"
				if board[r][c] == False and board[r][c + 1] == False and board[r][c + 2] == False and board[r + 1][c] == False and board[r + 2][c] == False:
					board[r][c] = True
					board[r][c + 1] = True
					board[r][c + 2] = True
					board[r + 1][c] = True
					board[r + 2][c] = True
					pieces.remove(piece)
					score += 5
					return "SUCCESS"
				else:
					return "INVALID PLAY"
			case "T2":
				if c >= 9 or r >= 9:
					return "INVALID LOCATION"
				if board[r][c] == False and board[r][c + 1] == False and board[r + 1][c + 1] == False:
					board[r][c] = True
					board[r][c + 1] = True
					board[r + 1][c + 1] = True
					pieces.remove(piece)
					score += 3
					return "SUCCESS"
				else:
					return "INVALID PLAY"
			case "T3":
				if c >= 8 or r >= 8:
					return "INVALID LOCATION"
				if board[r][c] == False and board[r][c + 1] == False and board[r][c + 2] == False and board[r + 1][c + 2] == False and board[r + 2][c + 2] == False:
					board[r][c] = True
					board[r][c + 1] = True
					board[r][c + 2] = True
					board[r + 1][c + 2] = True
					board[r + 2][c + 2] = True
					pieces.remove(piece)
					score += 5
					return "SUCCESS"
				else:
					return "INVALID PLAY"
			case "J2":
				if c >= 9 or r >= 9:
					return "INVALID LOCATION"
				if board[r][c + 1] == False and board[r + 1][c] == False and board[r + 1][c + 1] == False:
					board[r][c + 1] = True
					board[r + 1][c] = True
					board[r + 1][c + 1] = True
					pieces.remove(piece)
					score += 3
					return "SUCCESS"
				else:
					return "INVALID PLAY"
			case "J3":
				if c >= 8 or r >= 8:
					return "INVALID LOCATION"
				if board[r][c + 2] == False and board[r + 1][c + 2] == False and board[r + 2][c] == False and board[r + 2][c + 1] == False and board[r + 2][c + 2] == False:
					board[r][c + 2] = True
					board[r + 1][c + 2] = True
					board[r + 2][c] = True
					board[r + 2][c + 1] = True
					board[r + 2][c + 2] = True
					pieces.remove(piece)
					score += 5
					return "SUCCESS"
				else:
					return "INVALID PLAY"
	else:
		return "INVALID PIECE"

def testMove(piece,location):
	testBoard = copy.deepcopy(board)
	subScore = 0
	tempPieces = copy.copy(pieces).remove(piece)
	r = location // 10
	c = location % 10
	match piece:
		case "H2":
			subScore += 2
			testBoard[r][c] = True
			testBoard[r][c + 1] = True
		case "H3":
			subScore += 3
			testBoard[r][c] = True
			testBoard[r][c + 1] = True
			testBoard[r][c + 2] = True
		case "H4":
			subScore += 4
			testBoard[r][c] = True
			testBoard[r][c + 1] = True
			testBoard[r][c + 2] = True
			testBoard[r][c + 3] = True
		case "H5":
			subScore += 5
			testBoard[r][c] = True
			testBoard[r][c + 1] = True
			testBoard[r][c + 2] = True
			testBoard[r][c + 3] = True
			testBoard[r][c + 4] = True
		case "V2":
			subScore += 2
			testBoard[r][c] = True
			testBoard[r + 1][c] = True
		case "V3":
			subScore += 3
			testBoard[r][c] = True
			testBoard[r + 1][c] = True
			testBoard[r + 2][c] = True
		case "V4":
			subScore += 4
			testBoard[r][c] = True
			testBoard[r + 1][c] = True
			testBoard[r + 2][c] = True
			testBoard[r + 3][c] = True
		case "V5":
			subScore += 5
			testBoard[r][c] = True
			testBoard[r + 1][c] = True
			testBoard[r + 2][c] = True
			testBoard[r + 3][c] = True
			testBoard[r + 4][c] = True
		case "B1":
			subScore += 1
			testBoard[r][c] = True
		case "B2":
			subScore += 4
			testBoard[r][c] = True
			testBoard[r][c + 1] = True
			testBoard[r + 1][c] = True
			testBoard[r + 1][c + 1] = True
		case "B3":
			subScore += 9
			testBoard[r][c] = True
			testBoard[r][c + 1] = True
			testBoard[r][c + 2] = True
			testBoard[r + 1][c] = True
			testBoard[r + 1][c + 1] = True
			testBoard[r + 1][c + 2] = True
			testBoard[r + 2][c] = True
			testBoard[r + 2][c + 1] = True
			testBoard[r + 2][c + 2] = True
		case "L2":
			subScore += 3
			testBoard[r][c] = True
			testBoard[r + 1][c] = True
			testBoard[r + 1][c + 1] = True
		case "L3":
			subScore += 5
			testBoard[r][c] = True
			testBoard[r + 1][c] = True
			testBoard[r + 2][c] = True
			testBoard[r + 2][c + 1] = True
			testBoard[r + 2][c + 2] = True
		case "R2":
			subScore += 3
			testBoard[r][c] = True
			testBoard[r][c + 1] = True
			testBoard[r + 1][c] = True
		case "R3":
			subScore += 5
			testBoard[r][c] = True
			testBoard[r][c + 1] = True
			testBoard[r][c + 2] = True
			testBoard[r + 1][c] = True
			testBoard[r + 2][c] = True
		case "T2":
			subScore += 3
			testBoard[r][c] = True
			testBoard[r][c + 1] = True
			testBoard[r + 1][c + 1] = True
		case "T3":
			subScore += 5
			testBoard[r][c] = True
			testBoard[r][c + 1] = True
			testBoard[r][c + 2] = True
			testBoard[r + 1][c + 2] = True
			testBoard[r + 2][c + 2] = True
		case "J2":
			subScore += 3
			testBoard[r][c + 1] = True
			testBoard[r + 1][c] = True
			testBoard[r + 1][c + 1] = True
		case "J3":
			subScore += 5
			testBoard[r][c + 2] = True
			testBoard[r + 1][c + 2] = True
			testBoard[r + 2][c] = True
			testBoard[r + 2][c + 1] = True
			testBoard[r + 2][c + 2] = True
	results = testrcCheck(testBoard)
	return results[0], subScore + results[1], tempPieces

def rcCheck():
	global score
	compRow = []
	for r in range(10):
		count = 0
		for c in range(10):
			if board[r][c]:
				count += 1
			else:
				break
		if count == 10:
			compRow.append(r)
	compCol = []
	for c in range(10):
		count = 0
		for r in range(10):
			if board[r][c]:
				count += 1
			else:
				break
		if count == 10:
			compCol.append(c)
	for r in compRow:
		for c in range(10):
			board[r][c] = False
	for c in compCol:
		for r in range(10):
			board[r][c] = False
	score += 5 * (len(compRow) + len(compCol)) * (len(compRow) + len(compCol) + 1)

def testrcCheck(inputBoard):
	testBoard = copy.deepcopy(inputBoard)
	compRow = []
	for r in range(10):
		count = 0
		for c in range(10):
			if testBoard[r][c]:
				count += 1
			else:
				break
		if count == 10:
			compRow.append(r)
	compCol = []
	for c in range(10):
		count = 0
		for r in range(10):
			if testBoard[r][c]:
				count += 1
			else:
				break
		if count == 10:
			compCol.append(c)
	for r in compRow:
		for c in range(10):
			testBoard[r][c] = False
	for c in compCol:
		for r in range(10):
			testBoard[r][c] = False
	return testBoard,5 * (len(compRow) + len(compCol)) * (len(compRow) + len(compCol) + 1)

def moveCheck(pieces,board):
	possibleMoves = []
	if len(pieces) == 0:
		return True,[]
	for piece in pieces:
		match piece:
			case "H2":
				for r in range(10):
					for c in range(9):
						if board[r][c] == False and board[r][c + 1] == False:
							possibleMoves.append(["H2",10*r+c])
			case "H3":
				for r in range(10):
					for c in range(8):
						if board[r][c] == False and board[r][c + 1] == False and board[r][c + 2] == False:
							possibleMoves.append(["H3",10*r+c])
			case "H4":
				for r in range(10):
					for c in range(7):
						if board[r][c] == False and board[r][c + 1] == False and board[r][c + 2] == False and board[r][c + 3] == False:
							possibleMoves.append(["H4",10*r+c])
			case "H5":
				for r in range(10):
					for c in range(6):
						if board[r][c] == False and board[r][c + 1] == False and board[r][c + 2] == False and board[r][c + 3] == False and board[r][c + 4] == False:
							possibleMoves.append(["H5",10*r+c])
			case "V2":
				for r in range(9):
					for c in range(10):
						if board[r][c] == False and board[r + 1][c] == False:
							possibleMoves.append(["V2",10*r+c])
			case "V3":
				for r in range(8):
					for c in range(10):
						if board[r][c] == False and board[r + 1][c] == False and board[r + 2][c] == False:
							possibleMoves.append(["V3",10*r+c])
			case "V4":
				for r in range(7):
					for c in range(10):
						if board[r][c] == False and board[r + 1][c] == False and board[r + 2][c] == False and board[r + 3][c] == False:
							possibleMoves.append(["V4",10*r+c])
			case "V5":
				for r in range(6):
					for c in range(10):
						if board[r][c] == False and board[r + 1][c] == False and board[r + 2][c] == False and board[r + 3][c] == False and board[r + 4][c] == False:
							possibleMoves.append(["V5",10*r+c])
			case "B1":
				for r in range(10):
					for c in range(10):
						if board[r][c] == False:
							possibleMoves.append(["B1",10*r+c])
			case "B2":
				for r in range(9):
					for c in range(9):
						if board[r][c] == False and board[r][c + 1] == False and board[r + 1][c] == False and board[r + 1][c + 1] == False:
							possibleMoves.append(["B2",10*r+c])
			case "B3":
				for r in range(8):
					for c in range(8):
						if board[r][c] == False and board[r][c + 1] == False and board[r][c + 2] == False and board[r + 1][c] == False and board[r + 1][c + 1] == False and board[r + 1][c + 2] == False and board[r + 2][c] == False and board[r + 2][c + 1] == False and board[r + 2][c + 2] == False:
							possibleMoves.append(["B3",10*r+c])
			case "L2":
				for r in range(9):
					for c in range(9):
						if board[r][c] == False and board[r + 1][c] == False and board[r + 1][c + 1] == False:
							possibleMoves.append(["L2",10*r+c])
			case "L3":
				for r in range(8):
					for c in range(8):
						if board[r][c] == False and board[r + 1][c] == False and board[r + 2][c] == False and board[r + 2][c + 1] == False and board[r + 2][c + 2] == False:
							possibleMoves.append(["L3",10*r+c])
			case "R2":
				for r in range(9):
					for c in range(9):
						if board[r][c] == False and board[r][c + 1] == False and board[r + 1][c] == False:
							possibleMoves.append(["R2",10*r+c])
			case "R3":
				for r in range(8):
					for c in range(8):
						if board[r][c] == False and board[r][c + 1] == False and board[r][c + 2] == False and board[r + 1][c] == False and board[r + 2][c] == False:
							possibleMoves.append(["R3",10*r+c])
			case "T2":
				for r in range(9):
					for c in range(9):
						if board[r][c] == False and board[r][c + 1] == False and board[r + 1][c + 1] == False:
							possibleMoves.append(["T2",10*r+c])
			case "T3":
				for r in range(8):
					for c in range(8):
						if board[r][c] == False and board[r][c + 1] == False and board[r][c + 2] == False and board[r + 1][c + 2] == False and board[r + 2][c + 2] == False:
							possibleMoves.append(["T3",10*r+c])
			case "J2":
				for r in range(9):
					for c in range(9):
						if board[r][c + 1] == False and board[r + 1][c] == False and board[r + 1][c + 1] == False:
							possibleMoves.append(["J2",10*r+c])
			case "J3":
				for r in range(8):
					for c in range(8):
						if board[r][c + 2] == False and board[r + 1][c + 2] == False and board[r + 2][c] == False and board[r + 2][c + 1] == False and board[r + 2][c + 2] == False:
							possibleMoves.append(["J3",10*r+c])
	if len(possibleMoves) == 0:
		return False,[]
	else:
		return True,possibleMoves

def boardWeight(sampleBoard,sampleScore,tempPieces):
	count = 0
	for r in range(10):
		for c in range(10):
			if sampleBoard[r][c] == True:
				count += 1
	totalSquares = count
	moveScore = sampleScore
	b3Check = moveCheck(["B3"],sampleBoard)[0]
	h5Check = moveCheck(["H5"],sampleBoard)[0]
	v5Check = moveCheck(["V5"],sampleBoard)[0]
	rCount = 0
	for r in range(10):
		for c in range(10):
			if sampleBoard[r][c] == True:
				rCount += 1
				break
	cCount = 0
	for c in range(10):
		for r in range(10):
			if sampleBoard[r][c] == True:
				cCount += 1
				break
	maxRCused = min(rCount,cCount)
	canPlay = moveCheck(tempPieces,sampleBoard)[0]
	
	'''extend the array'''
	for r in range(10):
		sampleBoard[r].insert(0,True)
		sampleBoard[r].append(True)
	sampleBoard.insert(0,[True,True,True,True,True,True,True,True,True,True,True,True])
	sampleBoard.append([True,True,True,True,True,True,True,True,True,True,True,True])

	surfArea = 0 
	'''build surface area algorithm as "internal surface area" algorithm'''
	gap1 = 0
	gap2 = 0
	holes = 0
	for r in range(10):
		for c in range(9):
			a = 0

while moveCheck(pieces,board)[0]:
	if len(pieces) == 0:
		generatePieces()
		continue
	print(pieces,score)
	printBoard()

	'''print("Piece:")
	piece = input()
	print("Location:")
	location = int(input())'''

	moves = moveCheck(pieces,board)[1]
	selectMove = random.choice(moves)

	print(move(selectMove[0],selectMove[1]))
	rcCheck()
print(pieces,score)
printBoard()
print("GAME OVER")
print("Score: " + str(score))