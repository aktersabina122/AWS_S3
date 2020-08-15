
import webbrowser
import boto3

class HtmlDocument:
    def __init__(self):
        self.message = """<html><head></head> <body><h1>Hello World!</h1>"""
        self.save1 = HtmlManager()

    def save(self):
        self.to_save = self.message
        self.save1.writehtml(self.to_save)

class HtmlManager:
    def __init__(self):
        pass

    def writehtml(self, message):
        samplehtml = open('sabina.html','w')
        samplehtml.write(message)
        samplehtml.close()
        webbrowser.open_new_tab('sabina.html')
    

class AWSManager:
    def __init__(self):
        self.s3_client = boto3.client('s3')

    def save_to_s3(self):
        self.s3_client.upload_file('sabina.html','lmtd-class','sabina.html')

    def load_from_s3(self):
        self.s3_client.download_file('lmtd-class', 'test.html', 'filefroms3.html')
    

s1 = HtmlDocument()
s1.save()

s2 = AWSManager()
s2.save_to_s3()
s2.load_from_s3()


