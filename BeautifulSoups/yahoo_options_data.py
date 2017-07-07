import json
import sys
import re
import urllib
from bs4 import BeautifulSoup

def contractAsJson(filename):
    jsonQuoteData = "[]"

    inputFile = open(filename)

    soup = BeautifulSoup(inputFile, "html.parser")
    TICKER = str(soup.title).split(" ")[0].split(">")[1].upper()

    # Code to get info from Tables
    tables = soup.findChildren('table')
    dataTables = soup.findAll('table', {'class':'yfnc_datamodoutline1'})
    rows = list()
    for row in dataTables[0].findAll("tr"):
        rows.append(row)

    parsedTable = list()
    rowNum = 0
    #parse Call data
    for i in range(2,len(rows)):
        cols = rows[i].findChildren('td')
        d = {}

        d["Strike"] = str(cols[0].findAll(text=True)).split("'")[1]
        d["Last"] = str(cols[2].findAll(text=True)).split("'")[1]
        d["Change"] = " " + str(cols[3].findAll(text=True)).split("'")[3]
        d["Bid"] = str(cols[4].findAll(text=True)).split("'")[1]
        d["Ask"] = str(cols[5].findAll(text=True)).split("'")[1]
        d["Vol"] = str(cols[6].findAll(text=True)).split("'")[1]
        d["Open"] = str(cols[7].findAll(text=True)).split("'")[1]
        openStrNoComma = str(d["Open"]).replace(",","")
        d["Open Int"] = int(openStrNoComma)
        d["Row Number"] = rowNum
        d["Type"] = "C"
        symbolAndDate = str(cols[1].findAll(text=True)).split("'")[1]
        startOfDate = symbolAndDate.find("14")
        d["Date"] = symbolAndDate[startOfDate:startOfDate+6]
        d["Symbol"] = symbolAndDate[0:startOfDate]

        parsedTable.append(d)
        rowNum = rowNum+1


    beginingOfP = len(rows)-2
    rows = list()

    for row in dataTables[1].findAll("tr"):
        rows.append(row)
    #parse puts data
    for i in range(2,len(rows)):
        cols = rows[i].findChildren('td')
        d = {}
        d["Strike"] = str(cols[0].findAll(text=True)).split("'")[1]
        d["Last"] = str(cols[2].findAll(text=True)).split("'")[1]
        # change = str(cols[3].findAll(text=True)).split("'")[3]
        # if(change.find(".")==1): d["Change"] = " "+str(change)
        # else: d["Change"] = change
        d["Change"] = " " + str(cols[3].findAll(text=True)).split("'")[3]
        d["Bid"] = str(cols[4].findAll(text=True)).split("'")[1]
        d["Ask"] = str(cols[5].findAll(text=True)).split("'")[1]
        d["Vol"] = str(cols[6].findAll(text=True)).split("'")[1]
        d["Open"] = str(cols[7].findAll(text=True)).split("'")[1]
        openStrNoComma = str(d["Open"]).replace(",","")
        d["Open Int"] = int(openStrNoComma)
        d["Row Number"] = rowNum
        d["Type"] = "P"
        symbolAndDate = str(cols[1].findAll(text=True)).split("'")[1]
        startOfDate = symbolAndDate.find("14")
        d["Date"] = symbolAndDate[startOfDate:startOfDate+6]
        d["Symbol"] = symbolAndDate[0:startOfDate]
        parsedTable.append(d)
        rowNum = rowNum+1


    # Sort fuction
    lessOpenInt = lambda x,y: 1 if x["Open Int"] < y["Open Int"] else -1 if x["Open Int"] > y["Open Int"] else lessRow(x,y)
    lessRow = lambda x,y: -1 if x["Row Number"] < y["Row Number"] else 1

    #sort table and remove extra keys that aren't required after sort
    hiToLowTable = sorted(parsedTable, lessOpenInt)
    optionQuotes = []
    for i in range(len(hiToLowTable)):
        d = {}
        d = hiToLowTable[i]
        d.pop("Open Int")
        d.pop("Row Number")
        optionQuotes.append(d)


    # Code to get current price
    currInfo = soup.find('span', {'class':'time_rtq_ticker'})
    currData = str(currInfo.findChildren())
    currPrice = float(re.sub('[^0-9.]','',currData.split(">")[1]))


    # Code to get dateUrls
    URLs = soup.find_all(href = re.compile("m="))
    dateUrls = list()
    for i in range(len(URLs)):
        s = str(URLs[i])
        start = s.find("/q/op?s=")
        if start!=-1:
            s = s[start:]
            dateUrls.append("http://finance.yahoo.com" + s[0:s.find('"')])
        else:
            start = s.find("/q/os?s=")
            if start!=-1:
                s = s[start:]
                dateUrls.append("http://finance.yahoo.com" + s[0:s.find('"')])


    # gather results
    results = {}
    results["currPrice"] = currPrice
    results["dateUrls"] = dateUrls
    results["optionQuotes"] = optionQuotes
    jsonQuoteData = json.dumps(results, sort_keys=True, indent=4, separators=(',', ': '))

    return jsonQuoteData
