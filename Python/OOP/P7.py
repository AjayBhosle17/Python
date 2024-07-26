class Folder:
    FolderName='Python'
    def __init__(self):
        print("Folder Constructor")
        self.Fold='OuterClass'

    class Files:
        FilesType='Text'
        def __init__(self):
            print("Files Constructor")
            self.File='Innerclass'

        def dispFiles(self):
            print(self.File)
            print(self.FilesType)
    def dispFolder(self):
        print(self.Fold)
        print(self.FolderName)
FoldObj=Folder()
FoldObj.dispFolder()

FilesObj=FoldObj.Files()
FilesObj.dispFiles()

print(FoldObj.__class__)
print(FilesObj.__class__)

