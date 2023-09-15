# Dicom tool

## Description

Extract images from Dicom container.


This example based on python flask template extract images from Dicom container.
Library pydicom is used to analyze Dicom file and extract images.
Dicom contener should be upload by Web GUI. Uploaded file is opened by Pydicom.
All embedded images are written to the "./tmp" directory as PNG.


Known issues:
1.Extension of the Dicom file (.dcm) has to be lowercase



## URLs:

https://pydicom.github.io
https://flask.palletsprojects.com/en/2.3.x/



