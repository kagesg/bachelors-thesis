##------------------------------Importando bibliotecas------------------------------##
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

##------------------------------Definições de listas e parâmetros------------------------------##
filename = ['Resultados_1.xlsx','Resultados_2.xlsx','Resultados_3.xlsx']

nome_tab = [['Temp_1_1','Temp_1_2','Temp_1_3','Temp_1_4','Temp_1_5','Temp_1_6'],
        ['Temp_3_1','Temp_3_2','Temp_3_3','Temp_3_4','Temp_3_5','Temp_3_6'],
        ['Press_1_1','Press_1_2','Press_1_3','Press_1_4','Press_1_5','Press_1_6']]

x_label = ['Temperatura entrada água ' + r'$\left [ °C \right ]$',
        'Temperatura entrada gás ' + r'$\left [ °C \right ]$',
        'Pressão absoluta água ' + r'$\left [ bar \right ]$']

y_label = ['Temperatura saída gás de exaustão ' + r'$\left [ °C \right ]$',
        'Vazão mássica água ' + r'$\left [ \frac{kg}{h} \right ]$']

x_scale = [[9, 31],[730, 870],[2.5,12.5]]
y_scale_1 = [[170, 220],[175, 225],[180, 230]]
y_scale_2 = [[7, 16],[7, 17],[7, 17]]

major_tick_x = [1,10,0.5]
major_tick_y_1 = [5,5,5]
major_tick_y_2 = [1,1,1]

txt_px_1 = [x_scale[0][0]+major_tick_x[0]*1,x_scale[1][0]+major_tick_x[1]*0.5,x_scale[2][0]+major_tick_x[2]*1]
txt_px_2 = [x_scale[0][0]+major_tick_x[0]*1,x_scale[1][0]+major_tick_x[1]*0.5,x_scale[2][0]+major_tick_x[2]*12]

txt_py_1 = [y_scale_1[0][1]-major_tick_y_1[0]*1.5,y_scale_1[1][1]-major_tick_y_1[1]*1.5,y_scale_1[2][1]-major_tick_y_1[2]*1.5]
txt_py_2 = [y_scale_2[0][1]-major_tick_y_2[0]*1.5,y_scale_2[1][1]-major_tick_y_2[1]*1.5,y_scale_2[2][1]-major_tick_y_2[2]*1.5]

texto = ['Vazão mássica gás = 8.6 '+r'$\frac{kg}{h}$'+'\nPressão absoluta gás = 1 '+r'$bar$'+'\nTemperatura entrada gás = 780 '+r'$°C$',
        'Vazão mássica gás = 8.6 '+r'$\frac{kg}{h}$'+'\nPressão absoluta gás = 1 '+r'$bar$'+'\nTemperatura entrada água = 25 '+r'$°C$',
        'Vazão mássica gás = 8.6 '+r'$\frac{kg}{h}$'+'\nPressão absoluta gás = 1 '+r'$bar$'+'\nTemperatura entrada gás = 780 '+r'$°C$',
        'Vazão mássica gás = 8.6 '+r'$\frac{kg}{h}$'+'\nPressão absoluta gás = 1 '+r'$bar$'+'\nPressão absoluta água = 5 '+r'$bar$',
        'Vazão mássica gás = 8.6 '+r'$\frac{kg}{h}$'+'\nPressão absoluta gás = 1 '+r'$bar$'+'\nPressão absoluta água = 5 '+r'$bar$',
        'Vazão mássica gás = 8.6 '+r'$\frac{kg}{h}$'+'\nPressão absoluta gás = 1 '+r'$bar$'+'\nTemperatura entrada água = 25 '+r'$°C$']

legenda = [['Pressão absoluta água = 3 '+r'$bar$','Pressão absoluta água = 5 '+r'$bar$','Pressão absoluta água = 12 '+r'$bar$'],
        ['Pressão absoluta água = 3 '+r'$bar$','Pressão absoluta água = 5 '+r'$bar$','Pressão absoluta água = 12 '+r'$bar$'],
        ['Temperatura entrada água = 10 '+r'$°C$','Temperatura entrada água = 20 '+r'$°C$','Temperatura entrada água = 35 '+r'$°C$'],
        ['Temperatura entrada gás = 740 '+r'$°C$','Temperatura entrada gás = 780 '+r'$°C$','Temperatura entrada gás = 860 '+r'$°C$'],
        ['Temperatura entrada água = 10 '+r'$°C$','Temperatura entrada água = 20 '+r'$°C$','Temperatura entrada água = 35 '+r'$°C$'],
        ['Temperatura entrada gás = 740 '+r'$°C$','Temperatura entrada gás = 780 '+r'$°C$','Temperatura entrada gás = 860 '+r'$°C$']]

