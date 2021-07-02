import rpy2
from rpy2 import robjects
from rpy2.robjects import Formula, Environment
from rpy2.robjects.vectors import IntVector, FloatVector, DataFrame
from rpy2.robjects.lib import grid
from rpy2.robjects.packages import importr, data
from rpy2.rinterface import RRuntimeError
from rpy2.robjects import pandas2ri
import math, datetime
import numpy as np
import pandas as pd
from plotnine import *
from PIL import Image
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as seabornInstance
import os

c_col = ["#2f4858", "#f6ae2d", "#f26419",
         "#33658a", "#55dde0", "#2f4858",
         "#2f4858", "#f6ae2d", "#f26419",
         "#33658a", "#55dde0", "#2f4858"]


def label(from_, to_, step_):
    return pd.Series(np.arange(from_, to_ + step_, step_)).apply(lambda x: '{:,}'.format(x)).tolist()


def breaks(from_, to_, step_):
    return pd.Series(np.arange(from_, to_ + step_, step_)).tolist()


rprint = robjects.globalenv.get("print")
stats = importr('stats')
grdevices = importr('grDevices')
base = importr('base')
datasets = importr('datasets')
pandas2ri.activate()
lattice = importr('lattice')
xyplot = lattice.xyplot
pandas2ri.activate()
module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, 'wypadki.csv')
wypadki = pd.read_csv(file_path, sep=';')

dolnoslaskie = wypadki[(wypadki.ID > 200000) & (wypadki.ID < 400000)]
dolnoslaskie = dolnoslaskie.reset_index(drop=True)
wojewodztwa = wypadki[
    (wypadki.ID == 200000) | (wypadki.ID == 400000) | (wypadki.ID == 600000) | (wypadki.ID == 800000) | (
                wypadki.ID == 1000000) | (wypadki.ID == 1200000) | (wypadki.ID == 1400000) | (wypadki.ID == 1600000) | (
                wypadki.ID == 1800000) | (wypadki.ID == 2000000) | (wypadki.ID == 2200000) | (wypadki.ID == 2400000) | (
                wypadki.ID == 2600000) | (wypadki.ID == 2800000) | (wypadki.ID == 3000000) | (wypadki.ID == 3200000)]


# print(age)

def show_info(thelist,tes,name1,name2):
    min = base.min(thelist[tes])
    # print("Najmniejsza wartosc ", min)
    max = base.max(thelist[tes])
    # print("Najwieksza wartosc ", max)
    avg = base.mean(thelist[tes])
    # print("Srednia wartosc ", avg)
    sd = stats.sd(thelist[tes])
    # print("Odchylenie standardowe ", sd)
    median = stats.median(thelist[tes])
    # print("Mediana ", median)
    s1, s2, s3 = np.percentile(thelist[tes], [25, 50, 75])
    # print("Pierwszy kwartyl: " + str(s1) + "\nDrugi kwartyl: "+str(s2) + "\nTrzeci kwartyl: "+str(s3)+"\n")
    iqr = stats.IQR(thelist[tes])
    # print("Rozstep miedzykwartylowy ", iqr)
    q1 = stats.quantile(thelist[tes], 0.1)
    q2 = stats.quantile(thelist[tes], 0.9)
    # print("Kwantyl 0.1 ", q1)
    # print("Kwantyl 0.9 ", q2)

    oddalone = []
    oddalone.clear()
    oddalone = find_outliers(thelist,tes)

    summary = "Statystki "+name1+" , "+name2+"\nNajmniejsza wartość: " + str(min)[3:] + "Najwieksza wartość: " +str(max)[3:] + "Średnia wartość: "+str(avg)[3:] + "Odchylenie standardowe: " + str(sd)[3:] + "" \
             "Mediana: "+str(median)[3:] + "Pierwszy kwartyl: " + str(s1) + "\nDrugi kwartyl: " + str(s2) + "\nTrzeci kwartyl: " + str(s3) + "\nRozstęp miedzykwartylowy IQR: " +str(iqr)[3:]+"Kwantyl 0.1: " +str(q1)[4:] + "Kwantyl 0.9: " +str(q2)[5:] + "\nPunkty oddalone \n" + '\n'.join(oddalone)
    return summary


def pearson(thelist, thelist1):
    cor = stats.cor(thelist, thelist1)
    return cor


def show_records(thelist):
    print(thelist)


