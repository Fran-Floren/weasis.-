import urllib
import subprocess
import urllib.parse
global a

def consulta(x,y,z):
    url = urllib.parse.quote(f'$dicom:rs --url  "http://{x}:8080/dcm4chee-arc/aets/DCM4CHEE/rs" -r "{z}={y}"', safe='') #Constuyo la url
    print(url)
    subprocess.run(f'start weasis://{url}', shell=True) #Encodeo la URL

a = str(input('Ip:')) #IP 

cond = str(input('¿patient o study?'))


if cond == 'patient':
    q = 'patientID'
    p = str(input(''))
    consulta(a,p,q)
elif cond == 'study':
    w = 'studyUID'
    s = str(input(''))
    consulta(a,s,w)
else:
    a = str(input('Ip:')) #IP 
    cond = str(input('¿patient o study?'))