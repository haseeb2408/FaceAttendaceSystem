import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
"databaseURL" : "https://facerecognitionrealtime-b1c32-default-rtdb.firebaseio.com/"
})


ref=db.reference('Students')

data={
	
	"221":
	{
		"name" : "Hamza M",
		"major" : "AI Computer Vision",
		"starting_year" : 2020,
		"total_attendance" : 6,
		"standing" : "G",
		"year" : 4,
		"last_attendance_time" : "2022-12-11 00:12:23"
	},
	
	
	"223":
	{
		"name" : "Haseeb Ahmed",
		"major" : "AI",
		"starting_year" : 2020,
		"total_attendance" : 3,
		"standing" : "VG",
		"year" : 4,
		"last_attendance_time" : "2022-12-11 00:12:23"
	} ,
	
	"225":
	{
		"name" : "Saif Umer",
		"major" : "Mern Stack",
		"starting_year" : 2020,
		"total_attendance" : 8,
		"standing" : "W",
		"year" : 4,
		"last_attendance_time" : "2022-12-11 00:12:23"
	}
	
	
}

for key, value in data.items():
	ref.child(key).set(value)
