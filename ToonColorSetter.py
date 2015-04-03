import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText 
from direct.gui.DirectGui import *
from panda3d.core import *

rgbaValues[4]

bk_text = "The Toon color setter. ;)"
textObject = OnscreenText(text = bk_text, pos = (0.95,-0.95), 
scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)

def setText(textEntered):
	textObject.setText(textEntered)

def clearText():
	b.enterText('')
	
b = DirectEntry(text = "" ,scale=.05,command=setText,
initialText="Type a float value between 0.0 and 1.0", numLines = 2,focus=1,focusInCommand=clearText)