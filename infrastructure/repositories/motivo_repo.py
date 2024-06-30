import json
import sqlite3
from typing import List, Optional
from domain.entities.motivo import Motivo
from infrastructure.sql.crud_motivo import *
from infrastructure.util.database import obter_conexao

motivos = []

class MotivoRepo:

    @classmethod
    def criar_tabela(cls,):
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_CRIAR_TABELA)
        except sqlite3.Error as ex:
            print(ex)
            
    @classmethod
    def inserir_dados(cls,):
        try:
            with open("infrastructure/data/motivos.json", 'r', encoding='utf-8') as f:
                dados = json.load(f)["motivos"]
                
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                
                cursor.execute(SQL_VERIFICAR_EXISTENCIA)
                resultado = cursor.fetchone()
                if resultado[0] > 0:
                    print("Os motivos já foram inseridos anteriormente.")
                    return  
                
                for motivo in dados:
                    nome = motivo["nome"]
                    cursor.execute(SQL_INSERIR, (nome,))
                    
                conexao.commit()
                print("Inserção de dados concluída com sucesso.")
        
        except sqlite3.Error as ex:
            print("Erro ao inserir dados:", ex)

    @classmethod
    def obter_motivos(cls) -> List[Motivo]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_OBTER_TODOS)
                resultados = cursor.fetchall()
                motivos = [(id, nome) for id, nome in resultados]
                return motivos
        except sqlite3.Error as ex:
            print(ex)
            return []
        
    @classmethod
    def selecionar_por_id(cls, id: str) -> Optional[Motivo]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(
                    SQL_SELECIONAR_POR_ID,
                    (
                        id,
                    )
                ).fetchone()
                if tupla is not None:
                    motivo = Motivo(*tupla)
                    return motivo
                else:
                    return None
        except sqlite3.Error as ex:
            print(ex)
            return None