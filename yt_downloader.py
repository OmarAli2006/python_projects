# Programa para descargar videos de YouTube
# De Omar Chanel Ali Fuertes

import flet as ft
import yt_dlp
import subprocess
import os
import threading

def is_ffmpeg_installed():
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        return True
    except FileNotFoundError:
        return False

def download_video(link, page: ft.Page, output_path="."):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        page.add(ft.Text("Descarga completada.", color=ft.Colors.GREEN))

    except Exception as e:
        page.add(ft.Text(f"Error al descargar el video: {e}", color=ft.Colors.RED))

def main(page: ft.Page):
    page.title = "YouTube Downloader"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    url_input = ft.TextField(label="Introduce el enlace del video de YouTube", width=400)
    download_button = ft.ElevatedButton("Descargar", on_click=None)
    output_path = "."  # Current directory as default

    def start_download(e):
        link = url_input.value.strip()
        if not link:
            page.add(ft.Text("Por favor, introduce un enlace.", color=ft.colors.RED))
            return

        if not is_ffmpeg_installed():
            page.add(
                ft.Text(
                    "FFmpeg no está instalado. Por favor, instálalo para poder unir el video y el audio.\n"
                    "Puedes descargarlo desde: https://ffmpeg.org/download.html\n"
                    "Después de instalarlo, asegúrate de que esté en tu PATH.",
                    color=ft.colors.RED,
                )
            )
            return

        page.add(ft.Text(f"Descargando video desde: {link}"))
        threading.Thread(target=download_video, args=(link, page, output_path), daemon=True).start()

    download_button.on_click = start_download

    page.add(
        url_input,
        download_button,
    )

if __name__ == "__main__":
    ft.app(target=main)


# Nota: Asegúrate de tener instalado yt-dlp y sus dependencias.