#openpyxl

from openpyxl import Workbook
from openpyxl.styles import Font
import time


book = Workbook()
sheet = book.active

sheet['A1'] = "SKU"
sheet['A2'] = 1
sheet['A3'] = 2

sheet['B1'] = "Nombre"
sheet['B2'] = "Producto1"
sheet['B3'] = "Producto2"

sheet['C1'] = "Unidad"
sheet['C2'] = "Pieza"
sheet['C3'] = "Pieza"



book.save('demo.xlsx')
