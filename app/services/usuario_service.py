from models.usuario_model import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository) -> None:
        self.repository = repository

    # Create.
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

    # Read.
    def buscar_usuario_por_email(self, email: str):
        try:
            usuario = self.repository.pesquisar_usuario_por_email(email)

            if usuario:
                print(f"Usuário encontrado: {usuario.id} - {usuario.nome} - {usuario.email}")
                return usuario
            else:
                print("Usuário não encontrado")
        except Exception as error:
            print("Ocorreu um erro inesperado: {error}.")

    # Update.
    def atualizar_usuario_email(self, novo_email: str, email: str):
        try:
            usuario = self.repository.pesquisar_usuario_por_email(email)

            if not usuario:
                print("Usuário não encontrado.")
                return False

            usuario.email = novo_email

            atualizado = self.repository.atualizar_usuario(usuario)
            
            if atualizado:
                print("Email do usuário atualizado com sucesso!")
                return True
            else:
                print("Falha ao atualizar o email do usuário. Verifique a persistência.")
                return False
        except Exception as error:
            print(f"Ocorreu um erro ao atualizar o email do usuário: {error}")
            return False

    def atualizar_usuario_senha(self, nova_senha: str, email: str):
        try:
            usuario = self.repository.pesquisar_usuario_por_email(email)

            if not usuario:
                print("Usuário não encontrado.")
                return False
            
            usuario.senha = nova_senha

            atualizado = self.repository.atualizar_usuario(usuario)

            if atualizado:
                print("Senha do usuário atualizado com sucesso!")
                return True
            else:
                print("Falha ao atualizar a senha do usuário.")
                return False
        except Exception as error:
            print(f"Ocorreu um erro ao atualizar a senha do usuário: {error}")

    # Delete.
    def deletar_usuario(self, nome:str, email:str, senha:str):
        try:
            usuario = self.repository.pesquisar_usuario_por_email(email)

            if usuario:
                self.repository.deletar_usuario(usuario = usuario)
                return True 
            else:
                print("Usuário não encontrado no bancdo de dados.")
                return False
        except Exception as error:
            print(f"Ocorreu um erro inesperado: {error}.")

    # Validação
    def listar_todos_usuarios(self):
        return self.repository.listar_todos_usuarios()