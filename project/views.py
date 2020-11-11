from django.shortcuts import render
from project.models import Kr
from project.models import Krchartdata
from project.models import Clusteringkr
from project.models import ClusteringkrInfo
from datetime import datetime,timedelta
from django_pandas.io import read_frame
import FinanceDataReader as fdr
import pandas as pd
import numpy as np


# Create your views here.
def home(request):
    
    return render(request, 'home.html')


def fund(request):
    
    return render(request, 'fund.html')


def local (request):

    # ticker_list = Kr.objects.values_list('name', flat=True).distinct() #flat =True - tuple -> list
    ticker_list = ClusteringkrInfo.objects.all().filter(구분='국내').values_list('name', flat = True)
    selected = request.GET.get('etfkr')
    if selected == None:
        selected = 'KODEX 200'
        ticker_exclude = ticker_list.exclude(name=selected)
    else :
        ticker_exclude = ticker_list.exclude(name=selected)
    # print(selected)
    data = []
    date = []

    query = Kr.objects.filter(name=selected).order_by('-date')[:60]

    for i in query:
        date.append(str(i.date).split(' ')[0])
        data.append(i.close)

    date.reverse()
    data.reverse()
    data[:] = [(x / data[0] -1) *100 for x in data]
    
    qs = Krchartdata.objects.all()
    number_of_hischart = 5
    chart_df = read_frame (qs)
    chart_df = chart_df.drop(columns ='index')
    hisdata = {}
    hisdate = {}
    
    bardata_ = chart_df[chart_df.name.isin(['{0}_after'.format(selected)])].drop(columns ='name').values.flatten().tolist()
    bardata = [] 
    
    
    for val in bardata_: 
        if val != None : 
            bardata.append(val) 
    bardata[:] = [round(float(x)*100,2) for x in bardata]
    for i in range(number_of_hischart):
        #data
        hisdata['data{}'.format(i)] = chart_df[chart_df.name.isin(['{0}_{1}'.format(selected,i)])].drop(columns ='name').values.flatten().tolist()
        hisdata['data{}'.format(i)][:] = [round(float(x)*100,2) for x in hisdata['data{}'.format(i)]]
        #date
        hisdate['date{}'.format(i)] = chart_df[chart_df.name.isin(['{0}_{1}_date'.format(selected,i)])].drop(columns ='name').values.flatten().tolist()
        
        

    
    
    input_etf = request.GET.get('etfkr')
    if input_etf == None:
        input_etf = 'KODEX 200'
    
    #tickerlist 22개로 확장해야함
    total_ticker_list = ClusteringkrInfo.objects.all().values_list('name', flat = True)
    qs = Kr.objects.filter(name__in=total_ticker_list).all()
    
    etf_df = read_frame(qs)
    etf_df['date'] = etf_df['date'].dt.date
    etf_df = etf_df.rename(columns={'name':'etf'})
    df= pd.pivot_table(etf_df, values='change', index=['date'],
                        columns=['etf'], aggfunc='mean')
    df = df.dropna()
    # Corr Matrix
    corr_df = df.corr()


        
    corr = corr_df.loc[:,corr_df.columns==input_etf]
    high_corr = corr.sort_values(input_etf, ascending=False)[1:6]
    high_corr = round(high_corr,2)
    high_corr_list = high_corr.index.tolist()
    high_corr_values = high_corr.values.flatten().tolist()
    

    low_corr = corr.sort_values(input_etf)[:5]
    low_corr = round(low_corr,2)
    low_corr_list = low_corr.index.tolist()
    low_corr_values = low_corr.values.flatten().tolist()
    
    #종목코드
    code_df = fdr.EtfListing('KR')
    high_code = []
    low_code = []
    
    high_etf = high_corr.index.values.tolist()
    for i in high_etf:
        high_code.append(code_df[code_df.Name.isin([i])].Symbol.values[0])
        
    low_etf = low_corr.index.values.tolist()
    for i in low_etf:
        low_code.append(code_df[code_df.Name.isin([i])].Symbol.values[0])

    return render (request, 'local.html', {'data': data, 'date':date, 'selected':selected, 'ticker_exclude':ticker_exclude,
                                                'hisdata':hisdata, 'hisdate':hisdate, 'bardata':bardata,
                                            'high_corr':[high_corr_list,high_corr_values], 'low_corr': [low_corr_list,low_corr_values],
                                            'high_code':high_code, 'low_code':low_code, })

 
