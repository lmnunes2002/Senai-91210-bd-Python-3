import os
from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from models.usuario_model import Usuario
from config.database import Session

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    while True:
        print("\n--- Sistema de Gerenciamento de Usuários ---")
        print("1. Criar usuário")
        print("2. Buscar usuário por email")
        # print("3. Buscar usuário por ID")
        print("3. Atualizar email do usuário")
        print("4. Atualizar senha do usuário")
        print("5. Deletar usuário")
        print("6. Listar todos os usuários")
        print("7. Sair")

        escolha = int(input("Escolha uma opção: "))

        # Solicitando dados do usuário.
        if escolha == 1:
            print("\n--- Adicionar Usuário ---")
            nome = input("Digite o nome do usuário: ").strip()
            email = input("Digite o email do usuário: ").strip()
            senha = input("Digite a senha do usuário: ").strip()

            # Verificar se os campos obrigatórios estão preenchidos
            if not nome or not email or not senha:
                print("Erro: Todos os campos são obrigatórios!")
                return

            # Chamar o serviço para criar o usuário
            service.criar_usuario(nome, email, senha)
        
        # Busca usuário por email.
        elif escolha == 2:
                email = input("Digite o email do usuário para busca: ")
                service.buscar_usuario_por_email(email)

        # Atualiza email do usuário.
        elif escolha == 3:
            email = input("Informe o email do usuário a ser atualizado: ").strip()
            usuario = service.buscar_usuario_por_email(email)
            novo_email = input("Digite o novo e-mail do usuário: ").strip()

            if service.atualizar_usuario_email(novo_email, email):
                print("Atualização concluída com sucesso!")
            else:
                print("Falha ao atualizar o email.")

        # Atualiza senha do usuário.
        elif escolha == 4:
            email = input("Digite o email do usuário: ")
            usuario = service.buscar_usuario_por_email(email)
            nova_senha = input("Digite a nova senha do usuário: ").strip()

            if service.atualizar_usuario_senha(nova_senha, email):
                usuario.senha = input("Digite a nova senha do usuário: ")
                service.atualizar_usuario_senha(usuario)
            else:
                print("Usuário não encontrado")

        # Deleta usuário.
        elif escolha == 5:
            nome = input("Digite o nome do usuário que deseja deletar: ")
            email = input("Digite o email do usuário que deseja deletar: ")
            senha = input("Digite a senha do usuário que deseja deletar: ")

            return service.deletar_usuario(nome=nome, email=email, senha=senha)

        # Listar todos os usuários.
        elif escolha == 6:
            return service.listar_todos_usuarios()
        
         # Sair
        elif escolha == 7:
            print("Saindo do sistema. Até logo!")
            break

if __name__ == "__main__":
    os.system("cls||clear")
    main()