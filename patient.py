from bottle import route, error ,run ,request
pat_dict = {}

@error(404)
@error(500)
def error404(error):
    return 'Nothing here, sorry'


@route('/patient/')
def patients_list():
    return "No records"

@route('/patient', method='POST')
def patient_post():
	pid  = request.POST['pid']
	name = request.POST['name']
	gender = request.POST['gender']
	age = request.POST['age']
	address = request.POST['address']
	phone = request.POST['phone']
	temp_pat =[name,gender,age,address,phone]
	pat_dict.update({pid:temp_pat})
	return '<b>Patient Created with ID {0}'.format(pid)


@route('/patient/<pid>', method='GET')
def patient_show(pid):
    return pat_dict[pid][0]+" "+pat_dict[pid][1]+" "+pat_dict[pid][2]+" "+pat_dict[pid][3]+" "+pat_dict[pid][4]
	

@route('/patient/del/<pid>', method='DELETE')
def patient_delete(pid):
    del(pat_dict[pid])
	#return "Deleted Sucessfully {0}".format(id)

@route('/patient/updateInfo/<pid>', method='PUT')
def patient_save(pid):
	 name = request.POST['name']
	 gender = request.POST['gender']
	 age = request.POST['age']
	 address = request.POST['address']
	 phone = request.POST['phone'] 
	 temp_pat =[name,gender,age,address,phone]   
 	 pat_dict.update({pid:temp_pat})

run(host='localhost', port=8080)

