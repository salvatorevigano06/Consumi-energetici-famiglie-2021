import pandas as pd
import csv

def nuovoDataset():
    data = pd.read_csv('.\Dataset aggiornato\dataset.csv')
    data.columns=["Regione", "Dotazione riscaldamento", "Dotazione acqua calda", "Dotazione condizionamento", "Riscaldamento e acqua calda coincidenti", "Riscaldamento e condizionamento coincidenti", "Piu tipi di dotazioni per il riscaldamento", "Piu tipi di dotazioni per acqua calda", "Piu tipi di dotazioni per il condizionamento"]
    data.sort_values(['Regione', 'Dotazione riscaldamento', 'Dotazione acqua calda', 'Dotazione condizionamento', 'Riscaldamento e acqua calda coincidenti', 'Riscaldamento e condizionamento coincidenti', 'Piu tipi di dotazioni per il riscaldamento', 'Piu tipi di dotazioni per acqua calda', 'Piu tipi di dotazioni per il condizionamento'], ascending=True, inplace=True)
    data = data.replace(['..'],'0.0')
    data = data.replace(['....'], 'NULL')
    data = data.replace(['-'], 'NULL')
    conversioneToCsv=data.to_csv('datasetAggiornato.csv', columns=('Regione', 'Dotazione riscaldamento', 'Dotazione acqua calda', 'Dotazione condizionamento', 'Riscaldamento e acqua calda coincidenti', 'Riscaldamento e condizionamento coincidenti', 'Piu tipi di dotazioni per il riscaldamento', 'Piu tipi di dotazioni per acqua calda', 'Piu tipi di dotazioni per il condizionamento'), index=False, sep=';')
   
def valoreMassimo():
    df = pd.read_csv('dataset.csv', usecols=['Regione','Famiglie dotate di riscaldamento della abitazione', 'Famiglie dotate di acqua calda', 'Famiglie dotate di condizionamento'])
    df.columns=["Regione", "Dotazione riscaldamento", "Dotazione acqua calda", "Dotazione condizionamento"]
    dr = df.loc[df['Dotazione riscaldamento'].idxmax()]
    dac = df.loc[df['Dotazione acqua calda'].idxmax()]
    dc = df.loc[df['Dotazione condizionamento'].idxmax()]
    print(dr, "\n", dac, "\n", dc)
    
    with open('valoriMassimi.csv', 'w', newline = "") as f:
        writer = csv.writer(f, delimiter = ';')
        writer.writerow(df.columns)
        writer.writerow(dr)
        writer.writerow(dac)
        writer.writerow(dc)

valoreMassimo()