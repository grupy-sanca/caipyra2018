import matplotlib.pyplot as plt
import matplotlib.lines  as lines
import numpy as np

# dados em cada ano
# https://github.com/jtemporal/caipyra/blob/master/caipyra/estatisticas.py
anos    = [2016, 2017, 2018]
paçocas = [400, 825, 1625]
quentao = [125, 30, 40]
sonhos  = [696000, 1435500, 2871666] # milhares de sonhos em cada ano
carreta = [55, 90, 137]

participantes = [130, 200, 237]

# real costs a bit masked, but kept in proportion due to legal reasons
custos = {'fooooood' : 8137,
          'shirts + \nstuff like that' : 6842,
          'photography + \nfilming' : 3666,
          'speakers + \nkids space + \nstuff' : 3777}

# participantes x ano
with plt.xkcd():
    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.xticks(anos)
    plt.yticks([130, 200, 240])

    plt.plot(anos, participantes, '-', label = "Participants")
    plt.title("Caipyras of Caipyra")
    plt.xlabel("Year")
    plt.legend()
    plt.savefig("peoples.png",
                dpi = 150,
                transparent = True)


# generos em 2018
with plt.xkcd():
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    data = [200, 55, 2]
    generos = ['Men', 'Women', 'Non-binary']
    ax.pie(data, labels = generos, autopct ='%1.1f%%')

    plt.title("Gender composition in Caipyra2018")
    plt.tight_layout()
    plt.savefig("generos.png",
                dpi = 150,
                transparent = True)

# comidas x ano
with plt.xkcd():
    print("foods.png")
    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.xticks(anos)

    plt.plot(anos, paçocas, '-', label = "Pacoquinhas")
    plt.plot(anos, quentao, '-', label = "Liters of Quentao")

    plt.title("Consumption of Pacoquinhas and Quentao")
    plt.xlabel("Year")
    plt.legend()
    plt.savefig("foods.png",
                dpi = 150,
                transparent = True)


# custos em 2018
with plt.xkcd():
    print("custos.png")
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    ax.pie(custos.values(), labels = custos.keys(), autopct ='%1.1f%%')

    linhazinha = lines.Line2D([0], [0])
    ax.legend([linhazinha], ["total: ~ 22k BRL"],
              handlelength = 0, handletextpad = 0,
              fontsize = 'large', fancybox=True,
              loc="upper right",
              bbox_to_anchor=(0, 0, 0, 1)
              )

    plt.title("Costs of Caipyra2018")
    plt.tight_layout()
    plt.savefig("custos.png",
                dpi = 150,
                transparent = True)