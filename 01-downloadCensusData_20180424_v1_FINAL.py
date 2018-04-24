## program: 01-downloadCensusData_20180424_v1_FINAL.py
## task:        download and unzips Decennial Census 2000, 2010, and ACS 2012 5 Year Estimates
## version:     first draft
## project:     seg
## author:      kate willyard \ april 24, 2018
## notes:       this downloads the files for Dr. Keith's health project

## SET DIRECTORY AND DOWNLOAD TOOLS
dc00Path = "E:/seg/dc00"
dc10Path = "E:/seg/dc10"
acs12Path = "E:/seg/acs12"
from ftplib import FTP
import os, zipfile

## SET SEGMENTS TO DOWNLOAD FOR DC 2000 SF1, DC 2000 SF3, DC 2010 SF1, & ACS
dc00sf1List = ["001", "003", "005", "010"]
dc00sf3List = ["001", "003", "006", "013", "014", "015", "016", "027", "030", "052", "053", "054"]
dc10sf1List = ["003", "005", "012"]
acsList = ["0005", "0037", "0043", "0047", "0048", "0049", "0058", "0075"]
print "Finished Setting Directories"

## DOWNLOAD DC 2000 SF1 Data
print "STARTED 2000 Decennial Census Summary File 1 Data Downloads"
os.chdir(dc00Path)
ftp = FTP("ftp2.census.gov")
ftp.login()
ftp.cwd("census_2000/datasets/Summary_File_1/0Final_National")
fiList = ftp.nlst()
for fi in fiList:
        for seg in dc00sf1List:
                if fi[4:7] == seg:
                        fh = open (fi, "wb")
                        ftp.retrbinary("RETR " + fi, fh.write)
                        fh.close()
                        fh = open(fi, "rb")
                        zp = zipfile.ZipFile(fh)
                        for fiName in zp.namelist():
                                        zp.extract(fiName, ".")
                        fh.close()
                        os.remove(fi)
                        printStatement = "Downloaded file: " + fi
                        print printStatement
        if fi[2:5] == "geo":
                fh = open (fi, "wb")
                ftp.retrbinary("RETR " + fi, fh.write)
                fh.close()
                fh = open(fi, "rb")
                zp = zipfile.ZipFile(fh)
                for fiName in zp.namelist():
                        zp.extract(fiName, ".")
                fh.close()
                os.remove(fi)
                printStatement = "Downloaded file: " + fi
                print printStatement
ftp.quit()
print "COMPLETED Download of all 2000 Decennial Census Summary File 1 Data"

## DOWNLOAD DC 2000 SF3 Data
print "STARTED 2000 Decennial Census Summary File 3 Data Downloads"
ftp = FTP("ftp2.census.gov")
ftp.login()
ftp.cwd("census_2000/datasets/Summary_File_3/0_National")
fiList = ftp.nlst()
for fi in fiList:
        for seg in dc00sf3List:
                if fi[4:7] == seg:
                        fh = open (fi, "wb")
                        ftp.retrbinary("RETR " + fi, fh.write)
                        fh.close()
                        fh = open(fi, "rb")
                        zp = zipfile.ZipFile(fh)
                        for fiName in zp.namelist():
                                        zp.extract(fiName, ".")
                        fh.close()
                        os.remove(fi)
                        printStatement = "Downloaded file: " + fiName
                        print printStatement
if fi[2:5] == "geo":
        fh = open (fi, "wb")
        ftp.retrbinary("RETR " + fi, fh.write)
        fh.close()
        fh = open(fi, "rb")
        zp = zipfile.ZipFile(fh)
        for fiName in zp.namelist():
                zp.extract(fiName, ".")
        fh.close()
        os.remove(fi)
        printStatement = "Downloaded file: " + fiName
        print printStatement
ftp.quit()
print "COMPLETED Download of all 2000 Decennial Census Summary File 3 Data"

## DOWNLOAD DC 2010 SF1 Data
stList = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District_of_Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New_Hampshire", "New_Jersey", "New_Mexico", "New_York", "North_Carolina", "North_Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto_Rico", "Rhode_Island", "South_Carolina", "South_Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West_Virginia", "Wisconsin", "Wyoming"]
print "STARTED 2010 Decennial Census Summary File 1 Data Downloads"
os.chdir(dc10Path)
ftp = FTP("ftp2.census.gov")
ftp.login()
ftp.cwd("census_2010/04-Summary_File_1")
for st in stList:

        ftp.cwd(st)
        fiList = ftp.nlst()
        for fi in fiList:
                if fi[2:6] == "2010":
                        fh = open (fi, "wb")
                        ftp.retrbinary("RETR " + fi, fh.write)
                        fh.close()
                        fh = open(fi, "rb")
                        zp = zipfile.ZipFile(fh)
                        for fiName in zp.namelist():
                                        zp.extract(fiName, ".")
                        fh.close()
                        os.remove(fi)
                        printStatement = "Downloaded file: " + fiName
                        print printStatement
        printStatement = "Downloaded all 2010 Decennial Census Summary File 1 files for state: " + st
        print printStatement
        ftp.cwd("../")
ftp.quit()
print "COMPLETED Download of all 2010 Decennial Census Summary File 1 Data"

## DOWNLOAD ACS 2008-2012 Data
stList = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "DistrictOfColumbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "NewHampshire", "NewJersey", "NewMexico", "NewYork", "NorthCarolina", "NorthDakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "PuertoRico", "RhodeIsland", "SouthCarolina", "SouthDakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "WestVirginia", "Wisconsin", "Wyoming"]
print "STARTED 2008-2012 American Community Survey Data Downloads"
os.chdir(acs12Path)
ftp = FTP("ftp2.census.gov")
ftp.login()
ftp.cwd("acs2012_5yr/summaryfile/2008-2012_ACSSF_By_State_By_Sequence_Table_Subset")
for st in stList:
        ftp.cwd(st)
        ftp.cwd("Tracts_Block_Groups_Only")
        fiList = ftp.nlst()
        for fi in fiList:
                for seg in acsList:
                        if fi[7:11] == seg:
                                fh = open (fi, "wb")
                                ftp.retrbinary("RETR " + fi, fh.write)
                                fh.close()
                                fh = open(fi, "rb")
                                zp = zipfile.ZipFile(fh)
                                for fiName in zp.namelist():
                                                zp.extract(fiName, ".")
                                fh.close()
                                os.remove(fi)
                                printStatement = "Downloaded file: " + fi
                                print printStatement
                if fi[0:5] == "g2012":
                        fh = open (fi, "wb")
                        ftp.retrbinary("RETR " + fi, fh.write)
                        fh.close()
                        printStatement = "Downloaded file: " + fi
                        print printStatement
        printStatement = "Downloaded all 2008-2012 American Community Survey files for state: " + st
        print printStatement
        ftp.cwd("../")
        ftp.cwd("../")
ftp.quit()
print "COMPLETED Download of all 2008-2012 American Community Survey Data"
//
//


