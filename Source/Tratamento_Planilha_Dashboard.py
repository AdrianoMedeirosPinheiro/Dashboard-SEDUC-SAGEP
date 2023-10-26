import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
import pytz

# Substitua 'seuarquivo.csv' pelo caminho para o seu arquivo CSV
caminho_arquivo = 'Planilhas Nao Tratadas\\bisagep.csv'

# Use a função read_csv do pandas para importar o arquivo CSV
df = pd.read_csv(caminho_arquivo, delimiter=';')

# Defina as condições e os valores correspondentes
conditions = [
    (df['Destino'] == 'SEDUC » Aposentadoria Novo » SE01'),
    (df['Destino'] == 'SEDUC » CADDEP - COORDENADORIA DE AVALIAÇÃO DE DESEMPENHO E DESENVOLVIMENTO PROFISSIONAL » SE01'),
    (df['Destino'] == 'SEDUC » CAPO/Abono - CAPO/Abono Permanência » SE01'),
    (df['Destino'] == 'SEDUC » CAPO/Abono Permanência » SE01'),
    (df['Destino'] == 'SEDUC » CAPO/AN - Aposentadoria Novo » SE01'),
    (df['Destino'] == 'SEDUC » CAPO/Judicial - CAPO Aposentadoria Judicial » SE01'),
    (df['Destino'] == 'SEDUC » CAPO/Triagem - Capo Triagem » SE01'),
    (df['Destino'] == 'SEDUC » CCM - COORDENADORIA DE CONTROLE E MOVIMENTAÇÃO » SE01'),
    (df['Destino'] == 'SEDUC » CCM Averbação » SE01'),
    (df['Destino'] == 'SEDUC » CCM Certidões » SE01'),
    (df['Destino'] == 'SEDUC » CCM DESIG/SUBS. - CCM Designação e Substituição » SE01'),
    (df['Destino'] == 'SEDUC » CCM Férias » SE01'),
    (df['Destino'] == 'SEDUC » CCM JUDICIAL PECUNIA » SE01'),
    (df['Destino'] == 'SEDUC » CCM Licença Especial » SE01'),
    (df['Destino'] == 'SEDUC » CCM- Pecúnia » SE01'),
    (df['Destino'] == 'SEDUC » CCM/Certidões - CCM Certidões » SE01'),
    (df['Destino'] == 'SEDUC » CCM/Férias - CCM Férias » SE01'),
    (df['Destino'] == 'SEDUC » CCM/Férias/Ass. - CCM FÉRIAS/ASSINATURA » SE01'),
    (df['Destino'] == 'SEDUC » CCM/JUD/Pecunia - CCM JUDICIAL PECUNIA » SE01'),
    (df['Destino'] == 'SEDUC » CCM/LicAssinar - CCM - Licenças Assinatura » SE01'),
    (df['Destino'] == 'SEDUC » CCM/LicESp - CCM Licença Especial » SE01'),
    (df['Destino'] == 'SEDUC » CCM/Pecúnia - CCM- Pecúnia » SE01'),
    (df['Destino'] == 'SEDUC » Cessão e Revogação Assinatura CCM » SE01'),
    (df['Destino'] == 'SEDUC » CFOP - COORDENADORIA DE FOLHA DE PAGAMENTO » SE01'),
    (df['Destino'] == 'SEDUC » COORDENADORIA DE CONTROLE E MOVIMENTAÇÃO » SE01'),
    (df['Destino'] == 'SEDUC » COORDENADORIA DE FOLHA DE PAGAMENTO » SE01'),
    (df['Destino'] == 'SEDUC » COORDENADORIA DE ORGANIZAÇÃO DE REDE » SE01'),
    (df['Destino'] == 'SEDUC » COORDENADORIA DE PLANEJAMENTO E SELEÇÃO » SE01'),
    (df['Destino'] == 'SEDUC » COORDENADORIA DE VALORIZAÇÃO E ASSISTÊNCIA AOS SERVIDORES » SE01'),
    (df['Destino'] == 'SEDUC » COR - COORDENADORIA DE ORGANIZAÇÃO DE REDE » SE01'),
    (df['Destino'] == 'SEDUC » COR/CODIGO - COR CODIGO » SE01'),
    (df['Destino'] == 'SEDUC » COR/RETROATIVO - COR Retroativo » SE01'),
    (df['Destino'] == 'SEDUC » CPS - COORDENADORIA DE PLANEJAMENTO E SELEÇÃO » SE01'),
    (df['Destino'] == 'SEDUC » CVAS - COORDENADORIA DE VALORIZAÇÃO E ASSISTÊNCIA AOS SERVIDORES » SE01'),
    (df['Destino'] == 'SEDUC » CVAS-Assist. - Coordenadoria de Assistência » SE01'),
    (df['Destino'] == 'SEDUC » CVAS-LA/Assina - CVAS Licença Aprimoramento Assinatura » SE01'),
    (df['Destino'] == 'SEDUC » DESIGASSINATURA - CCM Designação e Dispensa Assinatura » SE01'),
    (df['Destino'] == 'SEDUC » DIOP - DIRETORIA DE ORGANIZAÇÃO DE PESSOAL » SE01'),
    (df['Destino'] == 'SEDUC » DIRETORIA DE ORGANIZAÇÃO DE PESSOAL » SE01'),
    (df['Destino'] == 'SEDUC » SAGEP - SECRETARIA ADJUNTA DE GESTÃO DE PESSOAS » SE01'),
    (df['Destino'] == 'SEDUC » SAGEP Cessão e Redistribuição » SE01'),
    (df['Destino'] == 'SEDUC » SAGEP Contrato Temporário PSS » SE01'),
    (df['Destino'] == 'SEDUC » SECRETARIA ADJUNTA DE GESTÃO DE PESSOAS » SE01')
]

