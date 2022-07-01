import matplotlib.pyplot as plt, pylab, pandas as pd, matplotlib.ticker, csv, numpy as np, json

def datasetIniziale():
    data = pd.read_csv('datasetIniziale.csv', sep=',')
    data.columns=["Regione", "Dotazione riscaldamento", "Dotazione acqua calda", "Dotazione condizionamento", "Riscaldamento e acqua calda coincidenti", "Riscaldamento e condizionamento coincidenti", "Piu tipi di dotazioni per il riscaldamento", "Piu tipi di dotazioni per acqua calda", "Piu tipi di dotazioni per il condizionamento"]
    data = data.replace(['..'],'0.0')
    data = data.replace(['....'], 'NULL')
    data = data.replace(['-'], 'NULL')
    data = data.astype({"Regione": str, "Dotazione riscaldamento": float, "Dotazione acqua calda": float, "Dotazione condizionamento": float, "Riscaldamento e acqua calda coincidenti": float, "Riscaldamento e condizionamento coincidenti": float, "Piu tipi di dotazioni per il riscaldamento": float, "Piu tipi di dotazioni per acqua calda": float, "Piu tipi di dotazioni per il condizionamento": float})
    conversioneToCsv=data.to_csv('.\datasetLeggibile\datasetIniziale_updated.csv', columns=('Regione', 'Dotazione riscaldamento', 'Dotazione acqua calda', 'Dotazione condizionamento', 'Riscaldamento e acqua calda coincidenti', 'Riscaldamento e condizionamento coincidenti', 'Piu tipi di dotazioni per il riscaldamento', 'Piu tipi di dotazioni per acqua calda', 'Piu tipi di dotazioni per il condizionamento'), index=False, sep=';', decimal=',')
