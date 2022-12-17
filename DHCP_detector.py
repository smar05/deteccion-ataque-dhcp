import pandas as pd

ip_serv_dhcp=input("Ingrese la direccion IP del servidor DHCP confiable: ")

df = pd.read_csv("captura.csv", index_col=0, header=0)

df_dhcp = df[(df['Protocol'] == 'DHCP') & (df['Source'] != ip_serv_dhcp) & (
    df['Destination'] != '255.255.255.255')]

df_dhcp2 = []

for indice, fila in df_dhcp.iterrows():
    if ('Offer' in fila['Info']) & (['IP Servidor DHCP: ' + fila['Source'], 
        'IP asignada a host: ' + fila['Destination']] not in df_dhcp2):
        df_dhcp2.append(['IP Servidor DHCP: ' + fila['Source'],
                        'IP asignada a host: ' + fila['Destination']])

if len(df_dhcp2) > 0:
    print('Se han detectado ' + str(len(df_dhcp2)) +
        ' servidores DHCP no confiables con direccion IP = ' + str(df_dhcp2))
else:
    print('No se han encontrado servidores DHCP no confiables')