def international(request):

    # ticker_list = Kr.objects.values_list('name', flat=True).distinct() #flat =True - tuple -> list
    ticker_list = ClusteringkrInfo.objects.all().filter(구분='해외').values_list('name', flat = True)
    selected = request.GET.get('etfkr')
    if selected == None:
        selected = 'TIGER 미국나스닥100'
        ticker_exclude = ticker_list.exclude(name=selected)
    else :
        ticker_exclude = ticker_list.exclude(name=selected)
    # print(selected)
    data = []
    date = []

    query = Kr.objects.filter(name=selected).order_by('-date')[:60]

    for i in query:
        date.append(str(i.date).split(' ')[0])
        data.append(i.close)

    date.reverse()
    data.reverse()
    data[:] = [(x / data[0] -1) *100 for x in data]
    
    qs = Krchartdata.objects.all()
    number_of_hischart = 5
    chart_df = read_frame (qs)
    chart_df = chart_df.drop(columns ='index')
    hisdata = {}
    hisdate = {}
    
    bardata_ = chart_df[chart_df.name.isin(['{0}_after'.format(selected)])].drop(columns ='name').values.flatten().tolist()
    bardata = [] 
    
    
    for val in bardata_: 
        if val != None : 
            bardata.append(val) 
    bardata[:] = [round(float(x)*100,2) for x in bardata]
    for i in range(number_of_hischart):
        #data
        hisdata['data{}'.format(i)] = chart_df[chart_df.name.isin(['{0}_{1}'.format(selected,i)])].drop(columns ='name').values.flatten().tolist()
        hisdata['data{}'.format(i)][:] = [round(float(x)*100,2) for x in hisdata['data{}'.format(i)]]
        #date
        hisdate['date{}'.format(i)] = chart_df[chart_df.name.isin(['{0}_{1}_date'.format(selected,i)])].drop(columns ='name').values.flatten().tolist()
        
        

    
    
    input_etf = request.GET.get('etfkr')
    if input_etf == None:
        input_etf = 'TIGER 미국나스닥100'

    total_ticker_list = ClusteringkrInfo.objects.all().values_list('name', flat = True)
    qs = Kr.objects.filter(name__in=total_ticker_list).all()
    etf_df = read_frame(qs)
    etf_df['date'] = etf_df['date'].dt.date
    etf_df = etf_df.rename(columns={'name':'etf'})
    df= pd.pivot_table(etf_df, values='change', index=['date'],
                        columns=['etf'], aggfunc='mean')
    df = df.dropna()
    # Corr Matrix
    corr_df = df.corr()


        
    corr = corr_df.loc[:,corr_df.columns==input_etf]
    high_corr = corr.sort_values(input_etf, ascending=False)[1:6]
    high_corr = round(high_corr,2)
    high_corr_list = high_corr.index.tolist()
    high_corr_values = high_corr.values.flatten().tolist()
    
    low_corr = corr.sort_values(input_etf)[:5]
    low_corr = round(low_corr,2)
    low_corr_list = low_corr.index.tolist()
    low_corr_values = low_corr.values.flatten().tolist()
    
    #종목코드
    code_df = fdr.EtfListing('KR')
    high_code = []
    low_code = []
    
    high_etf = high_corr.index.values.tolist()
    for i in high_etf:
        high_code.append(code_df[code_df.Name.isin([i])].Symbol.values[0])
        
    low_etf = low_corr.index.values.tolist()
    for i in low_etf:
        low_code.append(code_df[code_df.Name.isin([i])].Symbol.values[0])

    return render (request, 'international.html', {'data': data, 'date':date, 'selected':selected, 'ticker_exclude':ticker_exclude,
                                                'hisdata':hisdata, 'hisdate':hisdate, 'bardata':bardata,
                                            'high_corr':[high_corr_list,high_corr_values], 'low_corr': [low_corr_list,low_corr_values],
                                            'high_code':high_code, 'low_code':low_code, })
 