def valoreMassimo():
    df = pd.read_csv('.\datasetLeggibile\datasetIniziale_updated.csv', usecols=['Regione', 'Dotazione riscaldamento', 'Dotazione acqua calda',	'Dotazione condizionamento'], sep=';', decimal=',')
    df.columns=["Regione", "Dotazione_riscaldamento", "Dotazione_acqua_calda", "Dotazione_condizionamento"]
    media = df[['Dotazione_riscaldamento', 'Dotazione_acqua_calda', 'Dotazione_condizionamento']].mean(axis=1).nlargest(3, keep='all').sort_values(ascending=False).reset_index(name='Media valori')
    print(media)
    veneto = df[(df['Regione']=='Veneto')]
    emilia = df[(df['Regione']=='Emilia-Romagna')]
    sardegna = df[(df['Regione']=='Sardegna')]

    regioni = df[(df['Regione']=='Veneto') | (df['Regione']=='Emilia-Romagna') | (df['Regione'] == 'Sardegna')]
    regioni.to_csv('.\datasetRegioni\maxValue.csv', sep=';', decimal=',', index=False)
    ########################### Dotazione Riscaldamento ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3

    veneto_y = veneto.Dotazione_riscaldamento
    emilia_y = emilia.Dotazione_riscaldamento
    sardegna_y = sardegna.Dotazione_riscaldamento

    bar1 = plt.bar(br1, veneto_y, color ='#50A3A4', width = barWidth, edgecolor ='grey', label ='Veneto')
    bar2 = plt.bar(br2, emilia_y, color ='#FCAF38', width = barWidth, edgecolor ='grey', label ='Emilia Romagna')
    bar3 = plt.bar(br3, sardegna_y, color ='#F95335', width = barWidth, edgecolor ='grey', label = "Sardegna")
        
    for rect in bar1 + bar2 + bar3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.1f}%',ha='center',va='bottom')
    
    plt.xlabel('Regioni', fontweight ='bold', fontsize = 15)
    plt.ylabel('Dotazione riscaldamento', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.ylim((0,10))
    plt.yticks((0,100,10,20,30,40,50,60,70,80,90,100))
    ax.set_xticks([])

    ax.legend(loc="lower right")
    plt.savefig('.\maxValori\dotazioneRiscaldamento.png', dpi=300)
    ########################### Dotazione Acqua Calda ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3

    veneto_y = veneto.Dotazione_acqua_calda
    emilia_y = emilia.Dotazione_acqua_calda
    sardegna_y = sardegna.Dotazione_acqua_calda

    bar1 = plt.bar(br1, veneto_y, color ='#50A3A4', width = barWidth, edgecolor ='grey', label ='Veneto')
    bar2 = plt.bar(br2, emilia_y, color ='#FCAF38', width = barWidth, edgecolor ='grey', label ='Emilia Romagna')
    bar3 = plt.bar(br3, sardegna_y, color ='#F95335', width = barWidth, edgecolor ='grey', label = "Sardegna")
        
    for rect in bar1 + bar2 + bar3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.1f}%',ha='center',va='bottom')
    
    plt.xlabel('Regioni', fontweight ='bold', fontsize = 15)
    plt.ylabel('Dotazione acqua calda', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.yticks((0,100,10,20,30,40,50,60,70,80,90,100))
    ax.set_xticks([])

    ax.legend(loc="lower right")
    plt.savefig('.\maxValori\dotazioneAcquaCalda.png', dpi=300)
    ########################### Dotazione Condizionamento ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3

    veneto_y = veneto.Dotazione_condizionamento
    emilia_y = emilia.Dotazione_condizionamento
    sardegna_y = sardegna.Dotazione_condizionamento

    bar1 = plt.bar(br1, veneto_y, color ='#50A3A4', width = barWidth, edgecolor ='grey', label ='Veneto')
    bar2 = plt.bar(br2, emilia_y, color ='#FCAF38', width = barWidth, edgecolor ='grey', label ='Emilia Romagna')
    bar3 = plt.bar(br3, sardegna_y, color ='#F95335', width = barWidth, edgecolor ='grey', label = "Sardegna")
        
    for rect in bar1 + bar2 + bar3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.1f}%',ha='center',va='bottom')
    
    plt.xlabel('Regioni', fontweight ='bold', fontsize = 15)
    plt.ylabel('Dotazione condizionamento', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.yticks((0,100,10,20,30,40,50,60,70,80,90,100))
    ax.set_xticks([])

    ax.legend(loc="lower right")

    plt.savefig('.\maxValori\dotazioneCondizionamento.png', dpi=300)
def valoreMinimo():
    df = pd.read_csv('.\datasetLeggibile\datasetIniziale_updated.csv', usecols=['Regione', 'Dotazione riscaldamento', 'Dotazione acqua calda',	'Dotazione condizionamento'], sep=';', decimal=',')
    df.columns = ["Regione", "Dotazione_riscaldamento", "Dotazione_acqua_calda", "Dotazione_condizionamento"]
    media = df[['Dotazione_riscaldamento', 'Dotazione_acqua_calda', 'Dotazione_condizionamento']].mean(axis=1).nsmallest(3, keep='all').sort_values(ascending=False).reset_index(name='Media valori')
    print(media)
    valle_aosta = df[(df['Regione']=='Valle Aosta')]
    bolzano = df[(df['Regione']=='Bolzano')]
    trentino = df[(df['Regione']=='Trentino-Alto Adige')]
    regioni = df[(df['Regione'] == 'Valle Aosta') | (df['Regione']=='Bolzano') | (df['Regione']=='Trentino-Alto Adige')]
    regioni.to_csv('.\datasetRegioni\minValue.csv', sep=';', decimal=',', index=False)
    ########################### Dotazione Riscaldamento ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3

    valle_aosta_y = valle_aosta.Dotazione_riscaldamento
    bolzano_y = bolzano.Dotazione_riscaldamento
    trentino_y = trentino.Dotazione_riscaldamento

    bar1 = plt.bar(br1, valle_aosta_y, color ='#50A3A4', width = barWidth, edgecolor ='grey', label ="Valle d'Aosta")
    bar2 = plt.bar(br2, bolzano_y, color ='#FCAF38', width = barWidth, edgecolor ='grey', label ='Bolzano')
    bar3 = plt.bar(br3, trentino_y, color ='#F95335', width = barWidth, edgecolor ='grey', label = "Trentino Alto Adige")
        
    for rect in bar1 + bar2 + bar3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.1f}%',ha='center',va='bottom')

    plt.xlabel('Regioni', fontweight ='bold', fontsize = 15)
    plt.ylabel('Dotazione riscaldamento', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.ylim((0,10))
    plt.yticks((0,100,10,20,30,40,50,60,70,80,90,100))
    ax.set_xticks([])

    ax.legend(loc="lower right")
    plt.savefig('.\minValori\dotazioneRiscaldamento.png', dpi=300)
    ########################### Dotazione Acqua Calda ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3

    valle_aosta_y = valle_aosta.Dotazione_acqua_calda
    bolzano_y = bolzano.Dotazione_acqua_calda
    trentino_y = trentino.Dotazione_acqua_calda

    bar1 = plt.bar(br1, valle_aosta_y, color ='#50A3A4', width = barWidth, edgecolor ='grey', label ="Valle d'Aosta")
    bar2 = plt.bar(br2, bolzano_y, color ='#FCAF38', width = barWidth, edgecolor ='grey', label ='Bolzano')
    bar3 = plt.bar(br3, trentino_y, color ='#F95335', width = barWidth, edgecolor ='grey', label = "Trentino Alto Adige")
        
    for rect in bar1 + bar2 + bar3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.1f}%',ha='center',va='bottom')
    
    plt.xlabel('Regioni', fontweight ='bold', fontsize = 15)
    plt.ylabel('Dotazione acqua calda', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.yticks((0,100,10,20,30,40,50,60,70,80,90,100))
    ax.set_xticks([])

    ax.legend(loc="lower right")
    plt.savefig('.\minValori\dotazioneAcquaCalda.png', dpi=300)
    ########################### Dotazione Condizionamento ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3

    valle_aosta_y = valle_aosta.Dotazione_condizionamento
    bolzano_y = bolzano.Dotazione_condizionamento
    trentino_y = trentino.Dotazione_condizionamento

    bar1 = plt.bar(br1, valle_aosta_y, color ='#50A3A4', width = barWidth, edgecolor ='grey', label ="Valle d'Aosta")
    bar2 = plt.bar(br2, bolzano_y, color ='#FCAF38', width = barWidth, edgecolor ='grey', label ='Bolzano')
    bar3 = plt.bar(br3, trentino_y, color ='#F95335', width = barWidth, edgecolor ='grey', label = "Trentino Alto Adige")
        
    for rect in bar1 + bar2 + bar3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.1f}%',ha='center',va='bottom')
    
    plt.xlabel('Regioni', fontweight ='bold', fontsize = 15)
    plt.ylabel('Dotazione condizionamento', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.yticks((0,100,10,20,30,40,50,60,70,80,90,100))
    ax.set_xticks([])

    ax.legend(loc="upper right")

    plt.savefig('.\minValori\dotazioneCondizionamento.png', dpi=300)
def datasetSpecificheAcquaCalda():
    data = pd.read_csv('datasetSpecifiche.csv', sep=',')
    data = data.replace(['..'],'0.0')
    data = data.replace(['....'], 'NULL')
    data = data.replace(['-'], 'NULL')
    conversioneToCsv=data.to_csv('.\datasetLeggibile\datasetAcquaCalda_updated.csv', index=False, sep=';', decimal=',')
def concatenaDatasetAcquaCalda():
    data1 = pd.read_csv('.\datasetLeggibile\datasetSpecificheAcquaCalda.csv', usecols = ['REGIONE', 'Metano', 'Energia Solare'], sep=';', decimal=',')
    data1.columns = ('Regione', 'Metano', 'Energia_Solare')
    data2 = pd.read_csv('.\datasetLeggibile\RegioniInteressate.csv', usecols=['Dotazione_acqua_calda'], sep=';', decimal=',')
    regioni = data1[(data1['Regione']=='Veneto') | (data1['Regione']=='Emilia-Romagna') | (data1['Regione'] == 'Sardegna') | (data1['Regione'] == 'Valle Aosta') | (data1['Regione']=='Bolzano') | (data1['Regione']=='Trentino-Alto Adige')]
    regioni.to_csv('.\datasetLeggibile\datasetAcquaCalda_regioniInteressate.csv', sep = ';', decimal=',', index=0)
    data3 = pd.read_csv('.\datasetLeggibile\datasetAcquaCalda_regioniInteressate.csv', sep=';', decimal=',')
    a=pd.concat([data3, data2], axis=1)
    a.to_csv('.\datasetLeggibile\datasetConcatenatoAcquaCalda.csv', sep=';', index=0, decimal=',')
def concatena():
    data1 = pd.read_csv('.\datasetRegioni\maxValue.csv', sep=';')
    data2 = pd.read_csv('.\datasetRegioni\minValue.csv', sep=';')
    concatenazione = pd.concat([data1, data2], axis=0)
    concatenazione.to_csv('.\datasetLeggibile\RegioniInteressate.csv', sep=';', index=0, decimal=',')
def datasetAcquaCaldaElementi():
    df = pd.read_csv('.\datasetLeggibile\datasetConcatenatoAcquaCalda.csv', decimal=',', sep=';',index_col=0)
    maxValueEnergia = df[['Energia_Solare']].max(axis=1).sort_values(ascending=False).reset_index(name='Energia Solare max')
    maxValueMetano = df[['Metano']].max(axis=1).sort_values(ascending=False).reset_index(name='Metano max')

    minValueEnergia = df[['Energia_Solare']].min(axis=1).sort_values(ascending=True).reset_index(name='Energia Solare min')
    minValueMetano = df[['Metano']].min(axis=1).sort_values(ascending=True).reset_index(name='Metano min')
    print(maxValueEnergia, "\n")
    print(maxValueMetano, "\n")
    print(minValueEnergia, "\n")
    print(minValueMetano)

    df2 = pd.read_csv('.\datasetLeggibile\datasetConcatenatoAcquaCalda.csv', decimal=',', sep=';')
    ########################### Metano consumi maggiori ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3

    emilia_metano_max = df2[df2['Regione'] == 'Emilia-Romagna']
    veneto_metano_max = df2[df2['Regione'] == 'Veneto']
    trentino_metano_max = df2[df2['Regione'] == 'Trentino-Alto Adige']

    emilia_y = emilia_metano_max.Metano
    veneto_y = veneto_metano_max.Metano
    trentino_y = trentino_metano_max.Metano 

    bar1 = plt.bar(br1, emilia_y, color ='#50A3A4', width = barWidth, edgecolor ='grey', label ='Emilia Romagna')
    bar2 = plt.bar(br2, veneto_y, color ='#FCAF38', width = barWidth, edgecolor ='grey', label ='Veneto')
    bar3 = plt.bar(br3, trentino_y, color ='#F95335', width = barWidth, edgecolor ='grey', label = "Trentino Alto Adige")
        
    for rect in bar1 + bar2 + bar3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.1f}%',ha='center',va='bottom')
    
    plt.xlabel('Regioni', fontweight ='bold', fontsize = 15)
    plt.ylabel('Metano', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.ylim((0,10))
    plt.yticks((0,100,10,20,30,40,50,60,70,80,90,100))
    ax.set_xticks([])

    ax.legend(loc="upper right")
    plt.savefig('.\datasetRegioni\consumoAcqua\metano_max.png', dpi=300)
    ########################### Energia Solare consumi maggiori ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3

    bolzano_energia_max = df2[df2['Regione'] == 'Bolzano']
    trentino_energia_max = df2[df2['Regione'] == 'Trentino-Alto Adige']
    valle_aosta_energia_max = df2[df2['Regione'] == 'Valle Aosta']

    bolzano_y = bolzano_energia_max.Energia_Solare
    trentino_y = trentino_energia_max.Energia_Solare
    valle_aosta_y = valle_aosta_energia_max.Energia_Solare

    bar1 = plt.bar(br1, bolzano_y, color ='#50A3A4', width = barWidth, edgecolor ='grey', label ='Bolzano')
    bar2 = plt.bar(br2, trentino_y, color ='#FCAF38', width = barWidth, edgecolor ='grey', label ='Trentino Alto Adige')
    bar3 = plt.bar(br3, valle_aosta_y, color ='#F95335', width = barWidth, edgecolor ='grey', label = "Valle d'Aosta")
        
    for rect in bar1 + bar2 + bar3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.1f}%',ha='center',va='bottom')
    
    plt.xlabel('Regioni', fontweight ='bold', fontsize = 15)
    plt.ylabel('Energia Solare', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.ylim((0,10))
    plt.yticks((0,100,10,20,30,40,50,60,70,80,90,100))
    ax.set_xticks([])

    ax.legend(loc="upper right")
    plt.savefig('.\datasetRegioni\consumoAcqua\energia_solare_max.png', dpi=300)
    ########################### Metano consumi minori ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3

    sardegna_metano_min = df2[df2['Regione'] == 'Sardegna']
    valle_aosta_metano_min = df2[df2['Regione'] == 'Valle Aosta']
    bolzano_metano_min = df2[df2['Regione'] == 'Bolzano']

    sardegna_y = sardegna_metano_min.Metano
    valle_aosta_y = valle_aosta_metano_min.Metano
    bolzano_y = bolzano_metano_min.Metano

    bar1 = plt.bar(br1, sardegna_y, color ='#50A3A4', width = barWidth, edgecolor ='grey', label ='Sardegna')
    bar2 = plt.bar(br2, valle_aosta_y, color ='#FCAF38', width = barWidth, edgecolor ='grey', label ="Valle d'Aosta")
    bar3 = plt.bar(br3, bolzano_y, color ='#F95335', width = barWidth, edgecolor ='grey', label = "Bolzano")
        
    for rect in bar1 + bar2 + bar3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.1f}%',ha='center',va='bottom')
    
    plt.xlabel('Regioni', fontweight ='bold', fontsize = 15)
    plt.ylabel('Metano', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.ylim((0,10))
    plt.yticks((0,100,10,20,30,40,50,60,70,80,90,100))
    ax.set_xticks([])

    ax.legend(loc="upper right")
    plt.savefig('.\datasetRegioni\consumoAcqua\metano_min.png', dpi=300)
    ########################### Energia Solare consumi minori ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3

    emilia_energia_min = df2[df2['Regione'] == 'Emilia-Romagna']
    veneto_energia_min = df2[df2['Regione'] == 'Veneto']
    sardegna_energia_min = df2[df2['Regione'] == 'Sardegna']

    emilia_y = emilia_energia_min.Energia_Solare
    veneto_y = veneto_energia_min.Energia_Solare
    sardegna_y = sardegna_energia_min.Energia_Solare

    bar1 = plt.bar(br1, emilia_y, color ='#50A3A4', width = barWidth, edgecolor ='grey', label ='Emilia Romagna')
    bar2 = plt.bar(br2, veneto_y, color ='#FCAF38', width = barWidth, edgecolor ='grey', label ="Veneto")
    bar3 = plt.bar(br3, sardegna_y, color ='#F95335', width = barWidth, edgecolor ='grey', label = "Sardegna")
        
    for rect in bar1 + bar2 + bar3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.1f}%',ha='center',va='bottom')
    
    plt.xlabel('Regioni', fontweight ='bold', fontsize = 15)
    plt.ylabel('Energia Solare', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.ylim((0,10))
    plt.yticks((0,100,10,20,30,40,50,60,70,80,90,100))
    ax.set_xticks([])

    ax.legend(loc="upper right")
    plt.savefig('.\datasetRegioni\consumoAcqua\energia_solare_min.png', dpi=300)
def datasetSpecificheCondizionamento():
    data = pd.read_csv('datasetCondizionamento.csv', sep=';', usecols=['Regione', 'Tutti i giorni o quasi', 'Qualche giorno a settimana', 'Qualche giorno al mese', 'Solo occasionalmente o mai'])
    data.columns = ['Regione', 'Giornalmente', 'Spesso', 'Raramente', 'Occasionalmente o Mai']
    data = data.replace(['..'],'0.0')
    data = data.replace(['....'], 'NULL')
    data = data.replace(['-'], 'NULL')
    conversioneToCsv=data.to_csv('.\datasetLeggibile\datasetCondizionamento_updated.csv',index=False, sep=';', decimal=',')
def concatenaDatasetCondizionamento():
    data1 = pd.read_csv('.\datasetLeggibile\datasetCondizionamento_updated.csv', sep=';', decimal=',')
    data2 = pd.read_csv('.\datasetLeggibile\RegioniInteressate.csv', usecols=['Dotazione_condizionamento'], sep=';', decimal=',')
    regioni = data1[(data1['Regione']=='Veneto') | (data1['Regione']=='Emilia-Romagna') | (data1['Regione'] == 'Sardegna') | (data1['Regione'] == 'Valle Aosta') | (data1['Regione']=='Bolzano') | (data1['Regione']=='Trentino-Alto Adige')]
    regioni.to_csv('.\datasetLeggibile\datasetCondizionamento_regioniInteressate.csv', sep = ';', decimal=',', index=0)
    data3 = pd.read_csv('.\datasetLeggibile\datasetCondizionamento_regioniInteressate.csv', sep=';', decimal=',')
    a=pd.concat([data3, data2], axis=1)
    a.to_csv('.\datasetLeggibile\datasetConcatenatoCondizionamento.csv', sep=';', index=0, decimal=',')
def datasetCondizionamentoElementi():
    df = pd.read_csv('.\datasetLeggibile\datasetConcatenatoCondizionamento.csv', decimal=',', sep=';',index_col=0)
    df.columns = ['Giornalmente', 'Spesso', 'Raramente', 'Occasionalmente_o_mai', 'Dotazione_condizionamento']
    giornalmenteValue = df[['Giornalmente']].max(axis=1).sort_values(ascending=False).reset_index(name='Giornalmente')
    spessoValue = df[['Spesso']].max(axis=1).sort_values(ascending=False).reset_index(name='Spesso')
    raramenteValue = df[['Raramente']].min(axis=1).sort_values(ascending=True).reset_index(name='Raramente')
    occasionalmente_o_maiValue = df[['Occasionalmente_o_mai']].min(axis=1).sort_values(ascending=True).reset_index(name='Occasionalmente o mai')
    print(giornalmenteValue, "\n", spessoValue, "\n", raramenteValue, "\n", occasionalmente_o_maiValue)

    df2 = pd.read_csv('.\datasetLeggibile\datasetConcatenatoCondizionamento.csv', decimal=',', sep=';')
    df2.columns = ['Regione', 'Giornalmente', 'Spesso', 'Raramente', 'Occasionalmente_o_mai', 'Dotazione_condizionamento']
    ########################### Giornalmente consumi ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3
    br4 = br3 + 0.3
    br5 = br4 + 0.3
    br6 = br5 + 0.3
    veneto = df2[df2['Regione'] == 'Veneto']
    sardegna = df2[df2['Regione'] == 'Sardegna']
    emilia = df2[df2['Regione'] == 'Emilia-Romagna']
    trentino = df2[df2['Regione'] == 'Trentino-Alto Adige']
    bolzano = df2[df2['Regione'] == 'Bolzano']
    valle_aosta = df2[df2['Regione'] == 'Valle Aosta']
    
    veneto_y = veneto.Giornalmente
    sardegna_y = sardegna.Giornalmente
    emilia_y = emilia.Giornalmente
    trentino_y = trentino.Giornalmente
    bolzano_y = bolzano.Giornalmente
    valle_aosta_y = valle_aosta.Giornalmente

    blu = '#7293cb'
    arancione = '#e1974c'
    verde = '#84ba5b'
    magenta = '#d35e60'
    grigio = '#808585'
    viola = '#9067a7'

    bar1 = plt.bar(br6, veneto_y, color = blu, width = barWidth, edgecolor ='grey', label ='Veneto')
    bar2 = plt.bar(br5, sardegna_y, color = arancione, width = barWidth, edgecolor ='grey', label ='Sardegna')
    bar3 = plt.bar(br4, emilia_y, color = verde, width = barWidth, edgecolor ='grey', label = "Emilia Romagna")
    bar4 = plt.bar(br3, trentino_y, color = magenta, width = barWidth, edgecolor ='grey', label ='Trentino Alto Adige')
    bar5 = plt.bar(br2, bolzano_y, color = grigio, width = barWidth, edgecolor ='grey', label ='Bolzano')
    bar6 = plt.bar(br1, valle_aosta_y, color = viola, width = barWidth, edgecolor ='grey', label = "Valle d'Aosta")
        
    for rect in bar1 + bar2 + bar3 + bar4 + bar5 + bar6:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.1f}%',ha='center',va='bottom')
    
    plt.ylabel('Tutti i giorni o quasi', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.ylim((0,10))
    plt.yticks((0,100,10,20,30,40,50,60,70,80,90,100))
    ax.set_xticks([])

    ax.legend(loc="upper right")
    plt.savefig('.\datasetRegioni\consumoCondizionamento\consumoGiornaliero.png', dpi=300)
    ########################### Spesso consumi ###########################   
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3
    br4 = br3 + 0.3
    br5 = br4 + 0.3
    br6 = br5 + 0.3

    veneto_y = veneto.Spesso
    sardegna_y = sardegna.Spesso
    emilia_y = emilia.Spesso
    trentino_y = trentino.Spesso
    bolzano_y = bolzano.Spesso
    valle_aosta_y = valle_aosta.Spesso

    bar1 = plt.bar(br6, veneto_y, color = blu, width = barWidth, edgecolor ='grey', label ='Veneto')
    bar2 = plt.bar(br5, bolzano_y, color = arancione, width = barWidth, edgecolor ='grey', label ='Bolzano')
    bar3 = plt.bar(br4, emilia_y, color = verde, width = barWidth, edgecolor ='grey', label = "Emilia Romagna")
    bar4 = plt.bar(br3, trentino_y, color = magenta, width = barWidth, edgecolor ='grey', label ='Trentino Alto Adige')
    bar5 = plt.bar(br2, sardegna_y, color = grigio, width = barWidth, edgecolor ='grey', label ='Sardegna')
    bar6 = plt.bar(br1, valle_aosta_y, color = viola, width = barWidth, edgecolor ='grey', label = "Valle d'Aosta")
    for rect in bar1 + bar2 + bar3 + bar4 + bar5 + bar6:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.1f}%',ha='center',va='bottom')
    
    plt.ylabel('Qualche giorno a settimana', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.ylim((0,10))
    plt.yticks((0,100,10,20,30,40,50,60,70,80,90,100))
    ax.set_xticks([])

    ax.legend(loc="upper right")
    plt.savefig('.\datasetRegioni\consumoCondizionamento\consumoSpesso.png', dpi=300)
    ########################### Raramente consumi ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3
    br4 = br3 + 0.3
    br5 = br4 + 0.3
    br6 = br5 + 0.3
    
    veneto_y = veneto.Raramente
    sardegna_y = sardegna.Raramente
    emilia_y = emilia.Raramente
    trentino_y = trentino.Raramente
    bolzano_y = bolzano.Raramente
    valle_aosta_y = valle_aosta.Raramente

    bar1 = plt.bar(br1, trentino_y, color = blu, width = barWidth, edgecolor ='grey', label ='Trentino Alto Adige')
    bar2 = plt.bar(br2, veneto_y, color = arancione, width = barWidth, edgecolor ='grey', label ='Veneto')
    bar3 = plt.bar(br3, emilia_y, color = verde, width = barWidth, edgecolor ='grey', label = "Emilia Romagna")
    bar4 = plt.bar(br4, sardegna_y, color = magenta, width = barWidth, edgecolor ='grey', label ='Sardegna')
    bar5 = plt.bar(br5, bolzano_y, color = grigio, width = barWidth, edgecolor ='grey', label ='Bolzano')
    bar6 = plt.bar(br6, valle_aosta_y, color = viola, width = barWidth, edgecolor ='grey', label = "Valle d'Aosta")
    for rect in bar1 + bar2 + bar3 + bar4 + bar5 + bar6:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.1f}%',ha='center',va='bottom')
    
    plt.ylabel('Qualche giorno al mese', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.ylim((0,10))
    plt.yticks((0,100,10,20,30,40,50,60,70,80,90,100))
    ax.set_xticks([])

    ax.legend(loc="upper right")
    plt.savefig('.\datasetRegioni\consumoCondizionamento\consumoRaramente.png', dpi=300)
    ########################### Occasionalmente o mai consumi ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3
    br4 = br3 + 0.3
    br5 = br4 + 0.3
    br6 = br5 + 0.3
    
    veneto_y = veneto.Occasionalmente_o_mai
    sardegna_y = sardegna.Occasionalmente_o_mai
    emilia_y = emilia.Occasionalmente_o_mai
    trentino_y = trentino.Occasionalmente_o_mai
    bolzano_y = bolzano.Occasionalmente_o_mai
    valle_aosta_y = valle_aosta.Occasionalmente_o_mai

    bar1 = plt.bar(br1, veneto_y, color = blu, width = barWidth, edgecolor ='grey', label ='Veneto')
    bar2 = plt.bar(br2, sardegna_y, color = arancione, width = barWidth, edgecolor ='grey', label ='Sardegna')
    bar3 = plt.bar(br3, emilia_y, color = verde, width = barWidth, edgecolor ='grey', label = "Emilia Romagna")
    bar4 = plt.bar(br4, bolzano_y, color = magenta, width = barWidth, edgecolor ='grey', label ='Bolzano')
    bar5 = plt.bar(br5, trentino_y, color = grigio, width = barWidth, edgecolor ='grey', label ='Trentino Alto Adige')
    bar6 = plt.bar(br6, valle_aosta_y, color = viola, width = barWidth, edgecolor ='grey', label = "Valle d'Aosta")
    for rect in bar1 + bar2 + bar3 + bar4 + bar5 + bar6:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.1f}%',ha='center',va='bottom')
    
    plt.ylabel('Occasionalmente o mai', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.ylim((0,10))
    plt.yticks((0,100,10,20,30,40,50,60,70,80,90,100))
    ax.set_xticks([])

    ax.legend(loc="upper right")
    plt.savefig('.\datasetRegioni\consumoCondizionamento\consumoOccasionalmente_o_mai.png', dpi=300)
def datasetSpecificheRiscaldamento():
    data = pd.read_csv('datasetRiscaldamento.csv', sep=';')
    data.columns = ['Regione', 'Mattina', 'Pomeriggio', 'Sera', 'Totale']
    data = data.replace(['..'],'0.0')
    data = data.replace(['....'], 'NULL')
    data = data.replace(['-'], 'NULL')
    conversioneToCsv=data.to_csv('.\datasetLeggibile\datasetRiscaldamento_updated.csv', index = False, sep=';', decimal=',')
def concatenaDatasetRiscaldamento():
    data1 = pd.read_csv('.\datasetLeggibile\datasetRiscaldamento_updated.csv', usecols=['Regione', 'Mattina', 'Pomeriggio', 'Sera'], sep=';', decimal=',')
    data2 = pd.read_csv('.\datasetLeggibile\RegioniInteressate.csv', usecols=['Dotazione_riscaldamento'], sep=';', decimal=',')
    regioni = data1[(data1['Regione']=='Veneto') | (data1['Regione']=='Emilia-Romagna') | (data1['Regione'] == 'Sardegna') | (data1['Regione'] == 'Valle Aosta') | (data1['Regione']=='Bolzano') | (data1['Regione']=='Trentino-Alto Adige')]
    regioni.to_csv('.\datasetLeggibile\datasetCondizionamento_regioniInteressate.csv', sep = ';', decimal=',', index=0)
    data3 = pd.read_csv('.\datasetLeggibile\datasetCondizionamento_regioniInteressate.csv', sep=';', decimal=',')
    a=pd.concat([data3, data2], axis=1)
    a.to_csv('.\datasetLeggibile\datasetConcatenatoRiscaldamento.csv', sep=';', index=0, decimal=',')
def datasetRiscaldamentoElementi():
    df = pd.read_csv('.\datasetLeggibile\datasetConcatenatoRiscaldamento.csv', usecols=['Regione', 'Mattina', 'Pomeriggio', 'Sera'], decimal=',', sep=';', index_col=0)
    mattinaValue = df[['Mattina']].max(axis=1).sort_values(ascending=False).reset_index(name='Mattina')
    pomeriggioValue = df[['Pomeriggio']].min(axis=1).sort_values(ascending=True).reset_index(name='Pomeriggio')
    seraValue = df[['Sera']].min(axis=1).sort_values(ascending=True).reset_index(name='Sera')
    print(mattinaValue, "\n", pomeriggioValue, "\n", seraValue)

    df2 = pd.read_csv('.\datasetLeggibile\datasetConcatenatoRiscaldamento.csv', decimal=',', sep=';')
    ########################### Mattina consumi ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3
    br4 = br3 + 0.3
    br5 = br4 + 0.3
    br6 = br5 + 0.3

    veneto = df2[df2['Regione'] == 'Veneto']
    sardegna = df2[df2['Regione'] == 'Sardegna']
    emilia = df2[df2['Regione'] == 'Emilia-Romagna']
    trentino = df2[df2['Regione'] == 'Trentino-Alto Adige']
    bolzano = df2[df2['Regione'] == 'Bolzano']
    valle_aosta = df2[df2['Regione'] == 'Valle Aosta']
    
    veneto_y = veneto.Mattina
    sardegna_y = sardegna.Mattina
    emilia_y = emilia.Mattina
    trentino_y = trentino.Mattina
    bolzano_y = bolzano.Mattina
    valle_aosta_y = valle_aosta.Mattina

    blu = '#7293cb'
    arancione = '#e1974c'
    verde = '#84ba5b'
    magenta = '#d35e60'
    grigio = '#808585'
    viola = '#9067a7'

    bar1 = plt.bar(br6, valle_aosta_y, color = blu, width = barWidth, edgecolor ='grey', label ="Valle d'Aosta")
    bar2 = plt.bar(br5, emilia_y, color = arancione, width = barWidth, edgecolor ='grey', label ='Emilia Romagna')
    bar3 = plt.bar(br4, bolzano_y, color = verde, width = barWidth, edgecolor ='grey', label = "Bolzano")
    bar4 = plt.bar(br3, trentino_y, color = magenta, width = barWidth, edgecolor ='grey', label ='Trentino Alto Adige')
    bar5 = plt.bar(br2, veneto_y, color = grigio, width = barWidth, edgecolor ='grey', label ='Veneto')
    bar6 = plt.bar(br1, sardegna_y, color = viola, width = barWidth, edgecolor ='grey', label = "Sardegna")
        
    for rect in bar1 + bar2 + bar3 + bar4 + bar5 + bar6:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.1f}%',ha='center',va='bottom')
    
    plt.ylabel('Utilizzo riscaldamento di mattina', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.ylim((0,10))
    plt.yticks((0,10,1,2,3,4,5,6,7,8,9,10))
    ax.set_xticks([])

    ax.legend(loc="upper right")
    plt.savefig('.\datasetRegioni\consumoRiscaldamento\consumoMattina.png', dpi=300)
    ########################### Pomeriggio consumi ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3
    br4 = br3 + 0.3
    br5 = br4 + 0.3
    br6 = br5 + 0.3
    
    veneto_y = veneto.Pomeriggio
    sardegna_y = sardegna.Pomeriggio
    emilia_y = emilia.Pomeriggio
    trentino_y = trentino.Pomeriggio
    bolzano_y = bolzano.Pomeriggio
    valle_aosta_y = valle_aosta.Pomeriggio

    bar1 = plt.bar(br1, trentino_y, color = blu, width = barWidth, edgecolor ='grey', label ="Trentino Alto Adige")
    bar2 = plt.bar(br2, bolzano_y, color = arancione, width = barWidth, edgecolor ='grey', label ='Bolzano')
    bar3 = plt.bar(br3, sardegna_y, color = verde, width = barWidth, edgecolor ='grey', label = "Sardegna")
    bar4 = plt.bar(br4, valle_aosta_y, color = magenta, width = barWidth, edgecolor ='grey', label ='Valle Aosta')
    bar5 = plt.bar(br5, veneto_y, color = grigio, width = barWidth, edgecolor ='grey', label ='Veneto')
    bar6 = plt.bar(br6, emilia_y, color = viola, width = barWidth, edgecolor ='grey', label = "Emilia Romagna")
        
    for rect in bar1 + bar2 + bar3 + bar4 + bar5 + bar6:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.1f}%',ha='center',va='bottom')
    
    plt.ylabel('Utilizzo riscaldamento di pomeriggio', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.ylim((0,10))
    plt.yticks((0,10,1,2,3,4,5,6,7,8,9,10))
    ax.set_xticks([])

    ax.legend(loc="upper right")
    plt.savefig('.\datasetRegioni\consumoRiscaldamento\consumoPomeriggio.png', dpi=300)
    ########################### Sera consumi ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3
    br4 = br3 + 0.3
    br5 = br4 + 0.3
    br6 = br5 + 0.3

    veneto_y = veneto.Sera
    sardegna_y = sardegna.Sera
    emilia_y = emilia.Sera
    trentino_y = trentino.Sera
    bolzano_y = bolzano.Sera
    valle_aosta_y = valle_aosta.Sera

    bar1 = plt.bar(br1, sardegna_y, color = blu, width = barWidth, edgecolor ='grey', label = "Sardegna")
    bar2 = plt.bar(br2, bolzano_y, color = arancione, width = barWidth, edgecolor ='grey', label ='Bolzano')
    bar3 = plt.bar(br3, trentino_y, color = verde, width = barWidth, edgecolor ='grey', label = "Trentino Alto Adige")
    bar4 = plt.bar(br4, veneto_y, color = magenta, width = barWidth, edgecolor ='grey', label ='Veneto')
    bar5 = plt.bar(br5, valle_aosta_y, color = grigio, width = barWidth, edgecolor ='grey', label ="Valle d'Aosta")
    bar6 = plt.bar(br6, emilia_y, color = viola, width = barWidth, edgecolor ='grey', label = "Emilia Romagna")
        
    for rect in bar1 + bar2 + bar3 + bar4 + bar5 + bar6:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.1f}%',ha='center',va='bottom')
    
    plt.ylabel('Utilizzo riscaldamento di sera', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.ylim((0,10))
    plt.yticks((0,10,1,2,3,4,5,6,7,8,9,10))
    ax.set_xticks([])

    ax.legend(loc="upper right")
    plt.savefig('.\datasetRegioni\consumoRiscaldamento\consumoSera.png', dpi=300)
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 
        for row in csvReader: 
            jsonArray.append(row)
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

csvFilePath = r'.\datasetToJSON\datasetRiscaldamento.csv'
jsonFilePath = r'.\datasetToJSON\datasetRiscaldamento_iniziale.json'
csv_to_json(csvFilePath, jsonFilePath)