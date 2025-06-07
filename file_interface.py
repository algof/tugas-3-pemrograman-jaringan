import os
import json
import base64
from glob import glob


class FileInterface:
    def __init__(self):
        os.chdir('files/')

    def list(self,params=[]):
        try:
            filelist = glob('*.*')
            return dict(status='OK',data=filelist)
        except Exception as e:
            return dict(status='ERROR',data=str(e))

    def get(self,params=[]):
        try:
            filename = params[0]
            if (filename == ''):
                return None
            fp = open(f"{filename}",'rb')
            isifile = base64.b64encode(fp.read()).decode()
            return dict(status='OK',data_namafile=filename,data_file=isifile)
        except Exception as e:
            return dict(status='ERROR',data=str(e))
    
    def delete(self,params=[]):
        try:
            filename = params[0]
            if (filename == ''):
                return None
            os.remove(filename)
            return dict(status='OK', message=f"{filename} has been deleted")
        except Exception as e:
            return dict(status='ERROR',data=str(e))

    def upload(self,params=[]):
        try:
            filelist = glob('*.*')
            filename = params[0]

            if filename in filelist:
                return dict(status='ERROR',data=f"File '{filename}' already exists")
            
            content = params[1]
            file_bytes = base64.b64decode(content)

            extension = filename.split('.')[-1].lower()
            text_extensions = ['txt', 'csv', 'json', 'html', 'xml']
            if extension in text_extensions:
                file_str = file_bytes.decode('utf-8')
                with open(filename, 'w', encoding='utf-8') as file_pointer:
                    file_pointer.write(file_str)
            else:
                with open(filename, 'wb') as file_pointer:
                    file_pointer.write(file_bytes)
                    
            return dict(status='OK',message=f"{filename} has been uploaded")
        except Exception as e:
            return dict(status='ERROR',data=str(e))

    def get_dummy_base64(self,params=[]):
        try:
            filename = params[0]
            if (filename == ''):
                return None
            fp = open(f"{filename}",'rb')
            isifile = base64.b64encode(fp.read()).decode()
            return isifile
        except Exception as e:
            return dict(status='ERROR',data=str(e))

if __name__=='__main__':
    f = FileInterface()
    print(f.delete(["donalbebek_1.jpg"]))
    content_base64 = f.get_dummy_base64(['donalbebek.jpg'])
    print(f.upload(["donalbebek_4.jpg", content_base64]))