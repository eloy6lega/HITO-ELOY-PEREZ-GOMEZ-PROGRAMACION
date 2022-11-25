# ╭━━━┳╮╱╱╭━━━┳╮╱╱╭╮
# ┃╭━━┫┃╱╱┃╭━╮┃╰╮╭╯┃
# ┃╰━━┫┃╱╱┃┃╱┃┣╮╰╯╭╯
# ┃╭━━┫┃╱╭┫┃╱┃┃╰╮╭╯
# ┃╰━━┫╰━╯┃╰━╯┃╱┃┃
# ╰━━━┻━━━┻━━━╯╱╰╯

#importamos una librería que he descubierto para imprimir las datastructures mas legibles
import pprint

#creo el diccionario de productos con sus keys values
productos={'Patata':2.99,'Tomate':4.99,'Zanahoria':5.99,'Pan':0.45,'Aguacates':9.99,'Platanos':3.99,'Naranja':3.99,'Mandarina':2.5,'Calabacin':6.99,'Lechuga':5.5,'Agua':1.00,'Leche':5.99}
productos.keys()
productos.values()

#damos la bienvenida
print('----------------BIENVENIDO A LA FRUTERÍA DE MOHAMMAD----------------')
print('Registro')

#creamos la clase registro para registrar al cliente

class Persona():
    def __init__(self) -> None:
        pass
    @staticmethod
    def registro():
        try:
            nombre = str(input('Nombre: '))
            apellido = str(input('Primer apellido: '))
            DNI = input('Introduzca DNI/NIF (12345678X): ')
            tlf = int(input('Télefono de contacto (611222333): '))
        except:
            print('Alguno de los valores introducidos no es válido, inténtalo de nuevo más tarde')
            
            
        print(f'BIENVENIDO {nombre} {apellido} con DNI/NIF {DNI} y teléfono {tlf}')

#instancio
j=Persona
j.registro()

#imprimo con la librería que importé  
pprint.pprint(productos)
cesta={}
lista={}

#hacemos una función para elegir los productos
def elegirProducto():
    print('--------------------------------------------------------------')
    #escribimos el nombre del producto TAL CUAL está escrito en la lista
    q=input('Escriba el nombre del producto que quiere seleccionar (Es importante que lo escribas igual que está en la lista, si no el sistema no lo reconocerá): ')
    print('--------------------------------------------------------------')
    #¿Lo queremos agregar a la cesta o a la lista?
    col=float(input(f'Quieres agregar "{q}" a la cesta (1) o a la lista de deseos (2): '))
    #si agregamos a la cesta
    if col == 1:
        #almacena el valor
        cesta[q]=productos[q]
        #imprime nuestra cesta
        print(f'Cesta: {cesta}')
        #imprime el total de dinero a pagar SIN IMPUESTOS
        print(f'Total: {sum(cesta.values())}')
    #si agregamos a la lista de deseos
    elif col== 2:
        #almacena el valor en la lista
        lista[q]=productos[q]
        #imprime la lista
        print(f'Lista de deseos: {lista}')
        #imprime el total de dinero a pagar en la lista
        print(f'Total: {sum(lista.values())}')
    #si te equivocas introduce un valor válido y vuelve a invocar la function
    elif col >= 3:
        print('Introduce una opción válida')
        elegirProducto()
elegirProducto()

#otra function para seguir o no comprando
def seguirComprando():
    #preguntamos si quiere o no
    print('---------------------------------------------------')
    sc=float(input('¿Quiere seguir comprando? Si (1) / No (2): '))
    print('---------------------------------------------------')
    #si quiere:
    if sc == 1:
        #imprime
        pprint.pprint(productos)
        #invoca la function para volver a elegir un producto
        elegirProducto()
        #vuelve a invocar la function para seguir o no comprando
        seguirComprando()
    #si no quiere:
    elif sc == 2:
        #recomendamos que añada los productos de la lista de deseos a la cesta si el cliente quiere
        print('---------------------------------------------------')
        print('LE RECOMENDAMOS QUE SI TIENE PRODUCTOS EN LA LISTA DE DESEOS LOS AÑADA A LA CESTA')
        quierelista=float(input('¿QUIERE AÑADIR LOS PRODUCTOS DE LA LISTA DE DESEOS A LA CESTA? SI(1) / NO(2): '))
        #si quiere:
        if quierelista==1:
            #imprime la lista de deseos
            pprint.pprint(lista)
            #pide que escribamos los productos TAL Y COMO están escritos
            print('Escriba de nuevo los nombres de los productos que quieres añadir a la cesta desde tu lista')
            esc=input('Escriba aquí (Es importante que lo escribas igual que está en la lista, si no el sistema no lo reconocerá): ')
            #lo almacenamos en cesta
            cesta[esc]=productos[esc]
        #imprimimos cesta
        print(f'Cesta: {cesta}')
        #precio total de la cesta
        print(f'Total: {sum(cesta.values())}€')
        #nos redirige a la zona de pagos
        print('---------------------------------------------------')
        print('REDIRIGIENDO A LA ZONA DE PAGOS...')
        print('---------------------------------------------------')
    #si te has equivocado, escribe una opción válida
    else:
        print('Introduce una opción válida')
        seguirComprando()
