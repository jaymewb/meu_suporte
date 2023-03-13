from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuario, Post

# with app.app_context():
#     database.create_all()

with app.app_context():
    Usuario.query.all()

# with app.app_context():
#     meus_usuario1 = Usuario.query.filter_by().first()

# with app.app_context():
#     print(meus_usuario1.username)
#     print(meus_usuario1.email)
#     print(meus_usuario1.senha)













#
# with app.app_context():
#     usuario = Usuario()
#     usuario2 = Usuario()
#     database.session.add(usuario)
#     database.session.add(usuario2)
#     database.session.commit()




#     usuario = Usuario(username="Jay", email="jayme@gmail.com", senha="1234567")
#     usuario2 = Usuario(username="Enzo", email="enzo@gmail.com", senha="1234567")

# with app.app_context():
#     Usuario.query.all()
#     meus_usuarios = Usuario.query.first()
    # print(meus_usuarios.username)
    # print(meus_usuarios.email)
    # print(meus_usuarios.senha)

# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo="Primeiro Post do Lira", corpo="Lira voando")
#     database.session.add(meu_post)
#     database.session.commit()

# with app.app_context():
#     post = Post.query.first()
#     print(post.titulo)
#     print(post.autor.email)


# with app.app_context():
#     database.drop_all()
#     database.create_all()
# def database():
#     return None
