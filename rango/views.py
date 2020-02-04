from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	# Construct a dictionary to pass to the template engine as its content
	# Note the key boldmessage matches to {{ boldmessage }} in the template
	context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

	# Return a rendered response to send to the client.
	# We make use of the shorcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use.
	return render(request, 'rango/index.html', context=context_dict)
	
def about(request):
	context_dict = {'boldmessage': 'The boldest message in the West'}
	return render(request, 'rango/about.html', context=context_dict)