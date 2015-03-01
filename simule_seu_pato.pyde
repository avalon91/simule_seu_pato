from pato import *
from patoDeBorracha import *
from patoSelvagem import *
from patoFoguete import *

def setup():
    size(400,400)
    background(234)
    fill(123,145,222)
    def draw(): ellipse(mouseX,mouseY,20,20)
    
    b=patoFoguete()
    
    println(b.voo)
    println(b.nadar)
    



#http://pt.wikibooks.org/wiki/Python/Conceitos_b%C3%A1sicos/Heran%C3%A7a_e_polimorfismo
