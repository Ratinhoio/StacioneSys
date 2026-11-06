from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI(title = "Sistema de Estacionamento")

BANCO = "estacionamento.db"