leng_loc = [4,4,3]

size = 40
f_size = 10
pad = 8
alpha = 1

##------------------------------Função para importar os resultados------------------------------##
def import_df(filename,sheetname):
    df = pd.DataFrame(pd.read_excel(r"C:\\Users\\gusta\\OneDrive\\UTFPR\\TCC\\Programas\\GitHub-TCC\\"+filename,sheet_name=sheetname))
    df = df.loc[1:]
    df = df.reset_index()
    df = df.drop(['Unnamed: 0','index'], axis='columns', inplace=False)

    if filename == 'Resultados_3.xlsx':
        df = df[['Temperatura entrada água','Temperatura saída água','Temperatura entrada ar','Pressão água','Temperatura saída ar','Vazão água','Vazão do ar','Delta_Tml','Reynolds ar','Reynolds água','Nusselt ar','Nusselt água','Coef. convectivo ar','Coef. convectivo água','Calor ar','Calor água','Calor coef. global','Pressão ar']]
    return df

##------------------------------Agrupar as colunas e calcular valor médio da temperatura de saida do gás e da vazão da água------------------------------##
def group_1(df,order):
    df = df.groupby(by=order, as_index=False).mean()
    return df

##------------------------------Escolher qual dado para os gráficos------------------------------##
modo = int(input('Selecione o modo do gráfico:\n0:Temperatura de entrada água\n1:Temperatura de entrada gás\n2:Pressão da água\n'))

##------------------------------Salvar ou não os gráficos------------------------------##
ger_graf = str(input('Deseja salvar o gráfico? [S/N]'))

##------------------------------Criando DFs para cada simulação------------------------------##
df_1 = import_df(filename[modo],nome_tab[modo][0])
df_2 = import_df(filename[modo],nome_tab[modo][1])
df_3 = import_df(filename[modo],nome_tab[modo][2])
df_4 = import_df(filename[modo],nome_tab[modo][3])
df_5 = import_df(filename[modo],nome_tab[modo][4])
df_6 = import_df(filename[modo],nome_tab[modo][5])

#------------------------------Obtendo o index das colunas e definindo listas de colunas para cada modo------------------------------##
columns = df_1.columns.tolist()
ordem_gb = [[columns[0],columns[1],columns[2]],
            [columns[2],columns[0],columns[1]],
            [columns[3],columns[0],columns[1],columns[2]]]

if modo == 0:
    col_x = columns[0]
    col_y1 = columns[3]
    col_y2 = columns[4]
elif modo == 1:
    col_x = columns[2]
    col_y1 = columns[3]
    col_y2 = columns[4]
elif modo == 2:
    col_x = columns[3]
    col_y1 = columns[4]
    col_y2 = columns[5]

##------------------------------Agrupando dados e calculando os valores médios para os resultados encontrados------------------------------##
df_1 = group_1(df_1,ordem_gb[modo])
df_2 = group_1(df_2,ordem_gb[modo])
df_3 = group_1(df_3,ordem_gb[modo])
df_4 = group_1(df_4,ordem_gb[modo])
df_5 = group_1(df_5,ordem_gb[modo])
df_6 = group_1(df_6,ordem_gb[modo])

##------------------------------Criar figura e eixos com subplots() em gráficos separados (Grid 2X2)------------------------------##
fig,axs = plt.subplots(2,2,figsize=(22,15),dpi=100)

for i in range(0,2,1):

    for j in range(0,2,1):
        if i >= 1:
            
