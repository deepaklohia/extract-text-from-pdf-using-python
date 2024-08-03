# Extract PDF OCR (image) data into text file #
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


## Method 2: using Adobe PDF Services API ##
Refer to Adobe python files attached in folder,  after downloading the adobe sdk from link below.
update your "PDF_SERVICES_CLIENT_ID" and "PDF_SERVICES_CLIENT_SECRET" in your adobe python script which will be issued as JSON after you download sdk.
https://developer.adobe.com/document-services/apis/pdf-services/

### Adobe Acrobat Online PDF Tool ###
https://www.adobe.com/in/acrobat/online.html

## Final Step: PDF to JSON ##
once the PDF OCR file has been extracted,  you can run PDF to JSON Script to convert your PDF text data into JSON.
