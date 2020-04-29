#!/usr/bin/python3

# Yoni Carver
# 718.704.8555

# as of 6.12.2017

#%%
# Importing libraries

# scale
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.pdf import PageObject
# job code & product info
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

#%%
# name of cwd (current working directory)
# change cwd to network drive N: in cmd type -- cd /d N:

import os
cwd = os.getcwd()
foldername = cwd.rsplit('\\',1)
print(foldername)
print('CWD: %s\n' %cwd)

os.chdir('..')

#%%

# BATCH RUN THE CODE ON EVERY FILE IN THE CWD

# list of all PDFs in current working directory

directory = os.getcwd()                                                         # change this if you want to use another folder
files = [i for i in os.listdir(directory) if os.path.splitext(i)[1] == '.pdf']  # populate list with all .pdf files in directory

#dict = {}
#count = 0
#print('List of all pdf files in directory:')
#for f in files:
#  dict[count] = f
#  print(count, dict[count])
#  count += 1
for idx, item in enumerate(files):
    print(idx, item)

#%%
# DEFINE FUNCTION CUTSHEET

def cutsheet(filename):
  print('\nCURRENTLY WORKING ON FILE: %s\n' % filename)                         # file indication

  # SCALE pages -----------------------------------------------------------------------------------------------------------------

    # Take a pdf file as input
  inputpdf = filename
