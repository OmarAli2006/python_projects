import flet as fl
from rembg import remove
from PIL import Image
import os
import io

def main(page: fl.Page):
    page.title = "Remover Fondos Imagenes"
    page.vertical_alignment = fl.MainAxisAlignment.CENTER
    page.horizontal_alignment = fl.CrossAxisAlignment.CENTER
    page.padding = 20
# funciones
    
    input_path = None

    def pick_file_result(e: fl.FilePickerResultEvent):
        if e.files:
            input_path_text.value = e.files[0].path
            nonlocal input_path
            input_path = e.files[0].path

            with open(input_path, "rb") as img_file:
                preview.src = input_path
                preview.visible = True
            page.update()
            proccess_btn.disabled = False
            page.update()

    def save_file_result(e: fl.FilePickerResultEvent):
        if not e.path or not input_path:
            return
        status.visible = True
        status.value = "Procesando imagen..."
        progress_bar.visible = True
        page.update()
        try:
            input_img = Image.open(input_path)
            output_img = remove(input_img)
            if not e.path.endswith(".png"):
                e.path += ".png"
            output_img.save(e.path, format="PNG")
            status.value = "Imagen procesada con éxito"
            status.color = fl.Colors.GREEN_500

            # Show notification dialog
            def view_image(_):
                os.startfile(e.path)  # Open the processed image
                notification_dialog.open = False
                page.update()

            def close_notification(_):
                notification_dialog.open = False
                page.update()

            notification_dialog = fl.AlertDialog(
                title=fl.Text("Imagen procesada con éxito"),
                content=fl.Text("¿Qué deseas hacer ahora?"),
                actions=[
                    fl.ElevatedButton("Ver Imagen", on_click=view_image),
                    fl.ElevatedButton("Cerrar", on_click=close_notification),
                ],
                actions_alignment=fl.MainAxisAlignment.END,
            )
            page.dialog = notification_dialog
            notification_dialog.open = True
            page.update()  # Ensure the page is updated to show the dialog

        except Exception as ex:
            status.value = f"Error: {str(ex)}"
            status.color = fl.Colors.RED_500

        progress_bar.visible = False
        page.update()


    pick_files_dialog = fl.FilePicker(
        on_result = pick_file_result
    )

    save_file_dialog = fl.FilePicker(
        on_result = save_file_result
    )

    page.overlay.extend([pick_files_dialog, save_file_dialog])

#interfaz
    title = fl.Text(
        "Remover Fondos Imagenes",
        size=30,
        weight=fl.FontWeight.BOLD,
        text_align=fl.TextAlign.CENTER,
    )
    subtitle = fl.Text(
        "Sube una imagen y remueve el fondo fácilmente",
        size=16,
        weight=fl.FontWeight.NORMAL,
        text_align=fl.TextAlign.CENTER,
    )
    input_path_text = fl.Text(
        value="No se ha encontrado ninguna imagen",
        color=fl.Colors.GREY_400,
        size=16,
        weight=fl.FontWeight.NORMAL,
        tooltip="Ruta de la imagen seleccionada",
    )
    select_btn = fl.ElevatedButton(
        text="Seleccionar Imagen",
        icon=fl.Icons.FILE_UPLOAD,
        tooltip="Haz clic para seleccionar una imagen",
        on_click=lambda _: pick_files_dialog.pick_files(
            file_type=fl.FilePickerFileType.IMAGE,
        ),
    )

    preview = fl.Image(
        width=300,
        height=300,
        fit=fl.ImageFit.CONTAIN,
        visible=False,
        border_radius=fl.BorderRadius(10, 10, 10, 10),
        tooltip="Vista previa de la imagen seleccionada",
    )

    status = fl.Text(
        visible=False,
        text_align=fl.TextAlign.CENTER,
        size=14,
    )

    progress_bar = fl.ProgressBar(
        width=300,
        visible=False,
        tooltip="Progreso del procesamiento de la imagen",
    )

    proccess_btn = fl.ElevatedButton(
        text="Procesar y Guardar",
        icon=fl.Icons.SAVE,
        disabled=True,
        tooltip="Procesa la imagen seleccionada y guarda el resultado",
        on_click=lambda _: save_file_dialog.save_file(
            file_type=fl.FilePickerFileType.ANY,
            allowed_extensions=[".png"],
            file_name="output.png",
        ),
    )

    page.add(
        fl.Column(
            controls=[
                title,
                subtitle,
                fl.Divider(height=20),
                select_btn,
                input_path_text,
                fl.Divider(height=20),
                preview,
                progress_bar,
                proccess_btn,
                status,
            ],
            horizontal_alignment=fl.CrossAxisAlignment.CENTER,
            spacing=20,  # Add spacing between elements
        )
    )

fl.app(target=main)