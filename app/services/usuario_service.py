from models.usuario import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository) -> None:
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome= nome, email= email, senha= senha)
            
            cadastrado = self.repository.pesquisar_usuario_por_email(email = usuario.email)

            if cadastrado:
                print("Usuário já cadastrado!")
                return

            self.repository.salvar_usuario(usuario= usuario)
            print("Usuário cadastrado com sucesso!")
        except TypeError as error:
            print("Erro ao salvar arquivo: {error}.")
        except Exception as error:
            print("Ocorreu um erro inesperado: {error}.")

    def listar_todos_usuarios(self):
        return self.repository.listar_todos_usuarios()