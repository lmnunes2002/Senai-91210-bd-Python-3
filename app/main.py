import os
from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
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
            try:
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
            except ValueError as ve:
                print(f"Erro de validação: {ve}")
            except TypeError as te:
                print(f"Erro de tipo: {te}")
            except Exception as e:
                print(f"Erro inesperado: {e}")
        
    # # Busca usuário por email.
    # elif escolha == "2":
    #         email = input("Digite o email do usuário para busca: ")
    #         service.buscar_usuario_por_email(email)

    # # Exibindo dados dos usuários.
    # elif escolha == 7:
    #     print("\nListando usuários cadastrados: ")
    #     lista_usuarios = service.listar_todos_usuarios()

    #     for usuario in lista_usuarios:
    #         print(f"\nNome: {usuario.id} \nE-mail: {usuario.email} \nSenha: {usuario.senha}\n")

if __name__ == "__main__":
    os.system("cls||clear")
    main()