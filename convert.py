import os
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt
import pyPdf
import textract
from pytesseract import image_to_string
# from PIL import Image
# from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io



# tool = pyocr.get_available_tools()[0]
# lang = tool.get_available_languages()[1]

html_list=[]
pdf_list=[]
count=0
# import subprocess
# import pdfx


def convert(fname, pages=None):
    print(fname)
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)



    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

   
    infile = file(fname, 'rb')
    # infile=open(fname,'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text 


# def getPDFContent(path):

#     content = ""

#     pdf = pyPdf.PdfFileReader(file(path, "rb"))
#     print pdf.getNumPages()

#     for i in range(0, pdf.getNumPages()):
#         f=open("xxx.txt",'a')
#         content= pdf.getPage(i).extractText() + "\n"
#         # import string
#         # c=content.split()
#         # for a in c:
#         #     f.write(" ")
#         #     f.write(a)
#         # f.write('\n')
#         # f.close()

#     return content





# root_path=r'C:\Users\user\Desktop\test_download'
root_path=r'C:/Data/test'
states=(os.listdir(root_path))
print(root_path)
for state in states:
	html_list_new=[]
	count=count+1
	# if count>1:
	# 	break
	searchin=os.listdir(os.path.join(root_path,state))
	for area in searchin:
		folders=os.listdir(os.path.join(root_path+"\\"+str(state),area))
		for index,folder in enumerate(folders):
			files=os.listdir(os.path.join(root_path+"\\"+str(state)+"\\"+str(area),folder))
			if index==1:
				for myfile in files:
					html_list.append(myfile)
			if index==2:
				for myfile in files:
					pdf_list.append(myfile)

		# print(html_list)	
		# print(pdf_list)
		for hfile in html_list:
			if hfile.endswith('.html'):
				hfilenew = hfile[:-5]
				html_list_new.append(hfilenew)
		
		# print(pdf_list)		

		for index,pfile in enumerate(pdf_list):
			if pfile.endswith('.pdf'):
				pfilenew=pfile[:-4]


			if not pfile.endswith('.pdf'):	
				print (pfile)
		
			if pfilenew not in html_list_new:
				req_image = []
				final_text = []
				count=count+1
				# thisfile = open(root_path+"\\"+str(state)+"\\statecommission\\"+"\\PDF\\"+pfile,'w')
				# print(type(thisfile))
				# content=convert(thisfile)
				path=root_path+"/"+str(state)+"/statecommission/"+"PDF/"+pfile

				#using wand and pyocr
				# image_pdf = Image(filename="./PDF_FILE_NAME", resolution=300)
				# print(image_pdf)
				# image_jpeg = image_pdf.convert('jpeg')

				# for img in image_jpeg.sequence:
				#     img_page = Image(image=img)
				#     req_image.append(img_page.make_blob('jpeg'))


				# for img in req_image: 
				#     txt = tool.image_to_string(
				#         PI.open(io.BytesIO(img)),
				#         lang=lang,
				#         builder=pyocr.builders.TextBuilder()
				#     )
				#     final_text.append(txt)  

				# for line in final_text:
				# 	content=content+line 




				# print(path)
				#using pdfminer
				# content=convert(path)
				#using textract
				content = textract.process(path,method="pdfminer")
				print(content)

				# print image_to_string(Image.open(path), lang='eng')
				thisfile = open(root_path+"\\"+str(state)+"\\statecommission\\"+"TXT\\"+pfilenew.txt,'w') 
 
				thisfile.write(content)  
				 
				thisfile.close() 


				# subprocess.call(pdfx root_path+str(state)+"\\"+"pdf\\"+hfile+".pdf" -t -o  root_path+"\\"+state+"\\"+"pdf\\"+hfile+".txt", shell=True)
				# print(state+hfile)






# print count
					




