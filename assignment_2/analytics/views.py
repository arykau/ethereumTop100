from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


def getAddresses():
    addresses = []

    for i in range(1, 5):
        if (i != 1):
            URL = "https://etherscan.io/accounts/" + str(i)
            resp = requests.get(URL,
                                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36 OPR/83.0.4254.27'})
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, 'html.parser')

            result = ''

            for tr in soup.find_all('tr'):
                account = str(tr.find_all('a'))
                start = account.find(">")
                end = account.find("</a>")
                result = account[start+1:end]

                addresses.append(result)
        else:
            URL = "https://etherscan.io/accounts"
            resp = requests.get(URL,
                                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36 OPR/83.0.4254.27'})
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, 'html.parser')

            result = ''

            for tr in soup.find_all('tr'):
                account = str(tr.find_all('a'))
                if (account != "["):
                    start = account.find(">")
                    end = account.find("</a>")
                    result = account[start+1:end]
                    addresses.append(result)

    return (addresses)


def index(request):
    addresses = getAddresses()

    response1 = requests.get('https://api.etherscan.io/api?module=account&action=balancemulti&address=' +
                             str(addresses[1]) + ',' + str(addresses[2]) + ',' + str(addresses[3]) + ',' + str(addresses[4]) + ',' +
                             str(addresses[5]) + ',' + str(addresses[6]) + ',' + str(addresses[7]) + ',' + str(addresses[8]) + ',' +
                             str(addresses[9]) + ',' + str(addresses[10]) + ',' + str(addresses[11]) + ',' + str(addresses[12]) + ',' +
                             str(addresses[13]) + ',' + str(addresses[14]) + ',' + str(addresses[15]) + ',' + str(addresses[16]) + ',' +
                             str(addresses[17]) + ',' + str(addresses[18]) + ',' + str(addresses[19]) + ',' + str(addresses[20]) + ',' +
                             '&tag=latest&apikey=8UY6E6YVXBWHJFQQBVBQMXCP3J3ZACMHPB').json()

    response2 = requests.get('https://api.etherscan.io/api?module=account&action=balancemulti&address=' +
                             str(addresses[21]) + ',' + str(addresses[22]) + ',' + str(addresses[23]) + ',' + str(addresses[24]) + ',' +
                             str(addresses[25]) + ',' + str(addresses[27]) + ',' + str(addresses[28]) + ',' + str(addresses[29]) + ',' +
                             str(addresses[30]) + ',' + str(addresses[31]) + ',' + str(addresses[32]) + ',' + str(addresses[33]) + ',' +
                             str(addresses[34]) + ',' + str(addresses[35]) + ',' + str(addresses[36]) + ',' + str(addresses[37]) + ',' +
                             str(addresses[38]) + ',' + str(addresses[39]) + ',' + str(addresses[40]) + ',' + str(addresses[41]) + ',' +
                             '&tag=latest&apikey=8UY6E6YVXBWHJFQQBVBQMXCP3J3ZACMHPB').json()

    response3 = requests.get('https://api.etherscan.io/api?module=account&action=balancemulti&address=' +
                             str(addresses[42]) + ',' + str(addresses[43]) + ',' + str(addresses[44]) + ',' + str(addresses[45]) + ',' +
                             str(addresses[46]) + ',' + str(addresses[47]) + ',' + str(addresses[48]) + ',' + str(addresses[49]) + ',' +
                             str(addresses[51]) + ',' + str(addresses[53]) + ',' + str(addresses[54]) + ',' + str(addresses[55]) + ',' +
                             str(addresses[56]) + ',' + str(addresses[57]) + ',' + str(addresses[58]) + ',' + str(addresses[59]) + ',' +
                             str(addresses[60]) + ',' + str(addresses[61]) + ',' + str(addresses[62]) + ',' + str(addresses[63]) + ',' +
                             '&tag=latest&apikey=8UY6E6YVXBWHJFQQBVBQMXCP3J3ZACMHPB').json()

    response4 = requests.get('https://api.etherscan.io/api?module=account&action=balancemulti&address=' +
                             str(addresses[64]) + ',' + str(addresses[65]) + ',' + str(addresses[66]) + ',' + str(addresses[67]) + ',' +
                             str(addresses[68]) + ',' + str(addresses[69]) + ',' + str(addresses[70]) + ',' + str(addresses[71]) + ',' +
                             str(addresses[72]) + ',' + str(addresses[73]) + ',' + str(addresses[74]) + ',' + str(addresses[75]) + ',' +
                             str(addresses[76]) + ',' + str(addresses[77]) + ',' + str(addresses[79]) + ',' + str(addresses[80]) + ',' +
                             str(addresses[81]) + ',' + str(addresses[82]) + ',' + str(addresses[83]) + ',' + str(addresses[84]) + ',' +
                             '&tag=latest&apikey=8UY6E6YVXBWHJFQQBVBQMXCP3J3ZACMHPB').json()

    response5 = requests.get('https://api.etherscan.io/api?module=account&action=balancemulti&address=' +
                             str(addresses[85]) + ',' + str(addresses[86]) + ',' + str(addresses[87]) + ',' + str(addresses[88]) + ',' +
                             str(addresses[89]) + ',' + str(addresses[90]) + ',' + str(addresses[91]) + ',' + str(addresses[92]) + ',' +
                             str(addresses[93]) + ',' + str(addresses[94]) + ',' + str(addresses[95]) + ',' + str(addresses[96]) + ',' +
                             str(addresses[97]) + ',' + str(addresses[98]) + ',' + str(addresses[99]) + ',' + str(addresses[100]) + ',' +
                             str(addresses[101]) + ',' + str(addresses[102]) + ',' + str(addresses[103]) + ',' +
                             '&tag=latest&apikey=8UY6E6YVXBWHJFQQBVBQMXCP3J3ZACMHPB').json()

    dicts = response1['result'] + response2['result'] + \
        response3['result'] + response4['result'] + response5['result']

    context = {
        "dicts": dicts,
    }

    return render(request, 'analytics/index.html', context)
