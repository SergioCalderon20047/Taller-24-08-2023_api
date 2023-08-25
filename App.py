from flaskr import create_app
from .modelos import Cancion, Usuario, db
from .modelos import Album, db
from .modelos import Medio
from .modelos import AlbumSchema
from flask_restful import Api
from .vistas import VistaCanciones, VistaCancion

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCanciones, '/canciones')
app,add_resource(VistaCanciones, '/canciones/<int:id_cancion')

with app.app_context():
    u = Usuario(nombre='juan', contrasenia='12345')
    c = Cancion(titulo="prueba", minutos=2, segundos=25, interprete="Sergio")
    a = Album(titulo='prueba', anio=1999, descripcion='texto', medio=Medio.CD)
    u.albumes.append(a)
    a.canciones.append(c)
    db.session.add(u)
    db.session.add(c)
    db.session.add(A)
    db.session.commit()
    print([Album_Schema.dumps(album) for album in Album.query.all()])
    print(Album.query.all())
    print(Album.query.all()[0].cancion)
    db.session.delete(a)
    print(Album.query.all())
    print(Cancion.query.all())


