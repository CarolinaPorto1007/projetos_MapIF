#%%
import folium
from folium import plugins


###Rota simples
coordenadas = [[lat1,long1]
               [lat2,long2]]

for i in range(len(coordenadas)-1): #-1 pq no ultimo nao vai ter i+1
    ponto_inicial = coordenadas[i]
    ponto_final = coordenadas[i+1]
    folium.PolyLine(locations = [ponto_inicial,ponto_final],
                   color = 'green',
                   popup = 'Rota: X -> Y').add_to(mapa)



###Rota com popup marcador bonito

folium.Marker(location = [lat1,long1], 
              popup = "St. Therese Community Centre, 17 Conrod Rd.", 
              icon = folium.Icon(icon = "glyphicon glyphicon-home",
                                 color = "darkred",
                                 icon_color = "white",
                                 prefix = "glyphicon")).add_to(mapa_linhas)

folium.Marker(location = [lat2,long2], 
              popup = "1st Water Station", 
              icon = folium.Icon(icon = "glyphicon glyphicon-glass",
                                 color = "darkblue",
                                 icon_color = "white",
                                 prefix = "glyphicon")).add_to(mapa_linhas)


for i in range(len(coordenadas)-1):
    folium.PolyLine(locations = [[coordenadas[i][0], coordenadas[i][1]], [coordenadas[i+1][0], coordenadas[i+1][1]]],
                   color = 'navy').add_to(mapa_linhas)