axs[0,0].scatter(df_1[col_x], df_1[col_y1], color = '#FF3333',marker="P", s = size+5, label=legenda[modo][0])
axs[0,0].plot(df_1[col_x], df_1[col_y1],color = '#FF3333',linewidth=0.75)
axs[1,0].scatter(df_1[col_x], df_1[col_y2], color = '#3333FF',marker="P", s = size+5,label=legenda[modo][0])
axs[1,0].plot(df_1[col_x], df_1[col_y2],color = '#3333FF',linewidth=0.75)
axs[0,1].scatter(df_4[col_x], df_4[col_y1], color = '#FF9933',marker="X", s = size+12, label=legenda[modo+3][0])
axs[0,1].plot(df_4[col_x], df_4[col_y1],color = '#FF9933',linewidth=0.75)
axs[1,1].scatter(df_4[col_x], df_4[col_y2], color = '#9933FF',marker="X", s = size+12,label=legenda[modo+3][0])
axs[1,1].plot(df_4[col_x], df_4[col_y2],color = '#9933FF',linewidth=0.75)

axs[0,0].scatter(df_2[col_x], df_2[col_y1], color = '#CC0000',marker="d", s = size+2, label=legenda[modo][1])
axs[0,0].plot(df_2[col_x], df_2[col_y1],color = '#CC0000',linewidth=0.75)
axs[1,0].scatter(df_2[col_x], df_2[col_y2], color = '#0000CC',marker="d", s = size+2,label=legenda[modo][1])
axs[1,0].plot(df_2[col_x], df_2[col_y2],color = '#0000CC',linewidth=0.75)
axs[0,1].scatter(df_5[col_x], df_5[col_y1], color = '#CC6600',marker="D", s = size-2, label=legenda[modo+3][1])
axs[0,1].plot(df_5[col_x], df_5[col_y1],color = '#CC6600',linewidth=0.75)
axs[1,1].scatter(df_5[col_x], df_5[col_y2], color = '#6600CC',marker="D", s = size-2,label=legenda[modo+3][1])
axs[1,1].plot(df_5[col_x], df_5[col_y2],color = '#6600CC',linewidth=0.75)

axs[0,0].scatter(df_3[col_x], df_3[col_y1], color = '#660000',marker="o", s = size+3, label=legenda[modo][2])
axs[0,0].plot(df_3[col_x], df_3[col_y1],color = '#660000',linewidth=0.75)
axs[1,0].scatter(df_3[col_x], df_3[col_y2], color = '#000066',marker="o", s = size+3,label=legenda[modo][2])
axs[1,0].plot(df_3[col_x], df_3[col_y2],color = '#000066',linewidth=0.75)
axs[0,1].scatter(df_6[col_x], df_6[col_y1], color = '#663300',marker="p", s = size+10, label=legenda[modo+3][2])
axs[0,1].plot(df_6[col_x], df_6[col_y1],color = '#663300',linewidth=0.75)
axs[1,1].scatter(df_6[col_x], df_6[col_y2], color = '#330066',marker="p", s = size+10,label=legenda[modo+3][2])
axs[1,1].plot(df_6[col_x], df_6[col_y2],color = '#330066',linewidth=0.75)

##------------------------------Limites eixos------------------------------##
axs[0,0].set_xlim([x_scale[modo][0],x_scale[modo][1]])
axs[0,0].set_ylim([y_scale_1[modo][0],y_scale_1[modo][1]])
axs[1,0].set_xlim([x_scale[modo][0],x_scale[modo][1]])
axs[1,0].set_ylim([y_scale_2[modo][0],y_scale_2[modo][1]])
axs[0,1].set_xlim([x_scale[modo][0],x_scale[modo][1]])
axs[0,1].set_ylim([y_scale_1[modo][0],y_scale_1[modo][1]])
axs[1,1].set_xlim([x_scale[modo][0],x_scale[modo][1]])
axs[1,1].set_ylim([y_scale_2[modo][0],y_scale_2[modo][1]])

##------------------------------Texto de condições da simulação------------------------------##
axs[0,0].text(txt_px_1[modo],txt_py_1[modo],texto[modo],fontsize=f_size,bbox={'facecolor': '#FFFFFF','alpha': alpha,'pad': pad,'boxstyle':'round, pad=0.25'})
axs[0,0].text(txt_px_1[modo],txt_py_1[modo],texto[modo],fontsize=f_size,bbox={'facecolor': '#FFFFFF','alpha': alpha,'pad': pad,'boxstyle':'round, pad=0.25'})


