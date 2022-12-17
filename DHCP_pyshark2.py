import pyshark

# Establece la interfaz de red que se utilizará para la captura
# (reemplaza "eth0" por el nombre de la interfaz de tu red)
#interface = 'Adapter for loopback traffic capture'

# Inicia la captura de tráfico en tiempo real
capture = pyshark.LiveCapture()  # interface=interface)

# Procesa cada paquete capturado en tiempo real
for packet in capture.sniff_continuously():
    # Verifica que el paquete sea un paquete IP y tenga una dirección de origen y de destino
    if hasattr(packet, "ip") and packet.ip.src and packet.ip.dst:
        # Imprime información sobre el paquete capturado
        print("Protocolo:", packet.highest_layer)
        print("Origen:", packet.ip.src)
        print("Destino:", packet.ip.dst)
        print("Longitud:", packet.length)
        print()
