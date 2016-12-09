{
	'name': 'Education Management System',
	'description': 'Enroll Managment, Attance Management, Exam Result Management, Library Management',
	'author': 'Si, Kyaw, Lin, Ye',
	'depends': ['hr'],
        'data': [
		    "views/teacher_view.xml",
                    "views/student_view.xml",
		    "views/major_view.xml",
		    "views/student_enroll_view.xml",
		    
		    "sequences/sequence_settings.xml",
		    "workflow/student_enroll_workflow.xml"
                ],
	'qweb': [],
	'application': False,
}
