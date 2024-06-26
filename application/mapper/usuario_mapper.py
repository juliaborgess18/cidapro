from application.dto.alterar_usuario_dto import AlterarUsuarioDTO 
from application.dto.criar_usuario_dto import CriarUsuarioDTO
from application.dto.visualizar_usuario_dto import VisualizarUsuarioDTO
from application.utils.auth import obter_hash_senha
from domain.entities.usuario import Usuario 
from domain.models.funcao_usuario import *

class UsuarioMapper:
    
    @classmethod
    def cadastrar_usuario(cls, usuario: CriarUsuarioDTO) -> Usuario:
        novo_usuario_db = Usuario()
        
        novo_usuario_db.nome            = usuario.nome                    
        novo_usuario_db.cpf             = usuario.cpf            
        novo_usuario_db.data_nascimento = usuario.data_nascimento
        novo_usuario_db.email           = usuario.email          
        novo_usuario_db.senha           = obter_hash_senha(usuario.senha)
        novo_usuario_db.funcao          = SOLICITANTE
        
        return novo_usuario_db   
    
    @classmethod
    def alterar_usuario(cls, usuario: AlterarUsuarioDTO) -> Usuario:
        usuario_alterado_db = Usuario()
        
        usuario_alterado_db.id              = usuario.id            
        usuario_alterado_db.nome            = usuario.nome            
        usuario_alterado_db.data_nascimento = usuario.data_nascimento
        usuario_alterado_db.email           = usuario.email  
        
        return usuario_alterado_db 
    
    @classmethod
    def visualizar_usuario(cls, usuario: Usuario) -> VisualizarUsuarioDTO:
        return VisualizarUsuarioDTO(id=str(usuario.id), nome=usuario.nome, cpf=usuario.cpf, data_nascimento=usuario.data_nascimento, email=usuario.email)
        