seguirComprando()

#function para los pagos
def pagos():
    #preguntamos el país para los impuestos
    pais=input('¿De qué país es usted? (Es para aplicar los impuestos correspondientes): ')
    #si el país es españa
    if pais.lower()=='españa':
        #los impuestos serán del 21%
        print('IMPUESTOS DEL 21%')
        #total de dinero con impuestos aplicados
        print(f'Total con impuestos: {sum(cesta.values())*1.21}')
    #si el país es distinto a españa
    else:
        #el país será internacional
        print('PAÍS INTERNACIONAL')
        #oferta flash de impuestos al 10% por el BLACK FRIDAY
        print('TENEMOS UNA OFERTA FLASH DE SÓLO EL 10% DE IMPUESTOS A COMPRAS INTERNACIONALES')
        #total de precio con impuestos aplicados
        print(f'Total con impuestos: {sum(cesta.values())*1.10}')
    #elegimos el método de pago
    print('TIENE QUE ELEGIR EL MÉTODO DE PAGO')
    #variable para hacer un match case (switch case)
    mpago=int(input('1 CUENTA BANCARIA\n 2 TARJETA DE PAGO\n 3 BONO CULTURAL JOVEN\n 4 TARJERTA REGALO TIENDA MOHAMMAD\n Elija un número:'))
    #el switch case
    match mpago:
        #si pulsa 1
        case 1:
            print('---------------------------------------------------')
            print('HA SELECCIONADO CUENTA BANCARIA')
            #pide los datos de la cuenta +/-
            IBAN=int(input('IBAN: '))
            numerodecuenta=int(input('Número de cuenta: '))
            #hace el cobro e imprime un recibo
            print(f'IMPRIMIENDO Y ENVIANDO RECIBO A LA CUENTA CON IBAN {IBAN} Y NÚMERO DE CUENTA {numerodecuenta}')
            print(f'RECIBO SE HA ENVIADO CORRECTAMENTE VÍA SMS')
            print('---------------------------------------------------')
        #si pulsa 2
        case 2:
            print('---------------------------------------------------')
            print('HA SELECCIONADO TARJETA DE PAGO')
            #pide los datos de la tarjeta +/-
            numerotarjeta=int(input('Número de la tarjeta: '))
            fechacad=input('Fecha de caducidad (MM/AA): ')
            CVV=int(input('CVV de la tarjeta (XXX): '))
            print('DATOS ALMACENADOS CORRECTAMENTE. EFECTUANDO COBRO...')
            print(f'EL COBRO SE HA EFECTUADO CORRECTAMENTE A LA TARJETA CON NUMERO {numerotarjeta}')
            print('---------------------------------------------------')
        #si pulsa 3
        case 3:
            print('---------------------------------------------------')
            print('HA SELECCIONADO BONO CULTURAL JOVEN')
            #pide los datos del bono +/-
            numerotarjetajoven=int(input('Número de la tarjeta joven: '))
            codigotar=int(input('Código de la tarjeta joven (XXXX): '))
            #hace el cobro e imprime un recibo
            print(f'FELICIDADES POR HABER OBTENIDO EL BONO CULTURAL JOVEN')
            print('ESTE COBRO DEBERÁ JUSTIFICARLO POSTERIORMENTE EN LA APP O EN LA WEB DE www.bonoculturaljoven.gob.es')
            print('EL COBRO SE HA REALIZADO')
            print('RECIBO ENVIADO A EL CORREO ASIGNADO A SU BONO CULTURAL. TAMBIÉN SE HA ENVIADO UN SMS AL TELÉFONO MÓVIL')
            print('---------------------------------------------------')
        #si pulsa 4
        case 4:
            print('---------------------------------------------------')
            print('HA SELECCIONADO TARJETA DE REGALO TIENDA MOHAMMAD')
            #pide los datos de la tarjeta regalo +/-
            codigotarreg=int(input('Código de la tarjeta regalo (XXX): '))
            #hace el cobro e imprime un recibo
            print('RECONOCIENDO TARJETA COMO OFICIAL DE LA TIENDA')
            print('RECONOCIENDO...')
            print('RECONOCIENDO...')
            print('RECONOCIENDO...')
            print('RECONOCIENDO...')
            print('TARJETA CANJEADA CON ÉXITO')
            print('---------------------------------------------------')
    #DAMOS LAS GRACIAS AL CLIENTE Y LE ANIMAMOS A VOLVER
    print('GRACIAS POR COMPRAR EN LA TIENDA DE MOHAMMAD. ESPERAMOS SU REGRESO')
pagos()

