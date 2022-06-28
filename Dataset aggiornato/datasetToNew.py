from curses import use_default_colors
import matplotlib.pyplot as plt, pylab, pandas as pd, matplotlib.ticker, csv, numpy as np

########################### Utilizzo questa funzione per avere un file csv più leggibile ###########################
def datasetConsumi():
    data = pd.read_csv('datasetIniziale.csv', decimal=',')
    data.columns=["Regione", "Dotazione riscaldamento", "Dotazione acqua calda", "Dotazione condizionamento", "Riscaldamento e acqua calda coincidenti", "Riscaldamento e condizionamento coincidenti", "Piu tipi di dotazioni per il riscaldamento", "Piu tipi di dotazioni per acqua calda", "Piu tipi di dotazioni per il condizionamento"]
    data = data.replace(['..'],'0.0')
    data = data.replace(['....'], 'NULL')
    data = data.replace(['-'], 'NULL')
    data = data.astype({"Dotazione riscaldamento": float, "Dotazione acqua calda": float, "Dotazione condizionamento": float, "Riscaldamento e acqua calda coincidenti": float, "Riscaldamento e condizionamento coincidenti": float, "Piu tipi di dotazioni per il riscaldamento": float, "Piu tipi di dotazioni per acqua calda": float, "Piu tipi di dotazioni per il condizionamento": float})
    conversioneToCsv=data.to_csv('datasetIniziale_updated.csv', columns=('Regione', 'Dotazione riscaldamento', 'Dotazione acqua calda', 'Dotazione condizionamento', 'Riscaldamento e acqua calda coincidenti', 'Riscaldamento e condizionamento coincidenti', 'Piu tipi di dotazioni per il riscaldamento', 'Piu tipi di dotazioni per acqua calda', 'Piu tipi di dotazioni per il condizionamento'), index=False, sep=';', decimal=',')

