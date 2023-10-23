def drawRectangle():
	print("#####")
	print("#####")
	print("#####")
	print("#####")
	print("#####")

def drawTriangle():
	print("-----#----")
	print("----##----")
	print("---###---")
	print("--####--")
	print("-#####-")
	print("######")
	
def drawUpsideDownTri():
	print("######")
	print("-#####-")
	print("--####--")
	print("---###---")
	print("----##----")
	print("-----#----")

def drawTRU():
	drawTriangle()
	drawRectangle()
	drawUpsideDownTri()
	
def drawTRUp(p):
	for i in range(0, p):
		drawTRU()

drawTRUp(3)