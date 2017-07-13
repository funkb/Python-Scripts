
__author__ = 'Brandon Funk'

import os, sys
import subprocess

from tkinter.filedialog import askopenfilename, askdirectory

resourcesPath = "C:/Program Files/Allegorithmic/Substance Designer/5/resources/packages"
sbsCooker = "C:/Program Files/Allegorithmic/Substance Designer/5/bin64/sbscooker.exe"   # cooks sbs to sbsar materials
sbsRender = "C:/Program Files/Allegorithmic/Substance Designer/5/bin64/sbsrender.exe"  # renders output images from sbs/sbsar

###CHECK FOR REAL NUMBERS BETWEEN 1 and 2 ####
while True:
    try:
        cmd = int(input("1:Cooker   2:Render   3:SBS2Maps   >"))

        if cmd > 0 or cmd < 4:
            break
        else:
            print ("Number must be between one and three")
            raise Exception
    except:
        print ("Please enter a real number")
    
    


###COOKER (SBS TO SBSAR) ####
def runCooker():
    print ("Choose SBS Files")
    inputPath = askopenfilename(initialdir = "C:/", title = "Choose .SBS file", filetypes = (("Substance Material", "*.sbs"),("all files", "*")))
    outputPath = askdirectory()

    commandArgs = (' --input "{0}" '.format(inputPath)+
                   '--output-path "{0}"'.format(outputPath))
    subprocess.call( '"{0}" {1}'.format(sbsCooker, commandArgs) )
    os.startfile(outputPath)

###RENDER  (SBSAR TO PNG) ####
def runRender():
    inputPath = askopenfilename(initialdir = "C:/", title = "Choose .SBSAR file", filetypes = (("Substance Material Archive", "*.sbsar"),("all files", "*")))
    outputPath = askdirectory()

    commandArgs = (' render --inputs "{0}" '.format(inputPath)+
                   '--output-path "{0}"'.format(outputPath))
    subprocess.call( '"{0}" {1}'.format(sbsRender, commandArgs) )
    os.startfile(outputPath)

    
###SINGLE SBS TO TEXTURE MAPS#####
def sbsToMaps():
    inputPath = askopenfilename(initialdir = "C:/", title = "Choose .SBS file", filetypes = (("Substance Material", "*.sbs"),("all files", "*")))
    outputPath = askdirectory()

    commandArgs = (' --input "{0}" '.format(inputPath)+
                   '--output-path "{0}"'.format(outputPath))
    subprocess.call( '"{0}" {1}'.format(sbsCooker, commandArgs) )

    print (inputPath.rsplit('r"/"'))
    
    inputPath = outputPath + inputPath.rsplit('r"/"')[1]

    
    
    commandArgs = (' render --inputs "{0}" '.format(inputPath)+
                   '--output-path "{0}"'.format(outputPath))
    subprocess.call( '"{0}" {1}'.format(sbsRender, commandArgs) )

if cmd is 1:
    runCooker()
elif cmd is 2:
    runRender()
elif cmd is 3:
    sbsToMaps()
