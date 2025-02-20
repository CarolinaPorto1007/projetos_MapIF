#%% #lembre-se dessa hashtag com porcentagem para incializar o jupyternotebooks
import folium #Biblioteca base de criação de mapas
from folium import plugins
from folium.plugins import Draw
from folium.plugins import MousePosition
from folium.plugins import FloatImage #FEATURE: rosa dos ventos
import base64 #FEATURE: rosa dos ventos
import branca #FEATURE: legenda
from folium.plugins import Geocoder #FEATURE: caixa de busca

#Importando arquivos txt
doc = open( #Lendo arquivo txt para o input de destino final
            'txtmaior.txt',
            encoding="utf-8",
            mode="r",
        )

rotas = doc.read()
doc.close()

doc = open( #Lendo o arquivo html para aplicação da feature legenda
            'legenda.txt',
            encoding="utf-8",
            mode="r",
        )

legenda = doc.read()
doc.close()

#Ínício da geração básica do mapa
MapaIFPBCG = folium.Map(location = [-7.2397041,-35.9157529], 
                        zoom_start = 18, 
                        control_scale = True,
                        tiles= None) 

# criação da caixa de busca
Geocoder(collapsed=True,position= "topleft",add_marker=True).add_to(MapaIFPBCG)

folium.TileLayer(
		        tiles= 'https://{s}.tile.jawg.io/jawg-dark/{z}/{x}/{y}{r}.png?access-token={acesstoken}',
                attr='<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; <b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
                acesstoken = 'WvNMjK391KKRnUXspyFJXkHEPLsKaEP5F4biz9wjidz4bUZu4uYyNH2y23cleO4z',
                max_zoom= 22,
                min_zoom= 0,
                name='Modo Escuro').add_to(MapaIFPBCG)

folium.TileLayer(
		        tiles= 'https://tile.jawg.io/jawg-light/{z}/{x}/{y}{r}.png?access-token=WvNMjK391KKRnUXspyFJXkHEPLsKaEP5F4biz9wjidz4bUZu4uYyNH2y23cleO4z',
                attr='<a href=\"https://www.jawg.io?utm_medium=map&utm_source=attribution\" target=\"_blank\">&copy; Jawg</a> - <a href=\"https://www.openstreetmap.org?utm_medium=map-attribution&utm_source=jawg\" target=\"_blank\">&copy; OpenStreetMap</a>&nbsp;contributors',
                acesstoken = 'Su1RQRhG7TMz3hpWCkcf4VfDCPLNH1YllY5VTVgYhLDxbWH7mgngnOJDhsN7cDgz',
                max_zoom= 22,
                min_zoom= 0,
                name='Modo Claro').add_to(MapaIFPBCG)

folium.LayerControl().add_to(MapaIFPBCG)
#Fim da geração básica do mapa

