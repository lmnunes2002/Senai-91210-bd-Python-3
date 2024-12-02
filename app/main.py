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
        print("3. Buscar usuário por ID")
        print("4. Atualizar email do usuário")
        print("5. Atualizar senha do usuário")
        print("6. Deletar usuário")
        print("7. Listar todos os usuários")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

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
        elif escolha == "2":
                email = input("Digite o email do usuário para busca: ")
                service.buscar_usuario_por_email(email)

        # Busca usuário por email.
        elif escolha == "3":
                email = input("Digite o id do usuário para busca: ")
                service.buscar_usuario_por_id(id)

        # Atualiza email do usuário.
        elif escolha == "4":
             novo_email = input("Digite o novo e-mail do usuário: ")
             Usuario.email = novo_email
             service.atualizar_usuario_email(Usuario)

        # Atualiza senha do usuário.
        elif escolha == "5":
             nova_senha = input("Digite a nova senha do usuário: ")
             Usuario.senha = nova_senha
             service.atualizar_usuario_senha(Usuario)

        # Deleta usuário.
        elif escolha == "6":
            nome = input("Digite o nome do usuário que deseja deletar: ")
            email = input("Digite o email do usuário que deseja deletar: ")
            senha = input("Digite a senha do usuário que deseja deletar: ")

            return UsuarioService.deletar_usuario(nome=nome, email=email, senha=senha)

        # Listar todos os usuários.
        elif escolha == "7":
            return UsuarioService.listar_todos_usuarios()
        
         # Sair
        elif escolha == "0":
            print("Saindo do sistema. Até logo!")
            break

if __name__ == "__main__":
    os.system("cls||clear")
    main()