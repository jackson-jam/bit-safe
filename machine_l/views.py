from django.shortcuts import render
from scapy.all import *
from django.http import HttpResponse
from django.shortcuts import render, redirect


def data(request):
    callback = request.GET.get('callback')
    filterstr = "tcp and tcp port 80"  # arp就是arp包，此处使用tcp协议进行抓包
    # ip src 39.156.66.18 and tcp and tcp port 80 or ip src 111.30.185.60 and tcp and tcp port 80
    # 开始捕获数据包，指定网络接口和回调函数
    sniff(prn=packet_callback, filter=filterstr, count=0)


# Create your views here.
def packet_callback(packet):
    # print(packet.show())
    # if packet['Ether'].payload:#arp包
    #     print (packet['Ether'].src)
    #     print (packet['Ether'].dst)
    #     print (packet['Ether'].type)
    #
    # if packet['ARP'].payload:
    #     print (packet['ARP'].psrc)
    #     print (packet['ARP'].pdst)
    #     print (packet['ARP'].hwsrc)
    #     print (packet['ARP'].hwdst)
    # if packet['TCP'].payload:
    #     print(packet['TCP'].sport)
    #     print(packet['TCP'].dport)
    # time.sleep(2)
    data= packet['TCP']
    return HttpResponse(data)