def show_test(item1,item2,item3,item4,item5,item6):
    p = pearson(item1[item2], item1[item3])
    fig = (
            (ggplot(item1, aes(x=item1[item2], y=item1[item3]))
             + geom_point())
            +
            labs(
                title='Wykres korelacji danych '+item6+", współczynnik pearsona wynosi "+str(p)[3:],
                y=item4,
                x=item5
            ))
    fig
    fig.save('wykresy\mrelacja2.jpg', width=10, height=7)



outliers = []


def find_outliers(data_1,tes):
    sorted(data_1[tes])
    q1, q3 = np.percentile(data_1[tes], [25, 75])
    outliers.clear()
    iqr = q3 - q1

    lower_bound = q1 - (1.5 * iqr)

    upper_bound = q3 + (1.5 * iqr)
    i = 1
    for y in data_1[tes]:
        i = +1
        if y < lower_bound or y > upper_bound:

            x = data_1.loc[data_1[tes] == y, 'NAZWA']
            q = x.to_string(header=None, index=None)


            final = str(y) +" - " + q
            print(final)
            outliers.append(final)
    if not outliers:
        outliers.append("Brak punktów oddalonych !")
    return outliers


find_outliers(dolnoslaskie,"r7")
def stats_plot(item1, item2,item3,item4):
    arr = []
    arr = list(range(0 + len(item1)))
    Q1 = item1[item2].quantile(0.25)
    Q3 = item1[item2].quantile(0.75)
    IQR = Q3 - Q1

    sdf = pd.DataFrame({
        'Statystyki': [
            'Średnia', 'Mediana', 'IQR',
            'Kwantyl 0.1', 'Kwantyl 0.9',
            'Odchylenie standardowe', 'Min', 'Max'
        ],
        'value': [
            item1[item2].mean(), item1[item2].median(), IQR,
            item1[item2].quantile(0.1), item1[item2].quantile(0.9),
            item1[item2].std(), item1[item2].min(), item1[item2].max()
        ]
    })

    fig = (
            ggplot(item1) +
            aes(x=arr, y=item1[item2]) +
            geom_point(size=1) +
            labs(
                title=item4 + " w "+item3+" wraz ze statystykami",
                x='Index',
                y=item4,
            ) +
            geom_hline(sdf, aes(yintercept='value', colour='Statystyki'), show_legend=True)
        # geom_point(out, aes(x='x',y='y'),color="red", show_legend=True )

    )
    fig.save('wykresy\mstats.jpg')


#stats_plot(dolnoslaskie,"w7","bla","bla")

def dotplot():
    fig = (
            ggplot(dolnoslaskie) +
            aes(x='w7') +
            geom_dotplot(binwidth=0.5)
    )

    fig.save('./07.jpg')
    im = Image.open("07.jpg")
    im.show()

#dotplot()

def relationship(item1,item2,item3,item4,item5,item6):
    p = pearson(item1[item2],item1[item3])
    fig = (
            ggplot(item1) +
            geom_bin2d(
                aes(x=item2,
                    y=item3)
            ) +
            labs(

                title="Relacja pomiędzy danymi dla " +item6+" , współczynnik pearsona wynosi "+str(p)[3:],
                x=item4,
                y=item5
            ) +
            theme(figure_size=(8, 8))

    )
    fig.save('wykresy\mrelacja1.jpg')

#show_test(dolnoslaskie,"w7","z8","bla","bla","bla")

def regresja():
    dataframe = pd.DataFrame({'wypadki': wojewodztwa.w7,
                              'ranni': wojewodztwa.r7})

    print(dataframe)
    pandas2ri.activate()
    robjects.globalenv['dataframe'] = dataframe
    M = stats.lm('wypadki~ranni', data=base.as_symbol('dataframe'))
    print(base.summary(M).rx2('coefficients'))


def testhist():
    fig2 = (
            ggplot(dolnoslaskie) +
            geom_bar(

                aes(x='w7'),
                # binwidth =1,
                fill=c_col[1], color='black'
            ) +
            labs(
                title='Histogram wieku osób oddających krew',
                x='Wiek',
                y='Częstotliwość',
            ) +
            scale_y_continuous(
                # limits =(0,300),
                # labels = labels(0,300, 30),
                breaks=breaks(0, 35, 3)
            ) +
            scale_x_continuous(
                # limits =(0,100),
                # labels = label(0,100, 1),
                breaks=breaks(0, 565, 30)
            )
    )
    fig2
    fig2.save('./ahis.png')
    im2 = Image.open("ahis.png")
    im2.show()