def resource(request):
    # ticker_list = Kr.objects.values_list('name', flat=True).distinct() #flat =True - tuple -> list
    ticker_list = ClusteringkrInfo.objects.all().filter(구분='상품').values_list('name', flat = True)
    selected = request.GET.get('etfkr')
    if selected == None:
        selected = 'KODEX 골드선물(H)'
        ticker_exclude = ticker_list.exclude(name=selected)
    else :
        ticker_exclude = ticker_list.exclude(name=selected)
    # print(selected)
    data = []
    date = []

    query = Kr.objects.filter(name=selected).order_by('-date')[:60]

    for i in query:
        date.append(str(i.date).split(' ')[0])
        data.append(i.close)

    date.reverse()
    data.reverse()
    data[:] = [(x / data[0] -1) *100 for x in data]
    
    qs = Krchartdata.objects.all()
    number_of_hischart = 5
    chart_df = read_frame (qs)
    chart_df = chart_df.drop(columns ='index')
    hisdata = {}
    hisdate = {}
    
    bardata_ = chart_df[chart_df.name.isin(['{0}_after'.format(selected)])].drop(columns ='name').values.flatten().tolist()
    bardata = [] 
    
    
    for val in bardata_: 
        if val != None : 
            bardata.append(val) 
    bardata[:] = [round(float(x)*100,2) for x in bardata]
    for i in range(number_of_hischart):
        #data
        hisdata['data{}'.format(i)] = chart_df[chart_df.name.isin(['{0}_{1}'.format(selected,i)])].drop(columns ='name').values.flatten().tolist()
        hisdata['data{}'.format(i)][:] = [round(float(x)*100,2) for x in hisdata['data{}'.format(i)]]
        #date
        hisdate['date{}'.format(i)] = chart_df[chart_df.name.isin(['{0}_{1}_date'.format(selected,i)])].drop(columns ='name').values.flatten().tolist()
        
        

    
    
    input_etf = request.GET.get('etfkr')
    if input_etf == None:
        input_etf = 'KODEX 골드선물(H)' 

    total_ticker_list = ClusteringkrInfo.objects.all().values_list('name', flat = True)
    qs = Kr.objects.filter(name__in=total_ticker_list).all()
    etf_df = read_frame(qs)
    etf_df['date'] = etf_df['date'].dt.date
    etf_df = etf_df.rename(columns={'name':'etf'})
    df= pd.pivot_table(etf_df, values='change', index=['date'],
                        columns=['etf'], aggfunc='mean')
    df = df.dropna()
    # Corr Matrix
    corr_df = df.corr()

        
    corr = corr_df.loc[:,corr_df.columns==input_etf]
    
    high_corr = corr.sort_values(input_etf, ascending=False)[1:6]
    high_corr = round(high_corr,2)
    high_corr_list = high_corr.index.tolist()
    high_corr_values = high_corr.values.flatten().tolist()

    
    low_corr = corr.sort_values(input_etf)[:5]
    low_corr = round(low_corr,2)
    low_corr_list = low_corr.index.tolist()
    low_corr_values = low_corr.values.flatten().tolist()

    #종목코드
    code_df = fdr.EtfListing('KR')
    high_code = []
    low_code = []
    
    high_etf = high_corr.index.values.tolist()
    for i in high_etf:
        high_code.append(code_df[code_df.Name.isin([i])].Symbol.values[0])
        
    low_etf = low_corr.index.values.tolist()
    for i in low_etf:
        low_code.append(code_df[code_df.Name.isin([i])].Symbol.values[0])

    return render (request, 'resource.html', {'data': data, 'date':date, 'selected':selected, 'ticker_exclude':ticker_exclude,
                                                'hisdata':hisdata, 'hisdate':hisdate, 'bardata':bardata,
                                            'high_corr':[high_corr_list,high_corr_values], 'low_corr': [low_corr_list,low_corr_values],
                                            'high_code':high_code, 'low_code':low_code, })

def trends(request):
    ticker_list = ClusteringkrInfo.objects.all().values_list('name', flat = True)
    ticker_exclude = ticker_list.exclude(name='KODEX 200')
    
    
    input_etf = request.GET.get('etfkr')
    if input_etf == None:
        input_etf = 'KODEX 200'

    qs = Kr.objects.filter(name__in=ticker_list).all()
    
    etf_df = read_frame(qs)
    etf_df['date'] = etf_df['date'].dt.date
    etf_df = etf_df.rename(columns={'name':'etf'})
    df= pd.pivot_table(etf_df, values='change', index=['date'],
                        columns=['etf'], aggfunc='mean')
    df = df.dropna()
    # Corr Matrix
    corr_df = df.corr()


        
    corr = corr_df.loc[:,corr_df.columns==input_etf]
    high_corr = corr.sort_values(input_etf, ascending=False)[1:6]
    high_corr = round(high_corr,2)
    high_corr_list = high_corr.index.tolist()
    high_corr_values = high_corr.values.flatten().tolist()
    
    low_corr = corr.sort_values(input_etf)[:5]
    low_corr = round(low_corr,2)
    low_corr_list = low_corr.index.tolist()
    low_corr_values = low_corr.values.flatten().tolist()
    return render(request, 'trends.html',{'ticker_exclude': ticker_exclude, 'input_etf': input_etf, 'high_corr':[high_corr_list,high_corr_values], 'low_corr': [low_corr_list,low_corr_values]}) 

