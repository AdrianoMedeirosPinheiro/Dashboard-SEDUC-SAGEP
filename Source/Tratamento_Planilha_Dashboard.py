import pandas as pd
import numpy as np
from datetime import datetime

# Substitua 'seuarquivo.csv' pelo caminho para o seu arquivo CSV
caminho_arquivo = 'Planilhas Nao Tratadas\\bisagep.csv'

# Use a função read_csv do pandas para importar o arquivo CSV
df = pd.read_csv(caminho_arquivo, delimiter=';')

# Agora você pode trabalhar com os dados no dataframe, por exemplo, exibindo as primeiras linhas
df.head()

#'''
df = df.drop("Setor Traduzido", axis=1)
df = df.drop("SAGEP", axis=1)
df = df.drop("Tempo de resposta", axis=1)
df = df.drop("Tempo parado", axis=1)
df.head()
#'''

# Defina as condições e os valores correspondentes
conditions = [
    (df['Origem'] == 'SEDUC » Aposentadoria Novo » SE01'),
    (df['Origem'] == 'SEDUC » CADDEP - COORDENADORIA DE AVALIAÇÃO DE DESEMPENHO E DESENVOLVIMENTO PROFISSIONAL » SE01'),
    (df['Origem'] == 'SEDUC » CAPO/Abono - CAPO/Abono Permanência » SE01'),
    (df['Origem'] == 'SEDUC » CAPO/Abono Permanência » SE01'),
    (df['Origem'] == 'SEDUC » CAPO/AN - Aposentadoria Novo » SE01'),
    (df['Origem'] == 'SEDUC » CAPO/Judicial - CAPO Aposentadoria Judicial » SE01'),
    (df['Origem'] == 'SEDUC » CAPO/Triagem - Capo Triagem » SE01'),
    (df['Origem'] == 'SEDUC » CCM - COORDENADORIA DE CONTROLE E MOVIMENTAÇÃO » SE01'),
    (df['Origem'] == 'SEDUC » CCM Averbação » SE01'),
    (df['Origem'] == 'SEDUC » CCM Certidões » SE01'),
    (df['Origem'] == 'SEDUC » CCM DESIG/SUBS. - CCM Designação e Substituição » SE01'),
    (df['Origem'] == 'SEDUC » CCM Férias » SE01'),
    (df['Origem'] == 'SEDUC » CCM JUDICIAL PECUNIA » SE01'),
    (df['Origem'] == 'SEDUC » CCM Licença Especial » SE01'),
    (df['Origem'] == 'SEDUC » CCM- Pecúnia » SE01'),
    (df['Origem'] == 'SEDUC » CCM/Certidões - CCM Certidões » SE01'),
    (df['Origem'] == 'SEDUC » CCM/Férias - CCM Férias » SE01'),
    (df['Origem'] == 'SEDUC » CCM/Férias/Ass. - CCM FÉRIAS/ASSINATURA » SE01'),
    (df['Origem'] == 'SEDUC » CCM/JUD/Pecunia - CCM JUDICIAL PECUNIA » SE01'),
    (df['Origem'] == 'SEDUC » CCM/LicAssinar - CCM - Licenças Assinatura » SE01'),
    (df['Origem'] == 'SEDUC » CCM/LicESp - CCM Licença Especial » SE01'),
    (df['Origem'] == 'SEDUC » CCM/Pecúnia - CCM- Pecúnia » SE01'),
    (df['Origem'] == 'SEDUC » Cessão e Revogação Assinatura CCM » SE01'),
    (df['Origem'] == 'SEDUC » CFOP - COORDENADORIA DE FOLHA DE PAGAMENTO » SE01'),
    (df['Origem'] == 'SEDUC » COORDENADORIA DE CONTROLE E MOVIMENTAÇÃO » SE01'),
    (df['Origem'] == 'SEDUC » COORDENADORIA DE FOLHA DE PAGAMENTO » SE01'),
    (df['Origem'] == 'SEDUC » COORDENADORIA DE ORGANIZAÇÃO DE REDE » SE01'),
    (df['Origem'] == 'SEDUC » COORDENADORIA DE PLANEJAMENTO E SELEÇÃO » SE01'),
    (df['Origem'] == 'SEDUC » COORDENADORIA DE VALORIZAÇÃO E ASSISTÊNCIA AOS SERVIDORES » SE01'),
    (df['Origem'] == 'SEDUC » COR - COORDENADORIA DE ORGANIZAÇÃO DE REDE » SE01'),
    (df['Origem'] == 'SEDUC » COR/CODIGO - COR CODIGO » SE01'),
    (df['Origem'] == 'SEDUC » COR/RETROATIVO - COR Retroativo » SE01'),
    (df['Origem'] == 'SEDUC » CPS - COORDENADORIA DE PLANEJAMENTO E SELEÇÃO » SE01'),
    (df['Origem'] == 'SEDUC » CVAS - COORDENADORIA DE VALORIZAÇÃO E ASSISTÊNCIA AOS SERVIDORES » SE01'),
    (df['Origem'] == 'SEDUC » CVAS-Assist. - Coordenadoria de Assistência » SE01'),
    (df['Origem'] == 'SEDUC » CVAS-LA/Assina - CVAS Licença Aprimoramento Assinatura » SE01'),
    (df['Origem'] == 'SEDUC » DESIGASSINATURA - CCM Designação e Dispensa Assinatura » SE01'),
    (df['Origem'] == 'SEDUC » DIOP - DIRETORIA DE ORGANIZAÇÃO DE PESSOAL » SE01'),
    (df['Origem'] == 'SEDUC » DIRETORIA DE ORGANIZAÇÃO DE PESSOAL » SE01'),
    (df['Origem'] == 'SEDUC » SAGEP - SECRETARIA ADJUNTA DE GESTÃO DE PESSOAS » SE01'),
    (df['Origem'] == 'SEDUC » SAGEP Cessão e Redistribuição » SE01'),
    (df['Origem'] == 'SEDUC » SAGEP Contrato Temporário PSS » SE01'),
    (df['Origem'] == 'SEDUC » SECRETARIA ADJUNTA DE GESTÃO DE PESSOAS » SE01')
]

