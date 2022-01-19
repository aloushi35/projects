#Fakhreddine, Ali
from collections import namedtuple
stoc = namedtuple('stoc','date close')
def StockMarket():
    'This function reads two stock files, PFE and MRNA, it then is able to find the price on a specific date and the maxpossible profit and loss, as well as the morning and evening star trends.'
    stocks = {}
    stocks1 = {}
    stocklist = []
    stocklist1 = []
    dates = []
    while True:
        s = input('$ ').split()
        if s[0] == 'quit':
            return
        elif s[0] == 'ReadFiles':
            for entry in open(s[1],'r'):
                elist = entry.split(',')
                stocks[elist[0]] = elist[4]
                readfiles = stoc(elist[0], elist[4])
                stocklist.append(readfiles)
            for entry1 in open(s[2],'r'):
                elist1 = entry1.split(',')
                stocks1[elist1[0]] = elist1[4]
                readfiles1 = stoc(elist1[0], elist1[4])
                stocklist1.append(readfiles1)
        elif s[0] == 'PricesOnDate':
            dates = s[1].split('-')
            year = dates[0]
            month = dates[1].lstrip('0')
            day = dates[2].lstrip('0')
            date1 = month+'/'+day+'/'+year
            print('PFE:', stocks[date1], '|', 'MRNA:', stocks1[date1])
        elif s[0] == 'MaxPossible':
            sto = [item[0] for item in stocklist]
            sto1 = [item[1] for item in stocklist]

            st = [item[0] for item in stocklist1]
            st1 = [item[1] for item in stocklist1]
            
            dates1 = s[3].split('-')
            year1 = dates1[0]
            month1 = dates1[1].lstrip('0')
            day1 = dates1[2].lstrip('0')
            date2 = month1+'/'+day1+'/'+year1
            
            dates2 = s[4].split('-')
            year2 = dates2[0]
            month2 = dates2[1].lstrip('0')
            day2 = dates2[2].lstrip('0')
            date3 = month2+'/'+day2+'/'+year2


            if s[1] == 'profit':
                if s[2] == 'PFE':
                    stocksub_list = sto1[sto.index(date2):sto.index(date3)+1]
                    for i in range(0, len(stocksub_list)):
                        stocksub_list[i] = float(stocksub_list[i])
                    a = max(stocksub_list)
                    price = stocksub_list[0]
                    b = min(stocksub_list[stocksub_list.index(price):stocksub_list.index(max(stocksub_list))+1])
                    print(a-b)

                if s[2] == 'MRNA':
                    stocksub_list1 = st1[st.index(date2):st.index(date3)+1]
                    for i in range(0, len(stocksub_list1)):
                        stocksub_list1[i] = float(stocksub_list1[i])
                    a1 = max(stocksub_list1)
                    price1 = stocksub_list1[0]
                    b1 = min(stocksub_list1[stocksub_list1.index(price1):stocksub_list1.index(max(stocksub_list1))+1])
                    print(a1-b1)

            if s[1] == 'loss':
                if s[2] == 'PFE':
                    stocksub_list = sto1[sto.index(date2):sto.index(date3)+1]
                    for i in range(0, len(stocksub_list)):
                        stocksub_list[i] = float(stocksub_list[i])
                    a2 = max(stocksub_list)
                    price2 = None
                    b2 = min(stocksub_list[stocksub_list.index(max(stocksub_list)):])
                    print(a2-b2)
                    
                if s[2] == 'MRNA':
                    stocksub_list1 = st1[st.index(date2):st.index(date3)+1]
                    for i in range(0, len(stocksub_list1)):
                        stocksub_list1[i] = float(stocksub_list1[i])
                    a3 = max(stocksub_list1)
                    price3 = None
                    b3 = min(stocksub_list1[stocksub_list1.index(max(stocksub_list1)):])
                    print(a3-b3)

        elif s[0] == 'FindTrend':
            stocx = [item[0] for item in stocklist]
            stocx1 = [item[1] for item in stocklist]

            stocxx = [item[0] for item in stocklist1]
            stocxx1 = [item[1] for item in stocklist1]

            dat1 = s[2].split('-')
            year3 = dat1[0]
            month3 = dat1[1].lstrip('0')
            day3 = dat1[2].lstrip('0')
            datt2 = month3+'/'+day3+'/'+year3
            
            dat2 = s[3].split('-')
            year4 = dat2[0]
            month4 = dat2[1].lstrip('0')
            day4 = dat2[2].lstrip('0')
            datt3 = month4+'/'+day4+'/'+year4

            if s[1] == 'PFE':
                if datt2 not in stocx:
                    pass
                elif datt3 not in stocx:
                    pass
                else:
                    stock_list = stocx[stocx.index(datt2):stocx.index(datt3)+1]
                    stock_listt = stocx1[stocx.index(datt2):stocx.index(datt3)+1]
                    f = [0] * len(stock_listt)
                    for j in stock_listt:
                        if stock_listt.index(j) < 3:
                            print(stock_list[stock_listt.index(j)] + ' | ' + stock_listt[stock_listt.index(j)])
                        elif float(stock_listt[stock_listt.index(j)]) < float(stock_listt[stock_listt.index(j)-1]) and float(stock_listt[stock_listt.index(j)-1]) > float(stock_listt[stock_listt.index(j)-2]) and float(stock_listt[stock_listt.index(j)-2]) and float(stock_listt[stock_listt.index(j)-2]) > float(stock_listt[stock_listt.index(j)-3]) and 1 not in f[stock_listt.index(j)-4:stock_listt.index(j)-1]:
                            f[stock_listt.index(j)] = 1
                            print(stock_list[stock_listt.index(j)] + ' | ' + stock_listt[stock_listt.index(j)] + ' | sell')
                        elif float(stock_listt[stock_listt.index(j)]) > float(stock_listt[stock_listt.index(j)-1]) and float(stock_listt[stock_listt.index(j)-1]) < float(stock_listt[stock_listt.index(j)-2]) and float(stock_listt[stock_listt.index(j)-2]) and float(stock_listt[stock_listt.index(j)-2]) < float(stock_listt[stock_listt.index(j)-3]) and 1 not in f[stock_listt.index(j)-4:stock_listt.index(j)-1]:
                            f[stock_listt.index(j)] = 1
                            print(stock_list[stock_listt.index(j)] + ' | ' + stock_listt[stock_listt.index(j)] + ' | buy')
                        else:
                            print(stock_list[stock_listt.index(j)] + ' | ' + stock_listt[stock_listt.index(j)])
            if s[1] == 'MRNA':
                if datt2 not in stocxx:
                    pass
                elif datt3 not in stocxx:
                    pass
                else:
                    stock_list1 = stocxx[stocxx.index(datt2):stocxx.index(datt3)+1]
                    stock_listt1 = stocxx1[stocxx.index(datt2):stocxx.index(datt3)+1]
                    f1 = [0] * len(stock_listt1)
                    for m in stock_listt1:
                        if stock_listt1.index(m) < 3:
                            print(stock_list1[stock_listt1.index(m)] + ' | ' + stock_listt1[stock_listt1.index(m)])
                        elif float(stock_listt1[stock_listt1.index(m)]) < float(stock_listt1[stock_listt1.index(m)-1]) and float(stock_listt1[stock_listt1.index(m)-1]) > float(stock_listt1[stock_listt1.index(m)-2]) and float(stock_listt1[stock_listt1.index(m)-2]) and float(stock_listt1[stock_listt1.index(m)-2]) > float(stock_listt1[stock_listt1.index(m)-3]) and 1 not in f1[stock_listt1.index(m)-4:stock_listt1.index(m)-1]:
                            f1[stock_listt1.index(m)] = 1
                            print(stock_list1[stock_listt1.index(m)] + ' | ' + stock_listt1[stock_listt1.index(m)] + ' | sell')
                        elif float(stock_listt1[stock_listt1.index(m)]) > float(stock_listt1[stock_listt1.index(m)-1]) and float(stock_listt1[stock_listt1.index(m)-1]) < float(stock_listt1[stock_listt1.index(m)-2]) and float(stock_listt1[stock_listt1.index(m)-2]) and float(stock_listt1[stock_listt1.index(m)-2]) < float(stock_listt1[stock_listt1.index(m)-3]) and 1 not in f1[stock_listt1.index(m)-4:stock_listt1.index(m)-1]:
                            f1[stock_listt1.index(m)] = 1
                            print(stock_list1[stock_listt1.index(m)] + ' | ' + stock_listt1[stock_listt1.index(m)] + ' | buy')
                        else:
                            print(stock_list1[stock_listt1.index(m)] + ' | ' + stock_listt1[stock_listt1.index(m)])
