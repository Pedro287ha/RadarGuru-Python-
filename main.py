import gpsd
from time import sleep
import os 

VELOCIDADE_LIMITE = 95

def checarVelocidade(velocidade) -> None:
    #velocidade = int(velocidade)
    if (velocidade > VELOCIDADE_LIMITE):
        print(f"Velocidade MAIOR que limite: {velocidade} > {VELOCIDADE_LIMITE}")

try:

    # Configuracao padrao de porta
    gpsd.connect(host="127.0.0.1", port=2947)

    while True:
        
        dados_gps = gpsd.get_current()
        
        modo_gps = dados_gps.mode
        numero_satelites_encontrados = dados_gps.sats 
        
        # <  1 NO MODE
        # == 1 NO FIX
        # == 2 2D FIX
        # >= 3 3D FIX
        
        if modo_gps >= 2:
            
            mapa_url = dados_gps.map_url()
            latitude = dados_gps.lat
            longitude = dados_gps.lon
            velocidade_em_kmp = round(dados_gps.hspeed * 3.6)
            
            #print(mapa_url)
            print(f"{velocidade_em_kmp} KM/h")
            
            print(latitude,longitude)
        else:
            print("Piscar....")
        sleep(1)
        
except ConnectionRefusedError:    
    print("Conexao falhou... servidor local possivelmente fechado!")

except UserWarning as erro:
    print("SINAL GPS NAO ENCONTRADO: --> ", erro)

except Exception as erro:
    print("ERRO DESCONHECIDO: ", erro)