#  inputpdf = input('name of input PDF: ') + '.pdf'                             # DEBUGGING purposes only
#  inputpdf = 'iondatasheet.pdf'                                                # DEBUGGING purposes only

  cutsheetfile = open(inputpdf, "rb")
  input1 = PdfFileReader(cutsheetfile)                                          # open the file you wish to work on
  scale_output = PdfFileWriter()                                                # assign a name to write the final scaled PDF

  #-----------------------------------------------------------------------------------------------------------------------------#

  pages = []                                                                    # empty list to be populated later
  for sheet in range(input1.getNumPages()):                                     # for item in # of pages in input1...
    pages.append(input1.getPage(sheet))                                         # add that page to the empty list "pages"

  count = 0                                                                     # start count at page 1
  for page in pages:                                                            # for each item in list "pages" (which is populated with input1)
    page.scaleTo(width=527, height=682)                                         # scale each page -- default: 527 682
    scale_output.addPage(page)                                                  # add each scaled page to page
    print("SCALING: Page %d is done" %  (count+1))                              # page completion indicator
    count += 1                                                                  # go to next page
  print("Scaling complete\n")                                                   # total completion indicator

  # Make and write to an output document
  scaleoutpdf = open('scaleout.pdf','wb')                                       # open scale output PDF file to be written to (default name: scaleout.pdf)
  with scaleoutpdf as s:                                                        # with scaleout.pdf as name: s...
    scale_output.write(s)                                                       # write scaled pages to output PDF


  #%%
  # MERGE pages

  #headerfile = open("./src/Cut Sheet Template v2017v01.pdf",'rb')               # open header PDF - in src folder
  headerfile = open("./src/Cut_Sheet_Template_v2020v02.pdf",'rb')               # open header PDF - in src folder
  header = PdfFileReader(headerfile)                                            # open header PDF
  header_page = header.getPage(0)                                               # get page 1 of header PDF (only has 1 page)

  scalefile = open("scaleout.pdf",'rb')                                         # open scale output PDF
  scale_reader = PdfFileReader(scalefile)                                       # open scaled page (see above code)
  scale_page = scale_reader.getPage(0)                                          # get page 1 of scaled PDF

  blankfile = open("./src/blank.pdf",'rb')                                      # open blank file (used as template for 8.5" x 11") - in src folder
  blank_reader = PdfFileReader(blankfile)                                       # open blank page as template for 8.5 x 11
  blank_page = blank_reader.getPage(0)                                          # get page 1 of template page (onlt has 1 page)
  writer = PdfFileWriter()                                                      # assign writer to write PDF

  pages1 = []                                                                   # empty list to be populated later
  for i in range(scale_reader.getNumPages()):                                   # for item in # of pages in scale_reader...
    pages1.append(scale_reader.getPage(i))                                      # add that page to the empty list "pages1"

  count = 0                                                                     # start count at page 1
  for page in pages1:                                                           # for each page in list "pages1" (which is populated with scale_reader)
    scale_page = scale_reader.getPage(count)                                    # iterate through pages using "count"
    complete_page = PageObject.createBlankPage(None, blank_page.mediaBox.getWidth(), blank_page.mediaBox.getHeight())   # get size of final PDF (to be 8.5" x 11")
    complete_page.mergeScaledTranslatedPage(scale_page, 1.05, 30, -5)           # merge, scale, and translate page -- default: 1.05 30 -5
    complete_page.mergePage(header_page)                                        # merge page with header
    #complete_page.mergeTranslatedPage(header_page, 0, 712)
    writer.addPage(complete_page)                                               # write completed page to PDF
    print("MERGING: Page %d is done" %  (count+1))                              # completion indicator
    count += 1                                                                  # go to next page
  print("Merging complete\n")                                                   # total completion indicator

  mergeoutpdf = open('mergeout.pdf','wb')                                       # open merge output PDF file to be written to (default name: mergeout.pdf)
  with mergeoutpdf as m:                                                        # with mergeout.pdf as name: m...
    writer.write(m)                                                             # write final PDF


  #%%
  # Job code & product info

  #jobcode = 'ABC123 - Debugging Code'                                           # DEBUGGING purposes only
  #productname = 'this text should be caps'                                      # DEBUGGING purposes only

  jobcode = os.path.basename(os.getcwd())
  productname = item.replace('.pdf','')

  c = canvas.Canvas('jobinfo.pdf', pagesize = letter)                           # specify output PDF name & set paper size to letter
  width, height = letter                                                        # set the width & height to letter (w = 8.5", h = 11")

  c.setFontSize(18)                                                             # set font size of job name
  c.drawCentredString(width / 2.0, 750, jobcode)                                # specify job name (to be centered on top page)

  c.setFontSize(14)                                                             # set font size for product name
  c.drawCentredString(width / 2.0, 730, productname)                            # specify product name (to be centered on top of page)

  c.save()                                                                      # save the file


  #%%
  # WATERMARK the job name and product name on top of merged & scaled

  output = PdfFileWriter()

  basewfile = open('mergeout.pdf', 'rb')                                        # open the base PDF file (to be watermarked)
  ipdf = PdfFileReader(basewfile, 'rb')                                         # read the base PDF file you want to watermark

  watermarkfile = open('jobinfo.pdf', 'rb')                                     # opem the file you are using as a watermark (created with jobcode & productname)
  wpdf = PdfFileReader(watermarkfile, 'rb')                                     # read the file you are using as a watermark
  watermark = wpdf.getPage(0)                                                   # get page 1 of watermark (watermark file should only have 1 page)

  count = 0                                                                     # start count at page 1
  for i in range(ipdf.getNumPages()):                                           # for each page in the number of pages in watermarking PDF...
    page = ipdf.getPage(i)                                                      # get page number
    page.mergePage(watermark)                                                   # watermark the page
    output.addPage(page)                                                        # add watermarked page to output file
    print("WATERMARKING: Page %d is done" %  (count+1))                         # page completion indicator
    count += 1                                                                  # go to next page
  print("Watermarking complete")                                                # total completion indicator

  finalname = productname + ' Cut Sheet.pdf'                                    # final name of cut sheet PDF will be productname + ' Cut Sheet.pdf'
  nameoutpdf = open(finalname,'wb')                                             # open final cut sheet PDF to be written to
  with nameoutpdf as n:                                                         # with (productname) Cut Sheet.pdf as name: n...
   output.write(n)                                                              # write output file
   n.close()                                                                    # close the file
  #%%
  # Close all files

  cutsheetfile.close()                                                          # close file
  headerfile.close()                                                            # close file
  scalefile.close()                                                             # close file
  blankfile.close()                                                             # close file
  basewfile.close()                                                             # close file
  watermarkfile.close()                                                         # close file
  basewfile.close()                                                             # close file

  count += 1
# END OF cutsheet(filename)
#%%

for item in files:                                                              # for each file in the list of files in the cwd...
  cutsheet(item)                                                                # run the code to turn that file into an LDG Cut Sheet (this batch runs the code on each file)

#%%
# Delete irrelevant files (files for internal use only)

os.remove('scaleout.pdf')                                                       # delete scaleout.pdf because it is not needed
os.remove('mergeout.pdf')                                                       # delete mergeout.pdf because it is not needed
os.remove('jobinfo.pdf')                                                        # delete jobinfo.pdf because it is not needed

