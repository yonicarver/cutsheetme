# cutsheetme
A Python script/executable for turning PDFs into a cutsheets

---

### Running cutsheetme
- Place any PDFs you wish to turn into cutsheets in the main directory
- Rename the main directory (default: "cutsheetme") to the job number/title
  - The filename will be the name of the  product in the cutsheet
- Navigate to the "./src" directory
- Double-click on the "RUNME_vXX.exe" (where XX is the current version number)
- Let the program run (you will see the status of the program on the screen in a command prompt window)
- When the program is complete, you will see your cutsheets in the root directory ("Cut Sheet" is appended to the original title of the PDF)
<br></br>

- Alternatively, you can run this script via Python by double-clicking the "RUNME_vXX.py" file (where XX is the current version number)

---

### Downloading cutsheetme
- Download this repository by downloading the zip file from: [https://github.com/yonicarver/cutsheetme](https://github.com/yonicarver/cutsheetme "cutsheetme Repository")

![alt text](https://github.com/yonicarver/cutsheetme/blob/master/readme_files/images/download_repository_arrow.PNG "download_repository_arrow.PNG")

- Extract the contents of repository and place the folder "custsheetme" in a location of your choosing
<br></br>
#### Downloading cutsheetme (.exe)
- You're done! Simply double click on the "RUNME_vXX.exe" file to run the program
<br></br>
#### Downloading cutsheetme (.py)
- You will need to install all required Python libraries. Open a command prompt window, navigate to the "src" directory of this repository (e.g. ```cd Documents\cutsheetme\src```), and type:
```
pip install -r requirements.txt
```
- In order to be able to run the script by double clicking on "RUNME_vXX.py", you will need to select Python as the default file opener for \*.py files. (Note: If you prefer to run the script via a command prompt window, run the script by typing ```python RUNME_vXX.py```

![alt text](https://github.com/yonicarver/cutsheetme/blob/master/readme_files/images/open_with_arrow.PNG "open_with_arrow.PNG")

---

### How to Install Python (Windows 7)

- Download Python 3.7.5 from: [https://www.python.org/downloads/release/python-375/](https://www.python.org/downloads/release/python-375/ "Python 3.7.5 Download")

- Scroll down to the "Files" section and click "Windows x86-64 executable installer"

- Run the installer

- Click the checkbox next to "Add Python 3.7 to PATH" and click "Install Now"

![alt text](https://github.com/yonicarver/cutsheetme/blob/master/readme_files/images/python_installer_arrows.PNG "python_installer_arrows.PNG")

- After the installation is complete, open a Command Prompt window and verify that Python 3.7.5 was installed correctly by typing: ```python```. Alternatively, you can check which version of Python is installed by typing: ```python --version``` <br />


If your Python installation is correct, you should see something like:
```
Python 3.7.5 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```


