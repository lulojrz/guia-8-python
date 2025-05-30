from queue import LifoQueue as Pila
from queue import Queue as Cola
import unittest
from python2 import calcular_promedio_por_estudiante,visitar_sitio,navegar_atras

class tests_promedio(unittest.TestCase):
    def test_parametro_vacio(self):
        self.assertEqual(calcular_promedio_por_estudiante(()),{})
    
    def test_nombre_vacio(self):
        self.assertEqual(calcular_promedio_por_estudiante((("",10),("juan",5))),{"juan":5.0})
    
    def test_nota_fuera_de_rango(self):
        self.assertEqual(calcular_promedio_por_estudiante((("juan",11),("juan",5))),{"juan":5.0})
        
    def test_varios_estudiantes(self):
        ##los diccionarios no tienen orden y podemos cambiarlo de orden tranquilamente sin que haga lio
        self.assertEqual(calcular_promedio_por_estudiante((("juan",9),("simon",4),("juan",7),("simon",0))),{"simon":2.0,"juan":8.0})

class test_historial(unittest.TestCase):
    #testear para clave nueva
    def test_resultado_clave_existente(self):
        historiales:dict= {
         "Juan":Pila(),
         "Pedro":Pila() }
        historiales["Juan"].put("youtube.com")
        historiales["Juan"].put("exactascampus.com")
        historiales["Pedro"].put("mercadolibre.com")
        
        visitar_sitio(historiales,"Juan","river.com")
       
        self.assertEqual(historiales["Juan"].get(),"river.com")


class test_navegar_para_atras(unittest.TestCase):
    def test_navegar_para_atras_clave_existente(self):
        historiales:dict= {
         "Juan":Pila(),
         "Pedro":Pila() }
        historiales["Juan"].put("youtube.com")
        historiales["Juan"].put("exactascampus.com")
        historiales["Pedro"].put("mercadolibre.com")
        self.assertEqual(navegar_atras(historiales,"Juan"),"exactascampus.com")
    
    def test_navegar_parametro_vacio(self):
        historiales:dict= {
         "Juan":Pila(),
         "Pedro":Pila() }
        historiales["Juan"].put("youtube.com")
        historiales["Juan"].put("exactascampus.com")
        historiales["Pedro"].put("mercadolibre.com")
        self.assertEqual(navegar_atras(historiales,""),"")
        
    def test_usuario_no_existente(self):
        historiales:dict= {
         "Juan":Pila(),
         "Pedro":Pila() }
        historiales["Juan"].put("youtube.com")
        historiales["Juan"].put("exactascampus.com")
        historiales["Pedro"].put("mercadolibre.com")
        self.assertEqual(navegar_atras(historiales,"Sebastian"),"")
        
        

      
        
if __name__ == '__main__':
    unittest.main(verbosity=2)