axs[1,0].text(txt_px_2[modo],txt_py_2[modo],texto[modo],fontsize=f_size,bbox={'facecolor': '#FFFFFF','alpha': alpha,'pad': pad,'boxstyle':'round, pad=0.25'})



axs[0,1].text(txt_px_1[modo],txt_py_1[modo],texto[modo+3],fontsize=f_size,bbox={'facecolor': '#FFFFFF','alpha': alpha,'pad': pad,'boxstyle':'round, pad=0.25'})



axs[1,1].text(txt_px_2[modo],txt_py_2[modo],texto[modo+3],fontsize=f_size,bbox={'facecolor': '#FFFFFF','alpha': alpha,'pad': pad,'boxstyle':'round, pad=0.25'})




##------------------------------Configuração do grid------------------------------##
axs[0,0].xaxis.set_major_locator(MultipleLocator(major_tick_x[modo]))
axs[0,0].yaxis.set_major_locator(MultipleLocator(major_tick_y_1[modo]))
axs[0,0].yaxis.set_minor_locator(AutoMinorLocator())
axs[0,0].grid(which='major',linestyle = '-', linewidth = 1,alpha = 0.5)
axs[0,0].set_axisbelow(True)

axs[1,0].xaxis.set_major_locator(MultipleLocator(major_tick_x[modo]))
axs[1,0].yaxis.set_major_locator(MultipleLocator(major_tick_y_2[modo]))
axs[1,0].yaxis.set_minor_locator(AutoMinorLocator())
axs[1,0].grid(which='major',linestyle = '-', linewidth = 1,alpha = 0.5)
axs[1,0].set_axisbelow(True)

axs[0,1].xaxis.set_major_locator(MultipleLocator(major_tick_x[modo]))
axs[0,1].yaxis.set_major_locator(MultipleLocator(major_tick_y_1[modo]))
axs[0,1].yaxis.set_minor_locator(AutoMinorLocator())
axs[0,1].grid(which='major',linestyle = '-', linewidth = 1,alpha = 0.5)
axs[0,1].set_axisbelow(True)

axs[1,1].xaxis.set_major_locator(MultipleLocator(major_tick_x[modo]))
axs[1,1].yaxis.set_major_locator(MultipleLocator(major_tick_y_2[modo]))
axs[1,1].yaxis.set_minor_locator(AutoMinorLocator())
axs[1,1].grid(which='major',linestyle = '-', linewidth = 1,alpha = 0.5) 
axs[1,1].set_axisbelow(True)

##------------------------------Etiquetas dos gráficos------------------------------##

axs[0,0].set_ylabel(y_label[0], fontsize = 14, fontweight="medium")
axs[0,0].set_xlabel(x_label[modo], fontsize = 14, fontweight="medium")
axs[1,0].set_ylabel(y_label[1], fontsize = 14, fontweight="medium")
axs[1,0].set_xlabel(x_label[modo], fontsize = 14, fontweight="medium")
axs[0,1].set_ylabel(y_label[0], fontsize = 14, fontweight="medium")
axs[0,1].set_xlabel(x_label[modo], fontsize = 14, fontweight="medium")
axs[1,1].set_ylabel(y_label[1], fontsize = 14, fontweight="medium")
axs[1,1].set_xlabel(x_label[modo], fontsize = 14, fontweight="medium")



axs[0,0].legend(loc=4,frameon=True,framealpha=alpha,edgecolor='inherit',labelspacing = 0.25,borderpad=0.5)
axs[1,0].legend(loc=leng_loc[modo],frameon=True,framealpha=alpha,edgecolor='inherit',labelspacing = 0.25,borderpad=0.5)
axs[0,1].legend(loc=4,frameon=True,framealpha=alpha,edgecolor='inherit',labelspacing = 0.25,borderpad=0.5)
axs[1,1].legend(loc=leng_loc[modo],frameon=True,framealpha=alpha,edgecolor='inherit',labelspacing = 0.2,borderpad=0.5)

##------------------------------Salvar o gráfico em arquivo .png------------------------------##
if ger_graf == 'S' and ger_graf != "":
    plt.savefig('Grafico_final_'+str(modo+1)+'_e',pad_inches=0.1)

##------------------------------Mostar o gráfico------------------------------##
plt.show()