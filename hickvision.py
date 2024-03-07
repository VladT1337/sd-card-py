import requests
SAVE_FILE = True

FILE_TEST = '/home/vtolubayev/Downloads/py_test.mp4' #change the path


PLAYBACK_URI = 'http:///ISAPI/Streaming/tracks/103/?starttime=20231031T055637Z&amp;endtime=20231031T055637Z&amp;name=ch01_0001002350000000002_00@ch01_20231031135637_PIRALARM_00&amp;size=119253'
MODIFIED_PLAYBACK_URI = 'rtps://46.210.89.130/Streaming/tracks/103/?starttime=20231031T055637Z&amp;endtime=20231031T055637Z&amp;name=ch01_0001002350000000002_00@ch01_20231031135637_PIRALARM_00&amp;size=119253'
#PLAYBACK_URI_RTSP = 'rtsp://192.168.225.2/Streaming/tracks/101/?starttime=20240222T115305Z&amp;endtime=20240222T120152Z&amp;name=ch01_00010000000000000&amp;size=37576192'
PLAYBACK_URI_RTSP = 'rtsp://192.168.225.2/Streaming/tracks/101/?starttime=20240224T045601Z&amp;endtime=20240224T064645Z&amp;name=ch01_00010000055000000&amp;size=264730624'
#XML_QUERIES

CONTENT_MGMT_SEARCH_XML ='''<?xml version="1.0" encoding="utf-8"?>
<CMSearchDescription>
 <searchID>C777384AD-66AO-0001-E7C2-1551F04F9085</searchID>   
'''

DOWNLOAD_REQUEST_XML= f'''<downloadRequest version="1.0" xmlns="http://www.isapi.org/ver20/XMLSchema">
 <playbackURI>
   {PLAYBACK_URI_RTSP}
 </playbackURI>
</downloadRequest>
'''



#rtsp://admin:Avihayapo@46.210.89.130:8554/main

username = 'admin'
password = 'Avihayapo'
host = '46.210.89.130'
port = '8554'
port2 = '8080'
protocol = 'http'

AUX_INFO_CHANNELS = 'ͬ/ISAPI/AUXInfo/attributes/Channels' #exceeded max retries rate
CONTENT_MGMT_CAPABILITIES = '/ISAPI/ContentMgmt/capabilities' #works - remote downloading pf file is supported
CONTENT_MGMT_SEARCH_PROFILE = '/ISAPI/ContentMgmt/search/profile'# <p>Can't find process for service:/ISAPI/ContentMgmt/search/profile</p>
CONTETNT_MGMT_RECORD_TRACKS = '/ISAPI/ContentMgmt/record/tracks'#returns XML with track ids
CONTENT_MGMT_SEARCH = '/ISAPI/ContentMgmt/search' #worked with tackId=103 POST
CONTENT_MGMT_STORAFE_HDD_SEARCH = '/ISAPI/ContentMgmt/storage/hdd' #should be used for hdd defs not for downloads
CONTENT_MGMT_DOWNLOAD = '/ISAPI/ContentMgmt/download'#called by post got invalid operation response for jpeg, succeeded with rtsp. 
CONTENT_MGMT_DOWNLOAD_CAPABILITIES = '/ISAPI/ContentMgmt/download/capabilities'

track_ids =[101, 103]
url = f'{protocol}://{host}{CONTENT_MGMT_DOWNLOAD}'
auth_param = requests.auth.HTTPDigestAuth(username,password)

print(auth_param)

#print('http://46.210.89.130')

#res_chk = requests.get('http://46.210.89.130')
#print(res_chk)
#print(res_chk.text)

print(url)
#print(DOWNLOAD_REQUEST_XML)

#res = requests.get(url, auth=auth_param)

res = requests.post(url,auth=auth_param, data=DOWNLOAD_REQUEST_XML)


print(res)
#print(res.content)

if(SAVE_FILE):
  file = open(FILE_TEST, 'wb+')
  file.write(res.content)
  file.close()