values = [
    'DIOP CAPO', 'DIPSE CADDEP', 'DIOP CAPO', 'DIOP CAPO', 'DIOP CAPO', 'DIOP CAPO', 'DIOP CAPO',
    'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM',
    'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM', 'DIOP CCM',
    'DIOP CAPO', 'DIFOB CFOP', 'DIOP CCM', 'DIFOB CFOP',
    'DIOP COR', 'DIPSE CPS', 'DIFOB CVAS', 'DIOP COR', 'DIOP COR', 'DIOP COR',
    'DIPSE CPS', 'DIFOB CVAS', 'DIFOB CVAS', 'DIFOB CVAS', 'DIOP CCM',
    'DIOP Diretoria', 'DIOP', 'SAGEP Gabinete', 'SAGEP Gabinete', 'DIPSE CPS', 'SAGEP Gabinete'
]

# Crie a nova coluna 'Setor Traduzido' com base nas condições e valores
df['Setor Traduzido'] = np.select(conditions, values, default='')

# Crie a coluna 'Pertence SAGEP' e defina os valores como 'Sim' onde as condições se aplicam
df['Pertence SAGEP'] = np.where(df['Setor Traduzido'] != '', 'Sim', '')

# Filtrar o DataFrame para incluir apenas as linhas em que 'Pertence SAGEP' é igual a 'Sim'
df_filtrado = df[df['Pertence SAGEP'] == 'Sim']

# Use o método to_datetime para converter a coluna para o tipo datetime
df['Data envio'] = pd.to_datetime(df['Data envio'], format='%d/%m/%Y')
df['Data recebimento'] = pd.to_datetime(df['Data recebimento'], format='%d/%m/%Y')

# Ordene o DataFrame pelo N° Protocolo e Data envio
df_filtrado.sort_values(by=['N° Protocolo', 'Data envio'], inplace=True)

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

# Passo 2: Calcular a data atual
data_atual = datetime.now()

# Passo 3: Calcular a diferença entre a data atual e 'Data envio' para as linhas identificadas
#df_filtrado['Tempo parado'] = data_atual - df_filtrado.loc[linhas_com_tempo_vazio, 'Data envio']

# Converter a diferença em dias para um número inteiro
df_filtrado['Tempo parado'] = (data_atual - df_filtrado.loc[linhas_com_tempo_vazio, 'Data envio']).dt.days

# Aplicar a função abs() apenas aos valores não nulos na coluna "Tempo de resposta"
df_filtrado['Tempo de resposta'] = df_filtrado['Tempo de resposta'].apply(lambda x: abs(x) if x is not None else None)

#Salvando o df_filtrado em arquivo excel
df_filtrado.to_excel("Planilhas Tratadas\\Planilha_Tratada_Tramitações.xlsx", index=False)

# Carregando o dataframe original
df = df_filtrado

# Filtrando para remover valores nulos na coluna 'Tempo de resposta'
df = df[df['Tempo de resposta'].notnull()]

# Agrupando por 'Origem' e calculando a média de 'Tempo de resposta'
df_resumo = df.groupby('Setor Traduzido')['Tempo de resposta'].mean().reset_index()

# Salvando o df_resumo, tempo medio de resposta, em arquivo excel
df_resumo.to_excel("Planilhas Tratadas\Planilha_Tratada_Tempo_Medio_Resposta.xlsx", index=False)

# Renomeando coluna
df_resumo = df_resumo.rename(columns={'Tempo de resposta': 'Tempo médio de resposta'})

# Crie o DataFrame df_criticos com os valores da coluna 'Tempo parado' maiores que 2
df_criticos = df_filtrado[df_filtrado['Tempo parado'] > 2]

# Salvando o df_criticos, tabela de processos criticos, em arquivo excel
df_criticos.to_excel("Planilhas Tratadas\\Planilha_Tratada_Processos_Criticos.xlsx", index=False)