values = [
    'DIOP CAPO', 'DIPSE CADDEP', 'DIOP CAPO', 'DIOP CAPO', 'DIOP CAPO', 'DIOP CAPO', 'DIOP CAPO',
    'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM',
    'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM',
    'DIOP CCM', 'DIFOB CFOP', 'DIOP CCM', 'DIFOB CFOP',
    'DIOP COR', 'DIPSE CPS', 'DIFOB CVAS', 'DIOP COR', 'DIOP COR', 'DIOP COR',
    'DIPSE CPS', 'DIFOB CVAS', 'DIFOB CVAS', 'DIFOB CVAS', 'DIOP CCM',
    'DIOP Diretoria', 'DIOP', 'SAGEP Gabinete', 'SAGEP Gabinete', 'DIPSE CPS', 'SAGEP Gabinete'
]

# Crie a nova coluna 'Setor Traduzido' com base nas condições e valores
df['Setor Traduzido'] = np.select(conditions, values, default='')

# Crie a coluna 'Pertence SAGEP' e defina os valores como 'Sim' onde as condições se aplicam
#df['Pertence SAGEP'] = np.where(df['Setor Traduzido'] != '', 'Sim', '')

# Crie a coluna 'Pertence SAGEP' e defina os valores como 'Sim' onde as condições se aplicam e 'Não' onde não se aplicam
df['Pertence SAGEP'] = np.where(df['Setor Traduzido'] != '', 'Sim', 'Não')

# Filtrar o DataFrame para incluir apenas as linhas em que 'Pertence SAGEP' é igual a 'Sim' ou 'Não'
df_filtrado = df[(df['Pertence SAGEP'] == 'Sim') | (df['Pertence SAGEP'] == 'Não')].dropna(subset=['N° Protocolo'])

# Use o método to_datetime para converter a coluna para o tipo datetime
df['Data envio'] = pd.to_datetime(df['Data envio'], format='%d/%m/%Y')
df['Data recebimento'] = pd.to_datetime(df['Data recebimento'], format='%d/%m/%Y')

# Ordene o DataFrame pelo N° Protocolo e Data envio
df_filtrado.sort_values(by=['N° Protocolo', 'Número'], inplace=True)

# Redefina o índice do DataFrame
df_filtrado.reset_index(drop=True, inplace=True)

# Crie uma nova coluna 'tempo de resposta' preenchida com valores vazios
df_filtrado['Tempo de resposta'] = None

# Converta a coluna 'Data envio' para o tipo datetime, caso ainda não esteja
df_filtrado['Data envio'] = pd.to_datetime(df_filtrado['Data envio'], format='%d/%m/%Y')

