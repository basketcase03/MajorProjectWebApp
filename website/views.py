from django.shortcuts import render
from django.http import HttpResponse
from . import depression_detection as dd


# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms
# https://docs.djangoproject.com/en/3.2/topics/forms/


def index(request):
	if request.method == 'GET':
		return render(request,'index.html',{})
	elif request.method == 'POST':
		feats_dict = {}
		feats_list = ['PFQ090', 'INQ060', 'DBQ197', 'CBD071', 'WHQ225', 'CBQ596', 
					'MCQ300C', 'MCQ160F', 'INQ150', 'DMDMARTL', 'SDMVSTRA', 'AUQ054', 
					'CBD091', 'HUQ071', 'DLQ150', 'HSAQUEX', 'HUQ010', 'INQ140', 'DLQ020', 
					'MCQ160L', 'FSD032B', 'MIALANG', 'DLQ140', 'RIDRETH1', 'DBD910']
		for feat in feats_list:
			feats_dict[feat] = request.POST.get(feat)
		dd_status = dd.get_status(feats_dict)
		return render(request,'index.html',{'sub_text':dd_status})

# if request.method=='POST':
# 	reddit_url=request.POST.get('your_name')
# 	dd__status=dd.get_status(reddit_url)
# 	return render(request,'index.html',{'sub_text':dd_status})