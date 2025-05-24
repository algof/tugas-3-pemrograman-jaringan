import json
import logging
import shlex

from file_interface import FileInterface

"""
* class FileProtocol bertugas untuk memproses 
data yang masuk, dan menerjemahkannya apakah sesuai dengan
protokol/aturan yang dibuat

* data yang masuk dari client adalah dalam bentuk bytes yang 
pada akhirnya akan diproses dalam bentuk string

* class FileProtocol akan memproses data yang masuk dalam bentuk
string
"""

class FileProtocol:
    def __init__(self):
        self.file = FileInterface()
    def proses_string(self,string_datamasuk=''):
        logging.warning(f"string diproses: {string_datamasuk}")

        c = string_datamasuk.split()
        print(len(c))

        try:
            if len(c) == 1:
                c_request = c[0]
                cl = self.file.list()
            elif len(c) == 2:
                c_request = c[0]
                params = c[1]
                logging.warning(params)
                if c_request == "GET":
                    cl = self.file.get([params])
                elif c_request == "DELETE":
                    cl = self.file.delete([params])
            elif len(c) == 3:
                filename = c[1]
                params = ''.join(c[2:])
                cl = self.file.upload([filename, params])
            return json.dumps(cl)
        except Exception:
            return json.dumps(dict(status='ERROR',data='request tidak dikenali'))


if __name__=='__main__':
    #contoh pemakaian
    fp = FileProtocol()
    # content = fp.proses_string("LIST")
    content = fp.proses_string("GET pokijan.jpg")
    # content = fp.proses_string("DELETE donalbebek_1.jpg")
    # print(content)
    data = json.loads(content)
    # print(data)
    # print(data['data_file'])
    content_2 = fp.proses_string(f"UPLOAD copypokijan_2.jpg {data['data_file']}")
    print(content_2)
    # print(f"UPLOAD copypokijan_1.jpg {data}")
    # isi_file = "'" + data['data_file'] + "'"
    # print(f"UPLOAD copypokijan_1.jpg {isi_file}")
    # print(fp.proses_string("GET pokijan.jpg"))
    # fp.proses_string(f"UPLOAD copypokijan_1.jpg {isi_file}")
    # print(f"UPLOAD copypokijan_1.jpg {data['data_file']}")