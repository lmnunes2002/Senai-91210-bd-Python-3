from models.usuario_model import Usuario
from sqlalchemy.orm import Session

class UsuarioRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def salvar_usuario(self, usuario: Usuario):
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)
    
    def pesquisar_usuario_por_email(self, email: str):
        return self.session.query(Usuario).filter_by(email= email).first()

    def atualizar_usuario(self, usuario: Usuario):
        self.session.commit()
        self.session.refresh(usuario)

    def deletar_usuario(self, usuario: Usuario):
        self.session.delete(usuario)
        self.session.commit()

    def listar_todos_usuarios(self):
        lista_usuarios = self.session.query(Usuario).all()
        return lista_usuarios