#Começo das escolhas do Usuário
while True:

    try: #Começo de tratamento de erro se digitar string
        UsuarioDestinoInicial = int(input("Onde você se encontra?\n'1' para Portaria \n'2' para Vivência \n'3' para Bloco de aulas\n\nDigite onde você está: ")) #Menu para o usuário digitar onde ele está

        #Portaria para algum destino, Responsável: Ronaldo Urquiza.
        if UsuarioDestinoInicial == 1:
            
            while True:
                try: #Começo de tratamento de erro se digitar string
                    UsuarioDestinoFinal = int(input(rotas)) #Menu para o usuário digitar onde ele quer ir
                
                    if UsuarioDestinoFinal == 1: #Rota para o Laboratório de programação 1
                        
                        coordenadasProg1 = [  
                        [-7.2401575, -35.9166026],
                        [-7.2399899, -35.9161708],
                        [-7.2400405, -35.9161520],
                        [-7.239970, -35.915956],
                        [-7.2400511, -35.9159213],
                        [-7.2400405, -35.9158757],
                        [-7.2399154, -35.9155726],
                        [-7.2396307, -35.9156907],
                        [-7.2393593, -35.9158167],
                        [-7.239193, -35.915882],
                        [-7.2391890, -35.9158757]]


                        folium.Marker(location = [-7.2401575, -35.9166026], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.2391890, -35.9158757], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-hdd",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasProg1)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasProg1[i]
                            ponto_final = coordenadasProg1[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Portaria -> Laboratório de Programação 1').add_to(MapaIFPBCG)
                        break 

                    elif UsuarioDestinoFinal == 2: #Rota para o Laboratório de programação 2

                        coordenadasProg2 = [  
                        [-7.2401575, -35.9166026],
                        [-7.2399899, -35.9161708],
                        [-7.2400405, -35.9161520],
                        [-7.239970, -35.915956],
                        [-7.2400511, -35.9159213],
                        [-7.2400405, -35.9158757],
                        [-7.2399154, -35.9155726],
                        [-7.2396307, -35.9156907],
                        [-7.2393593, -35.9158167],
                        [-7.239193, -35.915882],
                        [-7.2390852, -35.9159267],
                        [-7.2390772, -35.9159133]]


                        folium.Marker(location = [-7.2401575, -35.9166026], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.2390772, -35.9159133], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-hdd",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasProg2)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasProg2[i]
                            ponto_final = coordenadasProg2[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Portaria -> Laboratório de Programação 2').add_to(MapaIFPBCG)
                        break 

                    elif UsuarioDestinoFinal == 3: #Rota para o Laboratório de programação 3

                        coordenadasProg3 = [  
                        [-7.2401575, -35.9166026],
                        [-7.2399899, -35.9161708],
                        [-7.2400405, -35.9161520],
                        [-7.239970, -35.915956],
                        [-7.2400511, -35.9159213],
                        [-7.2400405, -35.9158757],
                        [-7.2399154, -35.9155726],
                        [-7.2396307, -35.9156907],
                        [-7.2393593, -35.9158167],
                        [-7.239193, -35.915882],
                        [-7.2389708, -35.9159750],
                        [-7.2389602, -35.9159562]]


                        folium.Marker(location = [-7.2401575, -35.9166026], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.2389602, -35.9159562], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-hdd",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasProg3)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasProg3[i]
                            ponto_final = coordenadasProg3[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Portaria -> Laboratório de Programação 3').add_to(MapaIFPBCG)
                        break 
                        
                    elif UsuarioDestinoFinal == 4: #Rota para o Laboratório de programação 4
                        
                        coordenadasProg4 = [  
                        [-7.2401575, -35.9166026],
                        [-7.2399899, -35.9161708],
                        [-7.2400405, -35.9161520],
                        [-7.239970, -35.915956],
                        [-7.2400511, -35.9159213],
                        [-7.2400405, -35.9158757],
                        [-7.2399154, -35.9155726],
                        [-7.2396307, -35.9156907],
                        [-7.2393593, -35.9158167],
                        [-7.2390852, -35.9159267],
                        [-7.239093, -35.915943]]


                        folium.Marker(location = [-7.2401575, -35.9166026], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239093, -35.915943], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-hdd",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasProg4)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasProg4[i]
                            ponto_final = coordenadasProg4[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Portaria -> Laboratório de Programação 4').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 5: #Rota para o Laboratório de programação 5
                        
                        coordenadasProg5 = [  
                        [-7.2401575, -35.9166026],
                        [-7.2399899, -35.9161708],
                        [-7.2400405, -35.9161520],
                        [-7.239970, -35.915956],
                        [-7.2400511, -35.9159213],
                        [-7.2400405, -35.9158757],
                        [-7.2399154, -35.9155726],
                        [-7.2396307, -35.9156907],
                        [-7.2393593, -35.9158167],
                        [-7.239038, -35.915697],
                        [-7.239049, -35.915676]]


                        folium.Marker(location = [-7.2401575, -35.9166026], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239049, -35.915676], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-hdd",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasProg5)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasProg5[i]
                            ponto_final = coordenadasProg5[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Portaria -> Laboratório de Programação 5').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 6: #Rota para o Laboratório de informática 1

                        coordenadasInfo1 = [  
                        [-7.2401575, -35.9166026],
                        [-7.2399899, -35.9161708],
                        [-7.2400405, -35.9161520],
                        [-7.239970, -35.915956],
                        [-7.2400511, -35.9159213],
                        [-7.2400405, -35.9158757],
                        [-7.2399154, -35.9155726],
                        [-7.2396307, -35.9156907],
                        [-7.2393593, -35.9158167],
                        [-7.2396653, -35.9159508],
                        [-7.239656, -35.915967]]


                        folium.Marker(location = [-7.2401575, -35.9166026], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239656, -35.915967], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-hdd",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasInfo1)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasInfo1[i]
                            ponto_final = coordenadasInfo1[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Portaria -> Laboratório de Informática 1').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 7: #Rota para a Biblioteca

                        
                        coordenadasBiblioteca = [  
                        [-7.2401575, -35.9166026],
                        [-7.2399899, -35.9161708],
                        [-7.2400405, -35.9161520],
                        [-7.239970, -35.915956],
                        [-7.2400511, -35.9159213],
                        [-7.2403203880177225, -35.915812759962705]]


                        folium.Marker(location = [-7.2401575, -35.9166026], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.2403203880177225, -35.915812759962705], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-book",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasBiblioteca)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasBiblioteca[i]
                            ponto_final = coordenadasBiblioteca[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Portaria -> Biblioteca').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 8: #Rota para a Sala 09

                        
                        coordenadasSala09 = [  
                        [-7.2401575, -35.9166026],
                        [-7.2399899, -35.9161708],
                        [-7.2400405, -35.9161520],
                        [-7.239970, -35.915956],
                        [-7.2400511, -35.9159213],
                        [-7.2403203880177225, -35.915812759962705],
                        [-7.24028048721991,  -35.91572294625111],
                        [-7.240326, -35.915702],
                        [-7.240207, -35.915415],
                        [-7.240091568821912, -35.91515968238606]]


                        folium.Marker(location = [-7.2401575, -35.9166026], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.240091568821912, -35.91515968238606], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-pencil",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasSala09)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasSala09[i]
                            ponto_final = coordenadasSala09[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Portaria -> Sala 09').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 9: #Rota para a Recepção

                        
                        coordenadasRecepção = [  
                        [-7.2401575, -35.9166026],
                        [-7.2399899, -35.9161708],
                        [-7.2400405, -35.9161520]]


                        folium.Marker(location = [-7.2401575, -35.9166026], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.2400405, -35.9161520], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-phone-alt",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasRecepção)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasRecepção[i]
                            ponto_final = coordenadasRecepção[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Portaria -> Recepção').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 10: #Rota para o Gabinete médico

                        
                        coordenadasGabineteMédico = [  
                        [-7.2401575, -35.9166026],
                        [-7.2399899, -35.9161708],
                        [-7.2400405, -35.9161520],
                        [-7.239970, -35.915956],
                        [-7.23990230, -35.91600200],
                        [-7.239851, -35.915985],
                        [-7.239814492338399, -35.91607441989644]]


                        folium.Marker(location = [-7.2401575, -35.9166026], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239814492338399, -35.91607441989644], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-heart-empty",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasGabineteMédico)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasGabineteMédico[i]
                            ponto_final = coordenadasGabineteMédico[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Portaria -> Gabinete Médico').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 11: #Rota para o Ramo estudantil 

                        
                        coordenadasRamo = [  
                        [-7.2401575, -35.9166026],
                        [-7.2399899, -35.9161708],
                        [-7.2400405, -35.9161520],
                        [-7.239970, -35.915956],
                        [-7.2400511, -35.9159213],
                        [-7.2400405, -35.9158757],
                        [-7.2399154, -35.9155726],
                        [-7.2396307, -35.9156907],
                        [-7.2393593, -35.9158167],
                        [-7.2396653, -35.9159508],
                        [-7.239743789261753, -35.91599373340077],
                        [-7.239766150, -35.915958126]]


                        folium.Marker(location = [-7.2401575, -35.9166026], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239766150, -35.915958126], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-briefcase",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasRamo)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasRamo[i]
                            ponto_final = coordenadasRamo[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Portaria -> Ramo estudantil').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 12: #Rota para o Laboratório de eletrônica analógica

                        
                        coordenadasEA = [  
                        [-7.2401575, -35.9166026],
                        [-7.2399899, -35.9161708],
                        [-7.2400405, -35.9161520],
                        [-7.239970, -35.915956],
                        [-7.2400511, -35.9159213],
                        [-7.2400405, -35.9158757],
                        [-7.2399154, -35.9155726],
                        [-7.2396307, -35.9156907],
                        [-7.239641 ,-35.915714]]


                        folium.Marker(location = [-7.2401575, -35.9166026], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239641 ,-35.915714], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-flash",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasEA)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasEA[i]
                            ponto_final = coordenadasEA[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Portaria -> Laboratório de Eletrônica Analógica').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 13: #Rota para o Laboratório de eletrônica digital

                        
                        coordenadasED = [  
                        [-7.2401575, -35.9166026],
                        [-7.2399899, -35.9161708],
                        [-7.2400405, -35.9161520],
                        [-7.239970, -35.915956],
                        [-7.2400511, -35.9159213],
                        [-7.2400405, -35.9158757],
                        [-7.2399154, -35.9155726],
                        [-7.2396307, -35.9156907],
                        [-7.2393593, -35.9158167],
                        [-7.2396653, -35.9159508],
                        [-7.239677, -35.915932]]


                        folium.Marker(location = [-7.2401575, -35.9166026], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239677, -35.915932], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-wrench",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasED)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasED[i]
                            ponto_final = coordenadasED[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Portaria -> Laboratório de Eletrônica Digital').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 14: #Rota para o Refeitório

                        
                        coordenadasRefeitorio = [  
                        [-7.2401575, -35.9166026],
                        [-7.2399899, -35.9161708],
                        [-7.2400405, -35.9161520],
                        [-7.239970, -35.915956],
                        [-7.2400511, -35.9159213],
                        [-7.2400405, -35.9158757],
                        [-7.2399154, -35.9155726],
                        [-7.23973790, -35.91516750],
                        [-7.23971780, -35.91516750],
                        [-7.23973760, -35.91519720]]


                        folium.Marker(location = [-7.2401575, -35.9166026], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.23973760, -35.91519720], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-cutlery",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasRefeitorio)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasRefeitorio[i]
                            ponto_final = coordenadasRefeitorio[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Portaria -> Refeitório').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 15: #Rota para o Auditório

                        
                        coordenadasAuditorio = [  
                        [-7.2401575, -35.9166026],
                        [-7.2399899, -35.9161708],
                        [-7.2400405, -35.9161520],
                        [-7.239970, -35.915956],
                        [-7.2400511, -35.9159213],
                        [-7.2400405, -35.9158757],
                        [-7.2399154, -35.9155726],
                        [-7.2396307, -35.9156907],
                        [-7.2393593, -35.9158167],
                        [-7.239174, -35.9162143]]


                        folium.Marker(location = [-7.2401575, -35.9166026], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239174, -35.916214], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-eye-open",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasAuditorio)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasAuditorio[i]
                            ponto_final = coordenadasAuditorio[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Portaria -> Auditório').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 16: #Rota para a Vivência

                            
                        coordenadasVivencia = [  
                        [-7.2401575, -35.9166026],
                        [-7.2399899, -35.9161708],
                        [-7.2400405, -35.9161520],
                        [-7.239970, -35.915956],
                        [-7.2400511, -35.9159213],
                        [-7.2400405, -35.9158757],
                        [-7.2399154, -35.9155726],
                        [-7.2396307, -35.9156907],
                        [-7.2393593, -35.9158167]]


                        folium.Marker(location = [-7.2401575, -35.9166026], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.2393593, -35.9158167], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-user",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasVivencia)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasVivencia[i]
                            ponto_final = coordenadasVivencia[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Portaria -> Vivência').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 17: #Rota para o Bloco de aulas

                            
                        coordenadasBlocoAulas = [  
                        [-7.2401575, -35.9166026],
                        [-7.2399899, -35.9161708],
                        [-7.2400405, -35.9161520],
                        [-7.239970, -35.915956],
                        [-7.2400511, -35.9159213],
                        [-7.2403203880177225, -35.915812759962705],
                        [-7.24028048721991,  -35.91572294625111],
                        [-7.240326, -35.915702],
                        [-7.240207, -35.915415]]


                        folium.Marker(location = [-7.2401575, -35.9166026], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.240207, -35.915415], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-tasks",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasBlocoAulas)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasBlocoAulas[i]
                            ponto_final = coordenadasBlocoAulas[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Portaria -> Bloco de Aulas').add_to(MapaIFPBCG)
                        break
                    
                    else:
                        print('Digite um número de 1 a 17') 
                
                except ValueError:#Se digitar string?
                    print('Digite um número, não um texto!')
                    continue

        #Vivência para algum destino, Responsável: Carolina Porto.
        elif UsuarioDestinoInicial == 2: 

            while True:
                try:#Começo de tratamento de erro se digitar string
                    UsuarioDestinoFinal = int(input(rotas)) #Menu para o usuário digitar onde ele quer ir
                    
                    if UsuarioDestinoFinal == 1: #Rota para o Laboratório de programação 1
                        coordenadasProg1 =[
                        [-7.239359 ,-35.915816],
                        [-7.239193,-35.915882],
                        [-7.2391890, -35.9158757]]
                        
                        folium.Marker(location = [-7.239359 ,-35.915816], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-user",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.2391890, -35.9158757], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-hdd",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasProg1)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasProg1[i]
                            ponto_final = coordenadasProg1[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Vivência -> Laboratório de Programação 1').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 2: #Rota para o Laboratório de programação 2
                        coordenadasProg2 =[
                        [-7.239359 ,-35.915816],
                        [-7.239193,-35.915882],
                        [-7.2390852, -35.9159267],
                        [-7.2390772, -35.9159133]]  
                    
                        folium.Marker(location = [-7.239359 ,-35.915816], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-user",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.2390772, -35.9159133], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-hdd",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasProg2)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasProg2[i]
                            ponto_final = coordenadasProg2[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Vivência -> Laboratório de Programação 2').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 3: #Rota para o Laboratório de programação 3 
                        coordenadasProg3 =[
                        [-7.239359 ,-35.915816],
                        [-7.239193,-35.915882],
                        [-7.2390852, -35.9159267],
                        [-7.2389708, -35.9159750],
                        [-7.2389602, -35.9159562]]  
                    
                        folium.Marker(location = [-7.239359 ,-35.915816], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-user",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.2389602, -35.9159562], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-hdd",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasProg3)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasProg3[i]
                            ponto_final = coordenadasProg3[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Vivência -> Laboratório de Programação 3').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 4: #Rota para o Laboratório de programação 4
                        coordenadasProg4 =[
                            [-7.239359 ,-35.915816],
                            [-7.2390852, -35.9159267],
                            [-7.239093, -35.915943]]  
                    
                        folium.Marker(location = [-7.239359 ,-35.915816], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-user",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239093, -35.915943], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-hdd",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasProg4)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasProg4[i]
                            ponto_final = coordenadasProg4[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Vivência -> Laboratório de Programação 4').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 5: #Rota para o Laboratório de programação 5
                        coordenadasProg5 =[
                            [-7.239359 ,-35.915816],
                            [-7.239038, -35.915697],
                            [-7.239049, -35.915676]]  
                    
                        folium.Marker(location = [-7.239359 ,-35.915816], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-user",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239049, -35.915676], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-hdd",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasProg5)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasProg5[i]
                            ponto_final = coordenadasProg5[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Vivência -> Laboratório de Programação 5').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 6: #Rota para o Laboratório de informática 
                        coordenadasLabinfo1 =[
                            [-7.239359 ,-35.915816],
                            [-7.2396653,-35.9159508],
                            [-7.239656, -35.915967]]
                        
                        folium.Marker(location = [-7.239359 ,-35.915816], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-user",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239656, -35.915967], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-hdd",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasLabinfo1)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasLabinfo1[i]
                            ponto_final = coordenadasLabinfo1[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Vivência -> Laboratório de Informática 1').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 7: #Rota para a Biblioteca
                        coordenadasBiblioteca =[
                            [-7.239359 ,-35.915816],
                            [-7.2396307,-35.9156907],
                            [-7.239914844385245, -35.91557318434195 ],
                            [-7.2401230,-35.9154600 ],
                            [-7.240207, -35.915415],
                            [-7.240326, -35.915702],
                            [-7.24028048721991,  -35.91572294625111],
                            [-7.2403203880177225, -35.915812759962705]]  
                    
                        folium.Marker(location = [-7.239359 ,-35.915816], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-user",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.2403203880177225, -35.915812759962705], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-book",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasBiblioteca)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasBiblioteca[i]
                            ponto_final = coordenadasBiblioteca[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Vivência -> Biblioteca').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 8: #Rota para a sala 09
                        coordenadasSala09 =[
                            [-7.239359 ,-35.915816],
                            [-7.2396307,-35.9156907],
                            [-7.239914844385245, -35.91557318434195 ],
                            [-7.2401230,-35.9154600 ],
                            [-7.240207, -35.915415],
                            [-7.240091568821912, -35.91515968238606]]  
                    
                        folium.Marker(location = [-7.239359 ,-35.915816], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-user",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.240091568821912, -35.91515968238606], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-pencil",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasSala09)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasSala09[i]
                            ponto_final = coordenadasSala09[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Vivência -> Sala 09').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 9: #Rota para a sala Recepção
                        coordenadasRecepção =[
                            [-7.239359 ,-35.915816],
                            [-7.2396307, -35.9156907],
                            [-7.239914844385245, -35.91557318434195 ],
                            [-7.2400405,-35.9158757 ],
                            [-7.240040,-35.915921],
                            [-7.239970, -35.915956],
                            [-7.24003920, -35.91615240]]  
                    
                        folium.Marker(location = [-7.239359 ,-35.915816], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-user",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.24003920, -35.91615240], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-phone-alt",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasRecepção)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasRecepção[i]
                            ponto_final = coordenadasRecepção[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Vivência -> Recepão').add_to(MapaIFPBCG)  
                        break

                    elif UsuarioDestinoFinal == 10: #Rota para o Gabinete médico
                        coordenadasGabineteMédico =[
                            [-7.239359 ,-35.915816],
                            [-7.2396307, -35.9156907],
                            [-7.239914844385245, -35.91557318434195 ],
                            [-7.2400405,-35.9158757 ],
                            [-7.240040,-35.915921],
                            [-7.239970, -35.915956],
                            [-7.23990230, -35.91600200],
                            [-7.239851, -35.915985],
                            [-7.239814492338399, -35.91607441989644]]  
                    
                        folium.Marker(location = [-7.239359 ,-35.915816], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-user",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239814492338399, -35.91607441989644], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-heart-empty",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasGabineteMédico)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasGabineteMédico[i]
                            ponto_final = coordenadasGabineteMédico[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Vivência -> Gabinete médico').add_to(MapaIFPBCG)                      
                        break

                    elif UsuarioDestinoFinal == 11: #Ramo Estudantil
                        coordenadasRamo =[
                            [-7.239359 ,-35.915816],
                            [-7.2396653,-35.9159508],
                            [-7.239743789261753 , -35.91599373340077 ],
                            [-7.239766150 , -35.915958126]]  
                    
                        folium.Marker(location = [-7.239359 ,-35.915816], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-user",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239766150 , -35.915958126], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-briefcase",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasRamo)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasRamo[i]
                            ponto_final = coordenadasRamo[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Vivência -> Ramo Estudantil').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 12: #laboratório Eletrônica Analógica
                        coordenadasLabEA =[
                            [-7.239359 ,-35.915816],
                            [-7.2396307, -35.9156907],
                            [-7.239641 ,-35.915714]]  
                    
                        folium.Marker(location = [-7.239359 ,-35.915816], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-user",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239641 ,-35.915714], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-flash",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasLabEA)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasLabEA[i]
                            ponto_final = coordenadasLabEA[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Vivência -> Eletrônica Analógica').add_to(MapaIFPBCG)
                        break

                    elif UsuarioDestinoFinal == 13: #laboratório Eletrônica Digital
                        coordenadasLabED =[
                            [-7.239359 ,-35.915816],
                            [-7.2396653,-35.9159508],
                            [-7.239677, -35.915932]]
                        
                        folium.Marker(location = [-7.239359 ,-35.915816], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-user",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239677, -35.915932], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-wrench",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasLabED)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasLabED[i]
                            ponto_final = coordenadasLabED[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Vivência -> Eletrônica Digital').add_to(MapaIFPBCG)            
                        break

                    elif UsuarioDestinoFinal == 14: #Refeitorio
                        coordenadasRefeitorio =[
                            [-7.239359 ,-35.915816],
                            [-7.2396307, -35.9156907],
                            [-7.239914844385245, -35.91557318434195 ],
                            [-7.23973790, -35.91516750],
                            [-7.23971780,-35.91516750],
                            [-7.23973760, -35.91519720]]  
                    
                        folium.Marker(location = [-7.239359 ,-35.915816], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-user",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.23973760, -35.91519720], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-cutlery",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasRefeitorio)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasRefeitorio[i]
                            ponto_final = coordenadasRefeitorio[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Vivência -> Refeitorio').add_to(MapaIFPBCG)   
                        break

                    elif UsuarioDestinoFinal == 15: #Auditorio
                        coordenadasAuditorio =[
                            [-7.239359 ,-35.915816],
                            [-7.239174, -35.916214]]  
                    
                        folium.Marker(location = [-7.239359 ,-35.915816], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-user",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239174, -35.916214], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-eye-open",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasAuditorio)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasAuditorio[i]
                            ponto_final = coordenadasAuditorio[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Vivência -> Auditório').add_to(MapaIFPBCG) 
                        break

                    elif UsuarioDestinoFinal == 16: #Portaria
                        coordenadasPort =[
                            [-7.239359 ,-35.915816],
                            [-7.2396307, -35.9156907],
                            [-7.239914844385245, -35.91557318434195],
                            [-7.2400405,-35.9158757],
                            [-7.240040,-35.915921],
                            [-7.239970, -35.915956],
                            [-7.24003920, -35.91615240],
                            [-7.239991, -35.916171], 
                            [-7.240157, -35.916602]]  
                        
                        folium.Marker(location = [-7.239359 ,-35.915816], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-user",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.240157, -35.916602], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasPort)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasPort[i]
                            ponto_final = coordenadasPort[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Vivência -> Portaria').add_to(MapaIFPBCG)  
                        break

                    elif UsuarioDestinoFinal == 17: #Bloco de Aulas
                        coordenadasBlocoAulas =[
                            [-7.239359 ,-35.915816],
                            [-7.2396307, -35.9156907],
                            [-7.239914844385245, -35.91557318434195  ],
                            [-7.2401230,-35.9154600],
                            [-7.240207, -35.915415]]
                        
                        folium.Marker(location = [-7.239359 ,-35.915816], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-user",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.240207, -35.915415], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-tasks",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasBlocoAulas)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasBlocoAulas[i]
                            ponto_final = coordenadasBlocoAulas[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Vivência -> Bloco de aulas').add_to(MapaIFPBCG) 
                        break
                    
                    else:
                        print('Digite um número de 1 a 17') 

                except ValueError:#Se digitar string?
                    print('Digite um número, não um texto!')
                    continue

        #Bloco de aulas para algum destino, Responsável: Mariane Oliveira.
        elif UsuarioDestinoInicial == 3: 
            
            while True: 
                try:#Começo de tratamento de erro se digitar string
                    UsuarioDestinoFinal = int(input(rotas)) #Menu para o usuário digitar onde ele quer ir

                    if UsuarioDestinoFinal == 1: #Rota para o Laboratório de programação 1
                            
                        coordenadasProg1 = [  
                        [-7.240207, -35.915415],
                        [-7.2401230,-35.9154600],
                        [-7.239914844385245, -35.91557318434195],
                        [-7.239914844385245, -35.91557318434195 ],
                        [-7.239359,-35.915816],
                        [-7.239193,-35.915882],
                        [-7.239189,-35.915875]]


                        folium.Marker(location = [-7.240207, -35.915415], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-tasks",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.2391890, -35.9158757], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-hdd",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasProg1)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasProg1[i]
                            ponto_final = coordenadasProg1[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Bloco de aulas -> Laboratório de Programação 1').add_to(MapaIFPBCG)
                        break
                    
                    elif UsuarioDestinoFinal == 2: #Rota para o Laboratório de programação 2
                            
                        coordenadasProg2 = [  
                        [-7.240207, -35.915415],
                        [-7.2401230,-35.9154600],
                        [-7.239914844385245, -35.91557318434195],
                        [-7.239914844385245, -35.91557318434195 ],
                        [-7.239359,-35.915816],
                        [-7.239193,-35.915882],
                        [-7.239085,-35.915926],
                        [-7.2390772,-35.9159133]
                        ]


                        folium.Marker(location = [-7.240207, -35.915415], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-tasks",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.2390772,-35.9159133], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-hdd",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasProg2)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasProg2[i]
                            ponto_final = coordenadasProg2[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Bloco de aulas -> Laboratório de Programação 2').add_to(MapaIFPBCG)
                        break
                    
                    elif UsuarioDestinoFinal == 3: #Rota para o Laboratório de programação 3
                            
                        coordenadasProg3 = [  
                        [-7.240207, -35.915415],
                        [-7.2401230,-35.9154600],
                        [-7.239914844385245, -35.91557318434195],
                        [-7.239914844385245, -35.91557318434195 ],
                        [-7.239359,-35.915816],
                        [-7.239193,-35.915882],
                        [-7.239085,-35.915926],
                        [-7.238970,-35.915976],
                        [-7.238961, -35.915957]
                        ]


                        folium.Marker(location = [-7.240207, -35.915415], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-tasks",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.238961, -35.915957], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-hdd",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasProg3)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasProg3[i]
                            ponto_final = coordenadasProg3[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Bloco de aulas -> Laboratório de Programação 3').add_to(MapaIFPBCG)
                        break    

                    elif UsuarioDestinoFinal == 4: #Rota para o Laboratório de programação 4
                            
                        coordenadasProg4 = [  
                        [-7.240207, -35.915415],
                        [-7.2401230,-35.9154600],
                        [-7.239914844385245, -35.91557318434195],
                        [-7.239914844385245, -35.91557318434195 ],
                        [-7.239359,-35.915816],
                        [-7.239193,-35.915882],
                        [-7.239085,-35.915926],
                        [-7.239093, -35.915943]
                        ]


                        folium.Marker(location = [-7.240207, -35.915415], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-tasks",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239093, -35.915943], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-hdd",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasProg4)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasProg4[i]
                            ponto_final = coordenadasProg4[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Bloco de aulas -> Laboratório de Programação 4').add_to(MapaIFPBCG) 
                        break  

                    elif UsuarioDestinoFinal == 5: #Rota para o Laboratório de programação 4
                            
                        coordenadasProg5 = [  
                        [-7.240207, -35.915415],
                        [-7.2401230,-35.9154600],
                        [-7.239914844385245, -35.91557318434195],
                        [-7.239914844385245, -35.91557318434195 ],
                        [-7.239359,-35.915816],
                        [-7.239038,-35.915697],
                        [-7.239049,-35.915676],
                        ]


                        folium.Marker(location = [-7.240207, -35.915415], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-tasks",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239049,-35.915676], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-hdd",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasProg5)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasProg5[i]
                            ponto_final = coordenadasProg5[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Bloco de aulas -> Laboratório de Programação 5').add_to(MapaIFPBCG) 
                        break

                    elif UsuarioDestinoFinal == 6: #Rota para o Laboratório de informática 1
                            
                        coordenadasLabInfo1 = [  
                        [-7.240207, -35.915415],
                        [-7.2401230,-35.9154600],
                        [-7.239914844385245, -35.91557318434195],
                        [-7.239914844385245, -35.91557318434195 ],
                        [-7.239359,-35.915816],
                        [-7.2396653,-35.9159508],
                        [-7.239656,	-35.915967],
                        ]


                        folium.Marker(location = [-7.240207, -35.915415], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-tasks",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239656, -35.915967], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-hdd",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasLabInfo1)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasLabInfo1[i]
                            ponto_final = coordenadasLabInfo1[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Bloco de aulas -> Laboratório de informática 1').add_to(MapaIFPBCG) 
                        break
                                
                    elif UsuarioDestinoFinal == 7: #Rota para a Biblioteca
                            
                        coordenadasBiblio = [  
                        [-7.240207, -35.915415],
                        [-7.240326, -35.915702],
                        [-7.240280487219918,-35.91572294625111],
                        [-7.2403203880177225, -35.915812759962705]
                        ]


                        folium.Marker(location = [-7.240207, -35.915415], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-tasks",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.2403203880177225, -35.915812759962705], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-book",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasBiblio)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasBiblio[i]
                            ponto_final = coordenadasBiblio[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Bloco de aulas -> Biblioteca').add_to(MapaIFPBCG) 
                        break                

                    elif UsuarioDestinoFinal == 8: #Rota para a Sala 09
                            
                        coordenadasSala = [  
                        [-7.240207, -35.915415],
                        [-7.240207, -35.915415],
                        [-7.240091568821912, -35.91515968238606]
                        ]


                        folium.Marker(location = [-7.240207, -35.915415], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-tasks",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.240091568821912, -35.91515968238606], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-pencil",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasSala)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasSala[i]
                            ponto_final = coordenadasSala[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Bloco de aulas -> Sala 09').add_to(MapaIFPBCG) 
                        break

                    elif UsuarioDestinoFinal == 9: #Rota para a Recepção
                            
                        coordenadasRece = [  
                        [-7.240207, -35.915415],
                        [-7.2401230,-35.9154600],
                        [-7.239914844385245, -35.91557318434195],
                        [-7.239914844385245, -35.91557318434195 ],
                        [-7.240040,-35.915921],
                        [-7.239970,-35.915956],
                        [-7.24003920,-35.91615240]
                        ]


                        folium.Marker(location = [-7.240207, -35.915415], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-tasks",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.24003920,-35.91615240], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-phone-alt",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasRece)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasRece[i]
                            ponto_final = coordenadasRece[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Bloco de aulas -> Recepção').add_to(MapaIFPBCG)  
                        break

                    elif UsuarioDestinoFinal == 10: #Rota para o Gabinete Médico
                            
                        coordenadasGabi = [  
                        [-7.240207, -35.915415],
                        [-7.2401230,-35.9154600],
                        [-7.239914844385245, -35.91557318434195],
                        [-7.239914844385245, -35.91557318434195 ],
                        [-7.240040,-35.915921],
                        [-7.239970,-35.915956],
                        [-7.239851, -35.915985],
                        [-7.239814492338399, -35.91607441989644]
                        ]


                        folium.Marker(location = [-7.240207, -35.915415], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-tasks",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239814492338399, -35.91607441989644], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-heart-empty",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasGabi)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasGabi[i]
                            ponto_final = coordenadasGabi[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Bloco de aulas -> Gabinete Médico').add_to(MapaIFPBCG)  
                        break

                    elif UsuarioDestinoFinal == 11: #Rota para o Ramo Estudantil
                            
                        coordenadasRamo = [  
                        [-7.240207, -35.915415],
                        [-7.2401230,-35.9154600],
                        [-7.2396307, -35.9156907],
                        [-7.239359,-35.915816],
                        [-7.2396653,-35.9159508],
                        [-7.239743789261753, -35.91599373340077],
                        [-7.239743789261753, -35.91599373340077],
                        [-7.239766150, -35.915958126]
                        ]

                        folium.Marker(location = [-7.240207, -35.915415], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-tasks",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239766150, -35.915958126], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-briefcase",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasRamo)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasRamo[i]
                            ponto_final = coordenadasRamo[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Bloco de aulas -> Ramo Estudantil').add_to(MapaIFPBCG) 
                        break 

                    elif UsuarioDestinoFinal == 12: #Rota para o Laboratório de Eletrônica Analógica
                            
                        coordenadasLabEA = [  
                        [-7.240207, -35.915415],
                        [-7.2401230,-35.9154600],
                        [-7.239914844385245, -35.91557318434195],
                        [-7.239914844385245, -35.91557318434195 ],
                        [-7.2396307, -35.9156907],
                        [-7.239641, -35.915714]
                        ]


                        folium.Marker(location = [-7.240207, -35.915415], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-tasks",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239641, -35.915714], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-flash",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasLabEA)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasLabEA[i]
                            ponto_final = coordenadasLabEA[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Bloco de aulas -> Laboratório de Eletrônica Analógica').add_to(MapaIFPBCG) 
                        break 

                    elif UsuarioDestinoFinal == 13: #Rota para o Laboratório de Eletrônica Digital
                            
                        coordenadasLabED = [  
                        [-7.240207, -35.915415],
                        [-7.2401230,-35.9154600],
                        [-7.239914844385245, -35.91557318434195],
                        [-7.239914844385245, -35.91557318434195 ],
                        [-7.239359,-35.915816],
                        [-7.2396653,-35.9159508],
                        [-7.239677, -35.915932],
                        ]


                        folium.Marker(location = [-7.240207, -35.915415], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-tasks",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239677, -35.915932], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-wrench",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasLabED)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasLabED[i]
                            ponto_final = coordenadasLabED[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Bloco de aulas -> Laboratório de Eletrônica Digital').add_to(MapaIFPBCG)  
                        break

                    elif UsuarioDestinoFinal == 14: #Rota para o Refeitório
                            
                        coordenadasRef = [  
                        [-7.240207, -35.915415],
                        [-7.2401230,-35.9154600],
                        [-7.239914844385245, -35.91557318434195],
                        [-7.23973790, -35.91516750],
                        [-7.23971780,-35.91516750],
                        [-7.23973760, -35.91519720]
                        ]


                        folium.Marker(location = [-7.240207, -35.915415], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-tasks",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.23973760, -35.91519720], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-cutlery",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasRef)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasRef[i]
                            ponto_final = coordenadasRef[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Bloco de aulas -> Refeitorio').add_to(MapaIFPBCG)  
                        break

                    elif UsuarioDestinoFinal == 15: #Rota para o Auditório
                            
                        coordenadasAud = [  
                        [-7.240207, -35.915415],
                        [-7.2401230,-35.9154600],
                        [-7.239914844385245, -35.91557318434195],
                        [-7.2396307, -35.9156907],
                        [-7.239359,-35.915816],
                        [-7.239174, -35.916214]
                        ]


                        folium.Marker(location = [-7.240207, -35.915415], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-tasks",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239174, -35.916214], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-eye-open",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasAud)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasAud[i]
                            ponto_final = coordenadasAud[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Bloco de aulas -> Auditório').add_to(MapaIFPBCG)
                        break  

                    elif UsuarioDestinoFinal == 16: #Rota para a Portaria
                            
                        coordenadasPort = [  
                        [-7.240207, -35.915415],
                        [-7.2401230,-35.9154600],
                        [-7.239914844385245, -35.91557318434195],
                        [-7.2400405,-35.9158757],
                        [-7.240040,-35.915921],
                        [-7.239970, -35.915956],
                        [-7.24003920, -35.91615240],
                        [-7.239991, -35.916171],
                        [-7.240157, -35.916602]
                        ]


                        folium.Marker(location = [-7.240207, -35.915415], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-tasks",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.240157, -35.916602], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasPort)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasPort[i]
                            ponto_final = coordenadasPort[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Bloco de aulas -> Portaria').add_to(MapaIFPBCG)  
                        break
                    
                    elif UsuarioDestinoFinal == 17: #Rota para a Vivência
                            
                        coordenadasVive = [  
                        [-7.240207, -35.915415],
                        [-7.2401230,-35.9154600],
                        [-7.239914844385245, -35.91557318434195],
                        [-7.2396307, -35.9156907],
                        [-7.239359,-35.915816]
                        ]


                        folium.Marker(location = [-7.240207, -35.915415], 
                            popup = "Início", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-tasks",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        folium.Marker(location = [-7.239359,-35.915816], 
                            popup = "Final", 
                            icon = folium.Icon(icon = "glyphicon glyphicon-user",
                                                color = "darkred",
                                                icon_color = "white",
                                                prefix = "glyphicon")).add_to(MapaIFPBCG)

                        for i in range(len(coordenadasVive)-1): #-1 pq no ultimo nao vai ter i+1
                            ponto_inicial = coordenadasVive[i]
                            ponto_final = coordenadasVive[i+1]
                            folium.PolyLine(locations = [ponto_inicial,ponto_final],
                                color = 'green',
                                popup = 'Rota: Bloco de aulas -> Vivência').add_to(MapaIFPBCG)  
                        break
                    
                    else:
                        print('Digite um número de 1 a 17') 
                
                except ValueError:#Se digitar string?
                    print('Digite um número, não um texto!')
                    continue  

        #Se digitar número além de 1, 2 e 3?
        else:
            print('Digite um número de 1 a 3')   
            continue

    #Se digitar string?
    except ValueError:
        print('Digite um número, não um texto!')
        continue

    break
    
#Adicionado rosa dos ventos ao mapa
rosa_dos_ventos = 'rosa.png' #arquivo
with open(rosa_dos_ventos, 'rb') as rosaventos: #salvando como binário
    string_imagem = base64.b64encode(rosaventos.read()).decode("utf-8") #decodificando formato da imagem
#Adicionando a imagem em formato de string ao mapa, afinal tudo é em HTML
FloatImage("data:image/png; base64, {}".format(string_imagem), bottom = 12,left=1).add_to(MapaIFPBCG)
#Fim das rosa dos ventos

#Adicionando legenda ao mapa
legenda_mapa = f"""{legenda}"""
legenda = branca.element.MacroElement()
legenda._template = branca.element.Template(legenda_mapa)
MapaIFPBCG.add_child(legenda) #integra legenda ao mapa
#Fim da legenda no mapa

MapaIFPBCG #Gera o mapa
#%%2