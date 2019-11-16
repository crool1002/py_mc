import xml.etree.ElementTree as ET
from  xml.etree.ElementTree import *

def getTimeStr(str):
    intTime = int(str)/1000
    mm, ss = divmod(intTime, 60)
    hh, mm = divmod(mm, 60)
    return "%02d:%02d:%02d" % (hh, mm, ss)

tree = ET.parse('16112019_end.xml')
root = tree.getroot()

# все данные
print('Expertise Data:')
print(root)
listtag = {}
for elem in root:
    FileName = elem.find('FileName')
    ELEM = elem.findall('ELEM')
    listtag[FileName.text] =[]
    for EL in ELEM:
        id = EL.find('ID')
        StartTime = EL.find('StartTime')
        PlanStartTime = EL.find('PlanStartTime')
        SmplRealSize = EL.find('SmplRealSize')
        if int(SmplRealSize.text)>=0:
            FONO_INFO = EL.find('FONO_INFO')
            #print(FileName.tag, FileName.text)
            if iselement(EL.find('FONO_INFO')):
                FONO_STRING_INFO = FONO_INFO.find('FONO_STRING_INFO')
                FONO_STRING_INFO_NAME = FONO_STRING_INFO.find('Name')
                if iselement(FONO_STRING_INFO.find('Category')):
                    FONO_STRING_INFO_Category = FONO_STRING_INFO.find('Category')
                    listtag[FileName.text] += [(id.tag,id.text)]
                    listtag[FileName.text] += [(StartTime.tag, getTimeStr(StartTime.text))]
                    listtag[FileName.text] += [(SmplRealSize.tag, getTimeStr(SmplRealSize.text))]
                    listtag[FileName.text] += [(FONO_STRING_INFO_NAME.tag, FONO_STRING_INFO_NAME.text)]
                    listtag[FileName.text] += [(FONO_STRING_INFO_Category.tag, FONO_STRING_INFO_Category.text)]
                else:
                    listtag[FileName.text] += [(id.tag,id.text)]
                    listtag[FileName.text] += [(StartTime.tag, getTimeStr(StartTime.text))]
                    listtag[FileName.text] += [(SmplRealSize.tag, getTimeStr(SmplRealSize.text))]
                    listtag[FileName.text] += [(FONO_STRING_INFO_NAME.tag, FONO_STRING_INFO_NAME.text)]
                    listtag[FileName.text] += [('Category', '')]
                if iselement(FONO_INFO.find('FileName')):
                    listtag[FileName.text] += [(FONO_INFO.find('FileName').tag, FONO_INFO.find('FileName').text)]


for i,k in listtag.items():
    print(i)
    for tag,text in k:
        print('    ',tag,text)