########################### Utilizzo questa funzione per avere le regioni con Dotazione Riscaldamento, Dotazione Acqua Calda e Dotazione Condizionamento più alti (basandomi sul valore di Dotazione Riscaldamento) ###########################
def valoreMassimo():
    df = pd.read_csv('datasetIniziale.csv', usecols=['Regione','Famiglie dotate di riscaldamento della abitazione', 'Famiglie dotate di acqua calda', 'Famiglie dotate di condizionamento'])
    df.columns=["Regione", "Dotazione_riscaldamento", "Dotazione_acqua_calda", "Dotazione_condizionamento"]
    ########################### Verifico i valori più grandi, riga per riga (basandomi sulla Dotazione_riscaldamento) ###########################
    dr = df.loc[df['Dotazione_riscaldamento'].idxmax()]
    dac = df.loc[df['Dotazione_acqua_calda'].idxmax()]
    dc = df.loc[df['Dotazione_condizionamento'].idxmax()]
    print(dr, "\n", dac, "\n", dc)

    umbria = df[(df['Regione']=='Umbria')]
    lombardia = df[(df['Regione']=='Lombardia')]
    veneto = df[(df['Regione']=='Veneto')]
    ########################### Dotazione Riscaldamento ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3

    umbria_y = umbria.Dotazione_riscaldamento
    lombardia_y = lombardia.Dotazione_riscaldamento
    veneto_y = veneto.Dotazione_riscaldamento

    bar1 = plt.bar(br1, umbria_y, color ='#50A3A4', width = barWidth, edgecolor ='grey', label ='Umbria')
    bar2 = plt.bar(br2, lombardia_y, color ='#FCAF38', width = barWidth, edgecolor ='grey', label ='Lombardia')
    bar3 = plt.bar(br3, veneto_y, color ='#F95335', width = barWidth, edgecolor ='grey', label = "Veneto")
    
    for rect in bar1 + bar2 + bar3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.0f}',ha='center',va='bottom')

    plt.xlabel('Regioni', fontweight ='bold', fontsize = 15)
    plt.ylabel('Dotazione riscaldamento', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.yticks((0,300,0,30,60,90,120,150,180,210,240,270,300))
    ax.set_xticks([])

    plt.legend()
    plt.savefig('.\maxValori\dotazioneRiscaldamento.png', dpi=300)
    ########################### Dotazione Acqua Calda ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3

    umbria_y = umbria.Dotazione_acqua_calda
    lombardia_y = lombardia.Dotazione_acqua_calda
    veneto_y = veneto.Dotazione_acqua_calda

    bar1 = plt.bar(br1, umbria_y, color ='#50A3A4', width = barWidth, edgecolor ='grey', label ='Umbria')
    bar2 = plt.bar(br2, lombardia_y, color ='#FCAF38', width = barWidth, edgecolor ='grey', label ='Lombardia')
    bar3 = plt.bar(br3, veneto_y, color ='#F95335', width = barWidth, edgecolor ='grey', label = "Veneto")
    
    for rect in bar1 + bar2 + bar3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.0f}',ha='center',va='bottom')
    
    plt.xlabel('Regioni', fontweight ='bold', fontsize = 15)
    plt.ylabel('Dotazione acqua calda', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.yticks((0,300,0,30,60,90,120,150,180,210,240,270,300))
    ax.set_xticks([])

    plt.legend()
    plt.savefig('.\maxValori\dotazioneAcquaCalda.png', dpi=300)
    ########################### Dotazione Condizionamento ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3

    umbria_y = umbria.Dotazione_condizionamento
    lombardia_y = lombardia.Dotazione_condizionamento
    veneto_y = veneto.Dotazione_condizionamento

    bar1 = plt.bar(br1, umbria_y, color ='#50A3A4', width = barWidth, edgecolor ='grey', label ='Umbria')
    bar2 = plt.bar(br2, lombardia_y, color ='#FCAF38', width = barWidth, edgecolor ='grey', label ='Lombardia')
    bar3 = plt.bar(br3, veneto_y, color ='#F95335', width = barWidth, edgecolor ='grey', label = "Veneto")
        
    for rect in bar1 + bar2 + bar3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.0f}',ha='center',va='bottom')
    
    plt.xlabel('Regioni', fontweight ='bold', fontsize = 15)
    plt.ylabel('Dotazione condizionamento', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.yticks((0,300,0,30,60,90,120,150,180,210,240,270,300))
    ax.set_xticks([])

    plt.legend()
    plt.savefig('.\maxValori\dotazioneCondizionamento.png', dpi=300)
    ########################### Le informazioni ottenute le scrivo su un file csv ###########################
    with open('.\maxValori\maxValori.csv', 'w', newline = "") as f:
        writer = csv.writer(f, delimiter = ';')
        writer.writerow(df.columns)
        writer.writerow(dr)
        writer.writerow(dac)
        writer.writerow(dc)

########################### Utilizzo questa funzione per avere le regioni con Dotazione Riscaldamento, Dotazione Acqua Calda e Dotazione Condizionamento più bassi (basandomi sul valore di Dotazione Riscaldamento) ###########################
def valoreMinimo():
    df = pd.read_csv('datasetIniziale.csv', usecols=['Regione','Famiglie dotate di riscaldamento della abitazione', 'Famiglie dotate di acqua calda', 'Famiglie dotate di condizionamento'])
    df.columns=["Regione", "Dotazione_riscaldamento", "Dotazione_acqua_calda", "Dotazione_condizionamento"]
    ########################### Verifico i valori più piccoli, riga per riga (basandomi sulla Dotazione_riscaldamento) ###########################
    dr = df.loc[df['Dotazione_riscaldamento'].idxmin()]
    dac = df.loc[df['Dotazione_acqua_calda'].idxmin()]
    dc = df.loc[df['Dotazione_condizionamento'].idxmin()]
    print(dr, "\n", dac, "\n", dc)

    sicilia = df[(df['Regione']=='Sicilia')]
    campania = df[(df['Regione']=='Campania')]
    valle_aosta = df[(df['Regione']=='Valle Aosta')]
    ########################### Dotazione Riscaldamento ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3

    sicilia_y = sicilia.Dotazione_riscaldamento
    campania_y = campania.Dotazione_riscaldamento
    valle_aosta_y = valle_aosta.Dotazione_riscaldamento

    bar1 = plt.bar(br1, sicilia_y, color ='#50A3A4', width = barWidth, edgecolor ='grey', label ='Sicilia')
    bar2 = plt.bar(br2, campania_y, color ='#FCAF38', width = barWidth, edgecolor ='grey', label ='Campania')
    bar3 = plt.bar(br3, valle_aosta_y, color ='#F95335', width = barWidth, edgecolor ='grey', label = "Valle d'Aosta")
        
    for rect in bar1 + bar2 + bar3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.0f}',ha='center',va='bottom')
    
    plt.xlabel('Regioni', fontweight ='bold', fontsize = 15)
    plt.ylabel('Dotazione riscaldamento', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.yticks((0,300,0,30,60,90,120,150,180,210,240,270,300))
    ax.set_xticks([])

    plt.legend()
    plt.savefig('.\minValori\dotazioneRiscaldamento.png', dpi=300)
    ########################### Dotazione Acqua Calda ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3
    sicilia_y = sicilia.Dotazione_acqua_calda
    campania_y = campania.Dotazione_acqua_calda
    valle_aosta_y = valle_aosta.Dotazione_acqua_calda

    bar1 = plt.bar(br1, sicilia_y, color ='#50A3A4', width = barWidth, edgecolor ='grey', label ='Sicilia')
    bar2 = plt.bar(br2, campania_y, color ='#FCAF38', width = barWidth, edgecolor ='grey', label ='Campania')
    bar3 = plt.bar(br3, valle_aosta_y, color ='#F95335', width = barWidth, edgecolor ='grey', label = "Valle d'Aosta")
        
    for rect in bar1 + bar2 + bar3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.0f}',ha='center',va='bottom')
    
    plt.xlabel('Regioni', fontweight ='bold', fontsize = 15)
    plt.ylabel('Dotazione acqua calda', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.yticks((0,300,0,30,60,90,120,150,180,210,240,270,300))
    ax.set_xticks([])

    plt.legend()
    plt.savefig('.\minValori\dotazioneAcquaCalda.png', dpi=300)
    ########################### Dotazione Condizionamento ###########################
    barWidth = 0.15
    fig, ax = plt.subplots(figsize = (10, 7))
    br1 = 0.3
    br2 = br1 + 0.3
    br3 = br2 + 0.3
    sicilia_y = sicilia.Dotazione_condizionamento
    campania_y = campania.Dotazione_condizionamento
    valle_aosta_y = valle_aosta.Dotazione_condizionamento

    bar1 = plt.bar(br1, sicilia_y, color ='#50A3A4', width = barWidth, edgecolor ='grey', label ='Sicilia')
    bar2 = plt.bar(br2, campania_y, color ='#FCAF38', width = barWidth, edgecolor ='grey', label ='Campania')
    bar3 = plt.bar(br3, valle_aosta_y, color ='#F95335', width = barWidth, edgecolor ='grey', label = "Valle d'Aosta")
        
    for rect in bar1 + bar2 + bar3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, f'{height:.0f}',ha='center',va='bottom')
    
    plt.xlabel('Regioni', fontweight ='bold', fontsize = 15)
    plt.ylabel('Dotazione condizionamento', fontweight ='bold', fontsize = 15)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.yticks((0,300,0,30,60,90,120,150,180,210,240,270,300))
    ax.set_xticks([])

    plt.legend()
    plt.savefig('.\minValori\dotazioneCondizionamento.png', dpi=300)
    ########################### Le informazioni ottenute le scrivo su un file csv ###########################
    with open('.\minValori\minValori.csv', 'w', newline = "") as f:
        writer = csv.writer(f, delimiter = ';')
        writer.writerow(df.columns)
        writer.writerow(dr)
        writer.writerow(dac)
        writer.writerow(dc)

