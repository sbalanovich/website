from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import SimpleTemplateResponse
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
import sklearn
import numpy as np
import scipy
import json
import pickle

def index(request):
	template = loader.get_template('visualization/index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

@csrf_exempt
def test_ajax(request):
    if request.is_ajax():
    	title = request.POST['title']
        title = "If the Big Bang happened 13.7 Billion years ago, how is the edge of the observable universe 16 Billion light years away? Did the universe expand faster than the speed of light?"
        m, b = (2, 5)
        try:
        	with open('visualization/clf.pickle', 'rb') as handle:
        		tup = pickle.load(handle)
        except Exception, e:
        	print str(e)
        clf, vect = tup
        m = 1727.23857077
        b = -409.438149837
        def predict(title):
        	x = clf.predict_proba(vect.transform([title]))[0][1]
        	y = m*x + b
        	return y
        prediction = predict(title)
    	return HttpResponse(json.dumps([title, title]))

'''
def predict(request):
    if request.method == 'POST' or request.is_ajax():
        title = request.POST['title']
        import scikit
        import numpy as np
        import scipy
        title = "If the Big Bang happened 13.7 Billion years ago, how is the edge of the observable universe 16 Billion light years away? Did the universe expand faster than the speed of light?"
        m, b = (2, 5)
        with open('filename.pickle', 'rb') as handle:
        	b = pickle.load(handle)
        clf, vect = b
        m = 1727.23857077
        b = -409.438149837
        def predict(title):
        	x = clf.predict_proba(vect.transform([title]))[0][1]
        	y = m*x + b
        	return y
        prediction = predict(title)
        template = loader.get_template('visualization/index.html')
        context = RequestContext(request, {"prediction": "haha"})
        return HttpResponse(template.render(context))

	template = loader.get_template('visualization/index.html')
	context = RequestContext(request, {"prediction": "lmao"})
	return HttpResponse(template.render(context))
	#return HttpResponse(json.dumps({'prediction': prediction})) #tried without the json. Doesn't work either


# Create your views here.
'''