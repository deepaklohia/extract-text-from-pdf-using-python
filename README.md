# Extract PDF OCR (image) data into text file #

### sample pdf ###
![sample_pdf](https://github.com/user-attachments/assets/8297b2a8-5ff2-4a6e-a8b2-760746936408)


## Method 1: using PDF2image and poppler library ##
1. Install Anaconda
2. Launch VS Via Anaconda and install libraries (as required)
conda install -c conda-forge poppler
conda install conda-forge::pdf2image
conda install conda-forge/label/cf202003::pdf2image
conda install conda-forge::pytesseract
conda install conda-forge/label/cf202003::pytesseract
conda install -c anaconda glob2 (if you are using pdf folder)

3. Download Popper from https://github.com/oschwartz10612/poppler-windows. Extract and save in a any location and update Poppler "Library\bin" path in Python Script (imageToText.py)
4. Update output(for Text) and input path (for PDF) in the Python Script.(imageToText.py )
5. Run the script via Anaconda , ensure that you have "Anaconda" as interpreter which is auto updated when we open Visual Studio via Anaconda.

### output using PDF2image and poppler###
![sample output text using PDF2Image and poppler](https://github.com/user-attachments/assets/faf7c192-96b7-4caf-8cd3-da847ce306b0)

## Method 2: using Adobe PDF Services API ##
Refer to Adobe python files attached in folder,  after downloading the adobe sdk from link below.
update your "PDF_SERVICES_CLIENT_ID" and "PDF_SERVICES_CLIENT_SECRET" in your adobe python script which will be issued as JSON after you download sdk.
https://developer.adobe.com/document-services/apis/pdf-services/
### editable text output using Adobe API ###
![editable_pdf_using_adobe_api](https://github.com/user-attachments/assets/65a41525-20d1-4a9e-8704-1272795f33a6)


### Adobe Acrobat Online PDF Tool ###
https://www.adobe.com/in/acrobat/online.html

## Final Step: PDF to JSON ##
once the PDF OCR file has been extracted,  you can run PDF to JSON Script to convert your PDF text data into JSON.
### excel output from pdf to JSON / Excel Script ###
![python to json extract using PyPDF2](https://github.com/user-attachments/assets/fc6cd693-701a-40fe-9339-b3114e9f5d58)

