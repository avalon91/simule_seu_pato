from pato import *
from patoDeBorracha import *
from patoSelvagem import *
from patoFoguete import *

def setup():

    size(600, 400)

    size(400,400)
    background(234)
    fill(123,145,222)
    def draw(): ellipse(mouseX,mouseY,20,20)

    lista = [] #cria uma lista de qualquer coisa
    p = pato()
    lista.append(p)
    
    p = patoDeBorracha() 
    lista.append(p)
    
    p = patoFoguete()
    lista.append(p)
    
    p = patoSelvagem()
    lista.append(p)
    
    for p in lista:
        println(p.getVoo())
        

def draw():
    #desenhando campos verdejantes
    background(0,200,100)
    
    #desenhando o rio
    fill(0,0,220)
    noStroke()
    rect(0,height/2 - 50, width, 100)

    println(b.voo)
    println(b.nadar)
    
#links para aprendizagem
#http://www.tutorialspoint.com/python/python_classes_objects.htm
#http://pt.wikibooks.org/wiki/Python/Conceitos_b%C3%A1sicos/Heran%C3%A7a_e_polimorfismo