def testbox():
    fig = (
            ggplot(dolnoslaskie) +
            geom_boxplot(
                aes(x='w7', y='w7')
            ) +
            labs(
                title='Distribution of time',
                y='Wypadki',
                x=''
            )
    )

    fig
    fig.save('./tbp.png')
    im = Image.open("tbp.png")
    im.show()


def testregresion(item1, item2,item3,item4,item5,item6):
    plt.figure()
    X = item1[item2].values.reshape(-1, 1)
    Y = item1[item3].values.reshape(-1, 1)
    print(X)
    print(Y)
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    Y_pred = linear_regressor.predict(X)
    slope = str(linear_regressor.coef_)
    inter = str(linear_regressor.intercept_)
    plt.scatter(X, Y)
    plt.plot(X, Y_pred, color='red')
    plt.ylabel(item6)
    plt.xlabel(item5+"\n" + "Dane dla "+item4+" Funkcja regresji: y="+inter[1:7]+"x + "+slope[2:7])
    plt.savefig("wykresy\mregresja.png", bbox_inches='tight')
    plt.show()
    plt.close()

testregresion(dolnoslaskie,"w7","w8","bla","bla","bla")

def mb(item1,item2,item3,item4):
    plt.figure()
    plt.boxplot(item1[item2])
    plt.xlabel("Wykres pudełkowy "+item3 +" dla "+item4)
    plt.ylabel(item3)
    plt.savefig('wykresy\mboxplot.png', bbox_inches='tight',dpi=1200)
    plt.show()
    plt.close()




def mhitbox(item1, item2, item3, item4):
    plt.figure()
    plt.hist(item1[item2], bins=10, color='#0504aa', alpha=0.7, rwidth=0.85)
    plt.grid(axis='y', alpha=0.6)
    plt.ylabel('Ilosc')
    plt.xlabel(' ' + item3 + ' dla '+ item4)
    plt.savefig('wykresy\mhistogram.png', bbox_inches='tight')
    plt.show()
    plt.close()


#mhitbox(dolnoslaskie,"w7","bla","bla")

def mplotbar(atr1, atr2,item3,item4):
    y_pos = np.arange(len(atr1))
    plt.figure()
    plt.barh(y_pos, atr1[atr2], align='center', alpha=0.5)
    plt.yticks(y_pos, atr1.NAZWA)
    plt.xlabel(item4 + " dla "+item3)
    plt.grid(True)
    plt.savefig("wykresy\mbox.png", bbox_inches='tight')
    plt.close()





def multiple2017(atr1,atr2):
    n_groups = len(atr1)
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.09
    opacity = 0.8

    reacts1 = plt.barh(index, atr1['w7'], bar_width, alpha=opacity,
                       color='b',
                       label='Wypadki w 2017')
    reacts2 = plt.barh(index + bar_width, atr1['r7'], bar_width, alpha=opacity,
                       color='c',
                       label='Ranni w 2017')
    reacts3 = plt.barh(index + 2 * bar_width, atr1['z7'], bar_width, alpha=opacity,
                       color='y',
                       label='Ofiary smiertelne w 2017')
    plt.yticks(index + bar_width, atr1.NAZWA)
    plt.title = "Wykres z danymi dla " + atr2 + " w 2017 roku"
    plt.legend()
    plt.tight_layout()
    plt.grid(True)
    plt.savefig("wykresy\ogolne2017.png", bbox_inches='tight')


def multiple2018(atr1,atr2):
    n_groups = len(atr1)
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.09
    opacity = 0.8

    reacts1 = plt.barh(index, atr1['w8'], bar_width, alpha=opacity,
                       color='b',
                       label='Wypadki w 2018')
    reacts2 = plt.barh(index + bar_width, atr1['r8'], bar_width, alpha=opacity,
                       color='c',
                       label='Ranni w 2018')
    reacts3 = plt.barh(index + 2 * bar_width, atr1['z8'], bar_width, alpha=opacity,
                       color='y',
                       label='Ofiary smiertelne w 2018')
    plt.yticks(index + bar_width, atr1.NAZWA)
    plt.title = "Wykres z danymi dla " + atr2 + " w 2018 roku"
    plt.legend()
    plt.tight_layout()
    plt.grid(True)
    plt.savefig("wykresy\ogolne2018.png", bbox_inches='tight')

def xdx():
    x = [-1, 0.5, 1, -0.5]
    y = [0.5, 1, -0.5, -1]

    plt.plot(x, y, '-o')
    plt.axis('equal')
    plt.savefig('wtf.png', bbox_inches='tight')


