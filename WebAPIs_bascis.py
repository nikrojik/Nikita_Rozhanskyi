import dropbox

class Repos:
    def __init__(self, token):
        self.tok = token
    def uploadFile(self, file_from, file_to):
        f = open(file_from, 'rb')
        f = f.read()
        dbx = dropbox.Dropbox(self.tok)
        if file_from != '' and file_to != '':
            dbx.files_upload(f, file_to)
            print("Uploaded!")
        else:
            print("Something gone wrong...")

    def deleteFile(self, path):
        dbx = dropbox.Dropbox(self.tok)
        dbx.files_delete_v2(path)
        print("Deleted!")

    def getMetaData(self, path):
        dbx = dropbox.Dropbox(self.tok)
        res = dbx.files_get_metadata(path)
        print(res)

if __name__ == '__main__':
    tok = input("Token:")
    user = Repos(tok)
    ft = input("Folder:")
    ff = input("Upload file:")
    ft = '/' + ft + '/' + ff
    user.uploadFile(ff, ft)
    user.getMetaData(ft)
    user.deleteFile(ft)
    
