from flask import Blueprint, render_template, request
from database.autor import AUTORES 
from database.models.autor import Autor

autor_route = Blueprint('autor',__name__)

"""
rotas de livros 

- /autor/ (GET) - Listar de autores 
- /autor/ (POST) - inserir o autor no servidor
- /autor/new (GET) - renderizar o formulario para criar um autor
- /autor/<id> (GET) - obter os dados do autor 
- /autor/<id>/edit (GET) - renderizar um formulario para editar um autor 
- /autor/<id>/update (PUT) - atualizar os dados do autor 
- /autor/<id>/delete (DELETE) - deleta o registro do usuario

"""


@autor_route.route('/')
def lista_autores(): 
    """ listar autores"""
    autores = Autor.select()
    return render_template('lista_autores.html', autores=autores)

@autor_route.route('/', methods=['POST'])
def inserir_autor(): 
    """ inserir os dados do autor"""
    data = request.json

    novo_autor = Autor.create(
        nome = data['nome'],
        livro = data['livro'],
    )
    return render_template('item_autor.html', autor=novo_autor)

@autor_route.route('/new')
def form_autor(): 
    """ formulario para cadastrar um autor"""
    return render_template('form_autores.html')

@autor_route.route('/<int:autor_id>')
def detalhe_autor(autor_id): 
    """exibir detalhes do autor """
    autor = Autor.get_by_id(autor_id)
    return render_template('detalhe_autores.html', autor=autor)

@autor_route.route('/<int:autor_id>/edit')
def form_edit_autor(autor_id): 
    """formulario para editar um autor"""
    autor = Autor.get_by_id(autor_id)
    return render_template('form_autores.html', autor=autor)

@autor_route.route('/<int:autor_id>/update', methods=['PUT'])
def uptade_autor(autor_id): 
    """atualizar informacoes do autor """
    data = request.json

    autor_editado = Autor.get_by_id(autor_id)
    autor_editado.nome = data['nome']
    autor_editado.livro = data['livro']
    autor_editado.save()
    #obter usuario pelo id 
   
    #edicao usuario 
    return render_template('item_autor.html', autor=autor_editado)


@autor_route.route('/<int:autor_id>/delete', methods=['DELETE'])
def delete_autor(autor_id): 
    """deletar informacoes do autor """
    autor = Autor.get_by_id(autor_id)
    autor.delete_instance()
    return{'deleted': 'ok'}