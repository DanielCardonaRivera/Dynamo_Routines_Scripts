# Importar las bibliotecas necesarias
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, View

# Obtener el documento activo
doc = DocumentManager.Instance.CurrentDBDocument

# Obtener todas las vistas en el documento
views = FilteredElementCollector(doc).OfClass(View).ToElements()

# Lista de nuevos nombres para las vistas
nuevos_nombres = ["Vista 1", "Vista 2", "Vista 3"]  

# Renombrar las vistas
for i, vista in enumerate(views):
    if i < len(nuevos_nombres):
        try:
            vista.Name = nuevos_nombres[i]
            # Guardar cambios
            TransactionManager.Instance.EnsureInTransaction(doc)
            doc.Regenerate()
            TransactionManager.Instance.TransactionTaskDone()
        except Exception as e:
            print(f"Error al renombrar la vista {vista.Id}: {e}")

# Salida
OUT = "Vistas renombradas exitosamente."
