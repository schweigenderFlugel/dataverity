from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.exc import IntegrityError
from server.api.models.consultancy import Student, StudentCreate
from db import DatabaseDep
from clerk import AuthDep
from utils.csv_utils import csv_file