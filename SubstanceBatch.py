import os, sys, glob, subprocess
from tkinter.filedialog import *


class SubstanceBaker:    


    ##INIT##
    def __init__ (self):
        self.currentDir = os.getcwd()
        self.sbsCooker = str(self.currentDir) + "\sbscooker.exe"
        self.sbsRender = str(self.currentDir) + "\sbsrender.exe"
        self.importFolder = ""
        self.exportFolder = ""
        self.root = Tk()
        self.root.withdraw()
        self.GUI()
        
    ##USER SELECTS FOLDER TO IMPORT THE FILES FROM##
    def openImport(self, event):
        self.importFolder = askdirectory()

    ##USER SELECTS FOLDER TO EXPORT THE FILES TO##
    def openExport(self, event):
        self.exportFolder = askdirectory()

    ##CHECKS IF USER HAS SELECTED THE FOLDERS##  ##CRUCIAL TO CONTINUE##
    def checkFolders(self):
        if self.importFolder is "" or self.exportFolder is "":
            print ("You have not selected one of your folders.")
            print (str(self.importFolder) + ">Import")##DEBUG
            print (str(self.exportFolder) + ">Export")##DEBUG
            return False
        else:
            return True

    ##COOK .SBS TO .SBSAR##
    def cook(self, event):

        ##ONLY PROCEED IF FOLDERS HAVE BEEN SELECTED
        if self.checkFolders() is True:
            ##COOK EVERY .SBS FILE IN IMPORT_FOLDER
            for file in glob.glob(os.path.join(self.importFolder, '*.sbs')):

                ##REQUIRED ARGS FOR BATCH BAKING
                commandArgs = (' --input "{0}" '.format(file)+
                       '--output-path "{0}"'.format(self.exportFolder))
            

                ##CALL THE PROCESS IN CMD
                process = subprocess.call( '"{0}" {1}'.format(self.sbsCooker, commandArgs) )
                print (str(process) + "   " + file)##DEBUG

            ##NAVIGATE TO EXPORT_FOLDER
            os.startfile(self.exportFolder)


    ##RENDER .SBSAR TO TEXTURE MAPS##
    def render(self, event):

        ##ONLY PROCEED IF FOLDERS HAVE BEEN SELECTED
        if self.checkFolders() is True:

            ##RENDER EVERY .SBSAR IN IMPORT_FOLDER
            for file in glob.glob(os.path.join(self.importFolder, '*.sbsar')):

                ##REQUIRED ARGS FOR BATCH BAKING
                commandArgs = (' render --inputs "{0}" '.format(file)+
                           '--output-path "{0}"'.format(self.exportFolder))

                ##CALL PROCESS IN CMD
                process = subprocess.call( '"{0}" {1}'.format(self.sbsRender, commandArgs) )

                print (str(process) + "   " + file)##DEBUG

            ##NAVIGATE TO EXPORT_FOLDER
            os.startfile(self.exportFolder)

    ##MAIN GUI SYSTEM## 
    def GUI(self):

        MainWindow = Tk()
        MainWindow.title("Substance Baker")
        MainWindow.geometry("300x300")

        mainMenu = Menu(MainWindow)
        MainWindow.config(menu = mainMenu)
        filemenu = Menu(mainMenu)
        mainMenu.add_cascade(label = "File", menu = filemenu)
        filemenu.add_command(label = "Exit", command = MainWindow.quit)

        importWidget = Button(MainWindow, text = "Import Folder")
        importWidget.pack(padx = 5, pady = 5)
        importWidget.bind('<Button-1>', self.openImport)
        
        exportWidget = Button(MainWindow, text = "Export Folder")
        exportWidget.pack(padx = 5, pady = 5)
        exportWidget.bind('<Button-1>',self.openExport)

        runCooker = Button(MainWindow, text = ".sbs to .sbsar")
        runCooker.pack(padx = 5, pady = 5)
        runCooker.bind('<Button-1>', self.cook)

        runRender = Button(MainWindow, text= ".sbsar to textures")
        runRender.pack(padx = 5, pady = 5)
        runRender.bind('<Button-1>', self.render)

        mainloop()

  
sb = SubstanceBaker()
