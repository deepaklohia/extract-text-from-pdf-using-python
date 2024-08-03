#JGDJSS By Deepak Lohia , Developed at www.dlohia.com
import os
import PyPDF2
import re
import pandas as pd
import numpy as np

#Change below########################START
input_file = 'C:/Users/dell/Documents/Python/PDF_to_JSON/sample2/pdf.pdf'
output_xlsx = 'C:/Users/dell/Downloads/output_text/new/output.xlsx'
#Change below########################END

output_file1 = 'pdf_content.txt'
output_file2 = 'pdf_line_content.txt'

#for filename in os.listdir(directory):
#if filename.endswith(".pdf"):
src_file = open(input_file,'rb')
pdfreader = PyPDF2.PdfReader(src_file)
num_pg = len(pdfreader.pages) 
#pdfreader.getNumPages()

print("Number of pages is:" + str(num_pg))

start_pno = 2
end_pno = num_pg-1

for pg in range(start_pno,end_pno):
    #pageob = pdfreader.getPage(pg)
    print("Extracting on page:" + str(pg))
    pageob = pdfreader.pages[pg]
    try:
        dest_file = open(output_file1,'a')
    except FileNotFoundError:
        dest_file = open(output_file1,'w')

    dest_file.write(pageob.extract_text())
    dest_file.close()

src_file.close()

out_file = open(output_file2,'w')
new_file = open(output_file1,'rb')

s = new_file.read()
strn = re.split(' No',str(s))
out_file.write('\n'.join(strn))

new_file.close()
out_file.close()

out_fl = open(output_file2,'r')

row = []

for eachline in out_fl.readlines():
    h_no = re.findall(r'\s:\s(.*?)Gender',eachline)
    gender = re.findall(r'.Gender\s:\s(.*?)Age',eachline)
    name = re.findall(r'.\dName\s:\s(.*?)\s',eachline)
    age = re.findall(r'[A-Z]*\s\s(\d\d)\s.\w',eachline)
    f_name = re.findall(r'\sName\s:\s(.*?)\s\s\d\d',eachline)
    row.append((h_no,gender,name,age,f_name))

out_fl.close()
os.remove(output_file1)
os.remove(output_file2)

pd.set_option('future.no_silent_downcasting', True)
df = pd.DataFrame(row, columns = ['House No', 'Gender', 'Name', 'Age',
                                  'Father\'s/Husband\'s Name'])

print(df.values)
for colmn in df.columns:
    df[colmn] = df[colmn].apply(lambda i: ''.join(i)) 

df.replace('', np.nan, inplace=True)
df.dropna(how = 'all', inplace=True)

writer = pd.ExcelWriter(output_xlsx)
df.to_excel(writer,'Content')

writer.close()
