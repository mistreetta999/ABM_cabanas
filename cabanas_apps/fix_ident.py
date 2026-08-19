import os

# Carpeta raíz del proyecto
root_dir = r"C:\Users\carol\OneDrive\Desktop\cabanas"

# Texto a eliminar
target_line = '"cabanas_apps.cabanas_app",'

# Recorrer todos los archivos .py dentro del proyecto
for subdir, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(subdir, file)
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            # Filtrar las líneas que no contengan la frase
            new_lines = [line for line in lines if target_line not in line]

            # Si hubo cambios, sobrescribir el archivo
            if len(new_lines) != len(lines):
                with open(file_path, "w", encoding="utf-8") as f:
                    f.writelines(new_lines)
                print(f"✅ Limpieza aplicada en: {file_path}")
