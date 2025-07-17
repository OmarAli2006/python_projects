import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "Mi lista de tareas"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text(value="MI LISTA DE TAREAS EN FLET",
                     size=30, weight=ft.FontWeight.BOLD, color='white')
    
    def agregar_tarea(e):
        if campo_tarea.value:
            tarea = ft.ListTile(title=ft.Text(campo_tarea.value),
                                leading=ft.Checkbox(on_change=seleccionar_tarea))
                                
            tareas.append(tarea)
            campo_tarea.value = ""
            actualizar_lista()

    def seleccionar_tarea(e):
        seleccionadas = [t.title.value for t in tareas if t.leading.value]
        tareas_seleccionadas.value = "Tareas Seleccionadas: " + ", ".join(seleccionadas)
        page.update()

    def actualizar_lista():
        list_tareas.controls.clear()
        list_tareas.controls.extend(tareas)
        page.update()

    campo_tarea = ft.TextField(hint_text="Escribe una nueva tarea", color='white')
    boton_tarea = ft.FilledButton(text="Agregar Tarea", on_click=agregar_tarea)

    list_tareas = ft.ListView(expand=1, spacing=3)

    tareas = []
    tareas_seleccionadas = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD, color='white')
    
    page.add(titulo, campo_tarea, boton_tarea, list_tareas, tareas_seleccionadas)

ft.app(target=main)