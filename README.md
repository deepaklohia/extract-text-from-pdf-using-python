## Extract PDF OCR (image) data to text/excel file ##
## Method 1: using PDF2image library ##
'''
1. install Anaconda
2.  Launch VS Via Anaconda and install libraries (as required)
conda install -c conda-forge poppler
conda install conda-forge::pdf2image
conda install conda-forge/label/cf202003::pdf2image
conda install conda-forge::pytesseract
conda install conda-forge/label/cf202003::pytesseract
conda install -c anaconda glob2 (if you are using pdf folder)

3. Download Popper from https://github.com/oschwartz10612/poppler-windows. Extract and save in a location and update Poppler path in Python Script (imageToText.py)

4. Update output(for Text) and input path (for PDF) in the Python Script.(imageToText.py )
STEP5: Run the script , ensure that you have "Anaconda" as interpreter which is auto updated when we open Visual Studio via Anaconda.
'''
