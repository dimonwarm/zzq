 # -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from query.models import Result
@csrf_exempt
def query(request):
	return render_to_response('query.html')

@csrf_exempt
def res(request):
	sorry="对不起,您此次未中签"
	congratulation="恭喜您，已中签!"
	inputval=request.POST.get('input','')
	c=Result.objects.filter(num=inputval)	
	if inputval.isdigit():
		if len(inputval)==13:		
			if len(c)==0:
				return render_to_response('res.html',{'output1':sorry,'got':0})
			else:
				c=Result.objects.filter(num=inputval)
				return render_to_response('res.html',{'output1':congratulation,'obj':c,'got':1})		
		else:
			sorry="请输入正确的信息"
			return  render_to_response('res.html',{'output1':sorry,'got':0})
	else:
		if len(inputval)==0:
			sorry="请输入正确的信息"
			return  render_to_response('res.html',{'output1':sorry,'got':0})
		else:
			c=Result.objects.filter(name=inputval)
			if len(c)==1:
				c=Result.objects.filter(name=inputval)
				return render_to_response('res.html',{'output1':congratulation,'obj':c,'got':1})
			elif len(c)==0:
				return render_to_response('res.html',{'output1':sorry,'got':0})
			else:
				return render_to_response('res.html',{'output1':congratulation,'obj':c,'got':1,'same':len(c),'samenum':1})



















