﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shes
from DISClib.Algorithms.Sorting import insertionsort as inss
from DISClib.Algorithms.Sorting import selectionsort as sels
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick


assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def createCatalogArray():
    
    catalog = {'videos': None,
               'categories': None,}
    catalog['videos']= lt.newList(datastructure='ARRAY_LIST')
    catalog['categories'] = lt.newList(datastructure='ARRAY_LIST')

    
    return catalog

def createCatalogSingleLinked():
    
    catalog = {'videos': None,
               'categories': None}
    catalog['videos']= lt.newList(datastructure='SINGLE_LINKED')
    catalog['categories'] = lt.newList(datastructure='SINGLE_LINKED')
    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)
    

def addCategory(catalog, category):
    t = newCategory(category['id'], category['name'])
    lt.addLast(catalog['categories'], t)



# Funciones para creacion de datos

def newCategory(category_id,name):
    category = {'id': category_id, 'name': name}
    return category




# Funciones de consulta


def findCategoryid(catalog,category):
    for pos in range(len(catalog["categories"])):
        if lt.getElement(catalog["categories"],pos) == category:
            return lt.getElement(catalog["categories"],pos)["id"]


def catalogCountryCategory(catalog,bestCountry,bestCategoryid):
    topnVideos = lt.newList(datastructure='ARRAY_LIST')
    for position in range(0,len(catalog["videos"])):
        element = lt.getElement(catalog['videos'],position)
        if (element["country"] == bestCountry and element["category_id"]==bestCategoryid):
            lt.addLast(topnVideos,element)
    return topnVideos

def topnVideosByViews(sortedVideos,numberVideos):
    topnVideos = lt.newList(datastructure='ARRAY_LIST')
    position = 0
    while position <= numberVideos:
        lt.addLast(topnVideos,lt.getElement(sortedVideos,position))
        position += 1
    return topnVideos

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosByViews(video1, video2):
    """
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2: informacion del segundo video que incluye su valor 'views'
    
    """
    if video1['views'] < video2['views']:
        return True
    elif video1['views'] >= video2['views']:
        return False



    

# Funciones de ordenamiento

def selectionSortVideos(catalog,size):
    sub_list = lt.subList(catalog['videos'],0,size)
    start_time = time.process_time()
    sorted_list = sels.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

def insertionSortVideos(catalog,size):
    sub_list = lt.subList(catalog['videos'],0,size)
    start_time = time.process_time()
    sorted_list = inss.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

def shellSortVideos(catalog,size):
    sub_list = lt.subList(catalog['videos'],0,size)
    start_time = time.process_time()
    sorted_list = shes.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

def mergeSortVideos(catalog,size):
    sub_list = lt.subList(catalog['videos'],0,size)
    start_time = time.process_time()
    sorted_list = merge.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

def quickSortVideos(catalog,size):
    sub_list = lt.subList(catalog['videos'],0,size)
    start_time = time.process_time()
    sorted_list = quick.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list


def catalogSortedByViewsCountyCategory(catalog,bestCountry,bestCategoryid):
    videosCC =catalogCountryCategory(catalog,bestCountry,bestCategoryid)
    sortedVideos = merge.sort(videosCC,cmpVideosByViews)
    return sortedVideos