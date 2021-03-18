from flask import render_template,request, redirect, url_for
from src import app
from src.models.productos import ProductosModels


@app.route('/producto')
def producto():
    
    productosModels = ProductosModels()
    productos = productosModels.traerTodos()
   

    return render_template('productos/index.html', productos = productos)  

@app.route('/productos/crear', methods=['GET', 'POST'])
def crear_producto():
    #request sirve para mostarar el formulario de dcreacion 
    # y crear uno nuevo
    #estosd pasos se identifican con los metodos
    if request.method == 'GET':
        return render_template('productos/crear.html')

    nombre = request.form.get('nombre')  
    descripcion = request.form.get('descripcion') 
    estado = request.form.get('estado') 
    precio_compra = request.form.get('precio_compra') 
    precio_venta = request.form.get('precio_venta') 
    ganancia = request.form.get('ganancia')
    productosModels = ProductosModels()
    productosModels.crear(nombre, descripcion,precio_compra, precio_venta, ganancia, estado)

    return redirect(url_for('producto'))


@app.route('/productos/editar/<int:id>',methods=['GET', 'POST'])
def editar_producto(id):
    if request.method == 'GET':
        return render_template('productos/editar.html')
        
    nombre = request.form.get('nombre')  
    descripcion = request.form.get('descripcion') 
    
    precio_compra = request.form.get('precio_compra') 
    precio_venta = request.form.get('precio_venta') 
    ganancia = request.form.get('ganancia')
    estado = request.form.get('estado') 

    if estado == '1':
        estado ='Activo'
    else :
        estado = 'Inactivo'


    productosModels = ProductosModels()
    productosModels.editar(id,nombre, descripcion,precio_compra, precio_venta, ganancia, estado)

    return redirect(url_for('producto'))

  