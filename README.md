patient
=======
import requests
posting data:
r=requests.post('http://localhost:8080/patient',data={"pid":"2","name":"avinash","gender":"M","age":"20","address":"bng","phone":"22222"})

getting data:
r=requests.get('http://localhost:8080/patient/2')
>>> r.text
u'avinash M 20 bng 22222'

deleting data:
r=requests.delete('http://localhost:8080/patient/del/2')
r=requests.get('http://localhost:8080/patient/2')
>>> r.text
>>>u " nothing here sorry"


updating data:

r=requests.put('http://localhost:8080/patient/updateInfo/2',data={"name":"avinash","gender":"M","age":"20","address":"bng","phone":"2ds"})
r=requests.get('http://localhost:8080/patient/2')
>>> r.text
u'avinash M 20 bng 2ds'