# Calcule o tempo de resposta com base na próxima linha com o mesmo protocolo
for index, row in df_filtrado.iterrows():
    if index < len(df_filtrado) - 1 and df_filtrado.at[index, 'N° Protocolo'] == df_filtrado.at[index + 1, 'N° Protocolo']:
        time_difference = df_filtrado.at[index + 1, 'Data envio'] - row['Data envio']
        df_filtrado.at[index, 'Tempo de resposta'] = time_difference.days

# Passo 1: Identificar linhas com 'tempo de resposta' vazias
linhas_com_tempo_vazio = df_filtrado['Tempo de resposta'].isnull()

# Define o fuso horário de Brasília
fuso_horario_brasilia = pytz.timezone('America/Sao_Paulo')

# Obtém a data e hora atual em Brasília
data_atual_utc = datetime.now()
data_atual_brasilia = data_atual_utc.astimezone(fuso_horario_brasilia)

# Remova o fuso horário da data e hora de Brasília
data_atual_brasilia_sem_tz = data_atual_brasilia.replace(tzinfo=None)

# Passo 3: Calcular a diferença entre a data atual e 'Data envio' para as linhas identificadas
#df_filtrado['Tempo parado'] = data_atual - df_filtrado.loc[linhas_com_tempo_vazio, 'Data envio']

# Define um período de tempo de dois dias
dois_dias = timedelta(days=2)

# Subtrai dois dias da diferença entre as datas
df_filtrado['Tempo parado'] = ((data_atual_brasilia_sem_tz - df_filtrado.loc[linhas_com_tempo_vazio, 'Data envio'])).dt.days

# Aplicar a função abs() apenas aos valores não nulos na coluna "Tempo de resposta"
df_filtrado['Tempo de resposta'] = df_filtrado['Tempo de resposta'].apply(lambda x: abs(x) if x is not None else None)

# Carregando o dataframe original
df = df_filtrado

# Filtrando para remover valores nulos na coluna 'Tempo de resposta' e onde 'Pertence SAGEP' seja igual a 'Sim'
df = df[(df['Tempo de resposta'].notnull()) & (df['Pertence SAGEP'] == 'Sim')]

# Agrupando por 'Setor Traduzido' e calculando a média de 'Tempo de resposta'
df_resumo = df.groupby('Setor Traduzido')['Tempo de resposta'].mean().reset_index()

# Renomeando coluna
df_resumo = df_resumo.rename(columns={'Tempo de resposta': 'Tempo médio de resposta'})

# Crie o DataFrame df_criticos com os valores da coluna 'Tempo parado' maiores que 2
df_criticos = df_filtrado[df_filtrado['Tempo parado'] > 2]

# 1. Comece com o DataFrame 'df_filtrado'
df = df_filtrado.copy()

# 2. Converta a coluna 'Número' para o tipo int
df['Número'] = df['Número'].astype(int)

# 3. Ordene o DataFrame pelo número do estágio e pelo número do protocolo
df = df.sort_values(by=['N° Protocolo', 'Número'])

# 4. Encontre o número de estágio mais alto para cada protocolo
max_stage = df.groupby('N° Protocolo')['Número'].max()

# 5. Crie a coluna 'Solucionado' e inicialize-a com valores nulos (None)
df['Solucionado'] = None

# 6. Atualize 'Solucionado' com base nas condições especificadas apenas para o último estágio de cada protocolo
for protocolo, max_stage_value in max_stage.items():
    last_stage_row = df[(df['N° Protocolo'] == protocolo) & (df['Número'] == max_stage_value)]
    if len(last_stage_row) > 0:
        if last_stage_row.iloc[0]['Pertence SAGEP'] == 'Não':
            df.loc[last_stage_row.index, 'Solucionado'] = 'Sim'
        else:
            df.loc[last_stage_row.index, 'Solucionado'] = 'Não'
        
df.to_excel("Planilhas Tratadas\\Planilha_Tratada_Tramitação.xlsx", index=False)
df_criticos.to_excel("Planilhas Tratadas\\Planilha_Tratada_Processos_Criticos.xlsx", index=False)
df_resumo.to_excel("Planilhas Tratadas\\Planilha_Tratada_Tempo_Medio_Resposta.xlsx", index=False)