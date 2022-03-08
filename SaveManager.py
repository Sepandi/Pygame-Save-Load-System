class SaveManager():
    #--Load-Save-File-in-Save-Folder
    def Load():
        LoadSave = open("SAVE","r")
        lines = LoadSave.readlines()
        level = lines[0].strip()
        return int(level)
    #--Save-File-in-Save-Folder
    def Save(level:int):
        Save = open("SAVE","w+")
        Save.writelines(str(level))
        Save.close()