def test(request):
    # ticker_list = Kr.objects.values_list('name', flat=True).distinct() #flat =True - tuple -> list
    ticker_list = ClusteringkrInfo.objects.all().filter(구분='국내').values_list('name', flat = True)
    ticker_exclude = ticker_list.exclude(name='KODEX 200')
    selected = request.GET.get('etfkr')
    if selected == None:
        selected = 'KODEX 200'
    # print(selected)
    data = []
    date = []

    query = Kr.objects.filter(name=selected).order_by('-date')[:60]

    for i in query:
        date.append(str(i.date).split(' ')[0])
        data.append(i.close)

    date.reverse()
    data.reverse()
    data[:] = [(x / data[0] -1) *100 for x in data]
    
    qs = Krchartdata.objects.all()
    number_of_hischart = 5
    chart_df = read_frame (qs)
    chart_df = chart_df.drop(columns ='index')
    hisdata = {}
    hisdate = {}
    
    bardata_ = chart_df[chart_df.name.isin(['{0}_after'.format(selected)])].drop(columns ='name').values.flatten().tolist()
    bardata = [] 
    
    
    for val in bardata_: 
        if val != None : 
            bardata.append(val) 
    bardata[:] = [round(float(x)*100,2) for x in bardata]
    for i in range(number_of_hischart):
        #data
        hisdata['data{}'.format(i)] = chart_df[chart_df.name.isin(['{0}_{1}'.format(selected,i)])].drop(columns ='name').values.flatten().tolist()
        hisdata['data{}'.format(i)][:] = [round(float(x)*100,2) for x in hisdata['data{}'.format(i)]]
        #date
        hisdate['date{}'.format(i)] = chart_df[chart_df.name.isin(['{0}_{1}_date'.format(selected,i)])].drop(columns ='name').values.flatten().tolist()
        
        

    
    
    input_etf = request.GET.get('etfkr')
    if input_etf == None:
        input_etf = 'KODEX 200'

    qs = Kr.objects.filter(name__in=ticker_list).all()
    
    etf_df = read_frame(qs)
    etf_df['date'] = etf_df['date'].dt.date
    etf_df = etf_df.rename(columns={'name':'etf'})
    df= pd.pivot_table(etf_df, values='change', index=['date'],
                        columns=['etf'], aggfunc='mean')
    df = df.dropna()
    # Corr Matrix
    corr_df = df.corr()


        
    corr = corr_df.loc[:,corr_df.columns==input_etf]
    high_corr = corr.sort_values(input_etf, ascending=False)[1:6]
    high_corr = round(high_corr,2)
    high_corr_list = high_corr.index.tolist()
    high_corr_values = high_corr.values.flatten().tolist()
    
    low_corr = corr.sort_values(input_etf)[:5]
    low_corr = round(low_corr,2)
    low_corr_list = low_corr.index.tolist()
    low_corr_values = low_corr.values.flatten().tolist()
    

    # print('bardata:\n',bardata)
    return render (request, 'test.html', {'data': data, 'date':date, 'selected':selected, 'ticker_exclude':ticker_exclude,
                                                'hisdata':hisdata, 'hisdate':hisdate, 'bardata':bardata,
                                           'input_etf': input_etf, 'high_corr':[high_corr_list,high_corr_values], 'low_corr': [low_corr_list,low_corr_values]})

def bench(request,selected_ticker):
    seleted = selected_ticker
    qs = ClusteringkrInfo.objects.filter(name= selected_ticker)
    
    name = [i.name for i in qs]
    cc = [i.구분 for i in qs]
    detail_cc = [i.구분상세 for i in qs]
    basic_index = [i.기초지수 for i in qs]
    description = [i.설명 for i in qs]
    # print(type(name)) #return -> list


    return render(request, 'bench.html',{'name': name[0], 'cc': cc[0], 'detail_cc': detail_cc[0] ,'basic_index': basic_index[0], 'description': description[0], })