from queue import LifoQueue as Pila
from queue import Queue as Cola
import unittest
from python2 import calcular_promedio_por_estudiante,visitar_sitio,navegar_atras,agregar_producto,actualizar_stock,actualizar_precio, calcular_inventario, contar_lineas,existe_palabra, cantidad_de_apariciones

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
        
 
class tests_agregar_producto_inventario(unittest.TestCase):
    def test_esperado(self):
        inventario:dict = {
       "Camiseta":{
       "Cantidad":5,
       "Precio":30000.00
        }}
        agregar_producto(inventario,"Gorra",35000.00,2)
        self.assertEqual(inventario["Gorra"],{"Cantidad":2,"Precio":35000.00})
        
    def test_precio_menora0(self):
        inventario:dict = {
       "Camiseta":{
       "Cantidad":5,
       "Precio":30000.00
        }}
        agregar_producto(inventario,"Gorra",-1,2)
        self.assertEqual(inventario,{"Camiseta":{"Cantidad":5,"Precio":30000.00}})
        
    def test_cantidad_menora0(self):
        inventario:dict = {
       "Camiseta":{
       "Cantidad":5,
       "Precio":30000.00
        }}
        agregar_producto(inventario,"Gorra",35000.00,-1)
        self.assertEqual(inventario,{"Camiseta":{"Cantidad":5,"Precio":30000.00}})
            
    def test_string_vacio(self):
        inventario:dict = {
       "Camiseta":{
       "Cantidad":5,
       "Precio":30000.00
        }}
        agregar_producto(inventario,"",35000.00,0)
        self.assertEqual(inventario,{"Camiseta":{"Cantidad":5,"Precio":30000.00}})
           
class tests_actualizar_stock(unittest.TestCase):
    def test_stock_clave_existente(self):
        inventario:dict = {
       "Camiseta":{
       "Cantidad":5,
       "Precio":30000.00
        }}
        actualizar_stock(inventario,"Camiseta",35)
        self.assertEqual(inventario,{"Camiseta":{"Cantidad":35,"Precio":30000.00}})
        
    def test_stock_clave_noexistente(self):
        inventario:dict = {
       "Camiseta":{
       "Cantidad":5,
       "Precio":30000.00
        }}
        actualizar_stock(inventario,"Remera",35)
        self.assertEqual(inventario,{"Camiseta":{"Cantidad":5,"Precio":30000.00}})
        
    def test_stock_cantidad_menora0(self):
        inventario:dict = {
       "Camiseta":{
       "Cantidad":5,
       "Precio":30000.00
        }}
        actualizar_stock(inventario,"Remera",-3)
        self.assertEqual(inventario,{"Camiseta":{"Cantidad":5,"Precio":30000.00}})
        
    def test_stock_string_vacio(self):
        inventario:dict = {
       "Camiseta":{
       "Cantidad":5,
       "Precio":30000.00
        }}
        actualizar_stock(inventario,"",35)
        self.assertEqual(inventario,{"Camiseta":{"Cantidad":5,"Precio":30000.00}})
        
class tests_actualizar_precio(unittest.TestCase):
    def test_precio_clave_existente(self):
        inventario:dict = {
       "Camiseta":{
       "Cantidad":5,
       "Precio":30000.00
        }}
        actualizar_precio(inventario,"Camiseta",40000)
        self.assertEqual(inventario,{"Camiseta":{"Cantidad":5,"Precio":40000.00}})
        
    def test_precio_clave_noexistente(self):
        inventario:dict = {
       "Camiseta":{
       "Cantidad":5,
       "Precio":30000.00
        }}
        actualizar_precio(inventario,"Remera",30.000)
        self.assertEqual(inventario,{"Camiseta":{"Cantidad":5,"Precio":30000.00}})
        
    def test_precio_cantidad_menora0(self):
        inventario:dict = {
       "Camiseta":{
       "Cantidad":5,
       "Precio":30000.00
        }}
        actualizar_precio(inventario,"Remera",-3)
        self.assertEqual(inventario,{"Camiseta":{"Cantidad":5,"Precio":30000.00}})
        
    def test_precio_string_vacio(self):
        inventario:dict = {
       "Camiseta":{
       "Cantidad":5,
       "Precio":30000.00
        }}
        actualizar_precio(inventario,"",35)
        self.assertEqual(inventario,{"Camiseta":{"Cantidad":5,"Precio":30000.00}})
        
class tests_calcular_inventario(unittest.TestCase):
    def test_calculo_inventario(self):
        inventario:dict = {
       "Camiseta":{
       "Cantidad":5,
       "Precio":30000
        },
       "Remera":{
         "Cantidad":2,
         "Precio":10000
           }
       }
        
        self.assertEqual(calcular_inventario(inventario),170000)
                
class tests_contar_lineas(unittest.TestCase):
    def test_contar_lineas_archivo_existente(self):
        self.assertEqual(contar_lineas("archivo.txt"),4)    
        
    def test_contar_lineas_archivo_noexistente(self):
        self.assertEqual(contar_lineas(""),0)    

  
class tests_existe_palabra(unittest.TestCase):
    def test_existe_palabra(self):
        self.assertTrue(existe_palabra("archivo.txt","me \n"))   
        
    def test_no_existe_palabra(self):
        self.assertFalse(existe_palabra("archivo.txt","a"))
        
class test_cant_apariciones(unittest.TestCase):
    def test_cant_apariciones(self):
        self.assertEqual(cantidad_de_apariciones("archivo.txt","Hola"),1)
           
if __name__ == '__main__':
    unittest.main(verbosity=2)