########################### Working in progress ###########################
def datasetTipologie():
    data = pd.read_csv('dataset2.csv', decimal=',')
    data.columns = ["Regione", "Imp. centr. risc.", "Imp. aut. risc.", "App. singoli risc.", "Imp. centr. acqua", "Imp. aut. acqua", "App. singoli acqua", "Imp. centr. o aut. cond.", "Cond. solo freddo", "Cond. caldo/freddo", "Tot. app. singoli"]
    data = data.replace(['..'],'0.0')
    data = data.replace(['....'], 'NULL')
    data = data.replace(['-'], 'NULL')
    data.astype({"Imp. centr. risc.": float, "Imp. aut. risc.": float, "App. singoli risc.": float, "Imp. centr. acqua": float, "Imp. aut. acqua": float, "App. singoli acqua": float, "Imp. centr. o aut. cond.": float, "Cond. solo freddo": float, "Cond. caldo/freddo": float, "Tot. app. singoli": float})
    conversioneToCsv=data.to_csv('datasetAggiornato2.csv', columns=("Regione", "Imp. centr. risc.", "Imp. aut. risc.", "App. singoli risc.", "Imp. centr. acqua", "Imp. aut. acqua", "App. singoli acqua", "Imp. centr. o aut. cond.", "Cond. solo freddo", "Cond. caldo/freddo", "Tot. app. singoli"), index=False, sep=';')