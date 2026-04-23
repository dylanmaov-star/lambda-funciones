import tkinter as tk

# zona de clases
class InterfazAcceso:

    def __init__(self, ajuste_color):
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title("Panel de Registro")
        self.ventana_principal.geometry("500x500")
        
        
        self.color_fondo = "#2c3e50" 
        self.ventana_principal.config(bg=self.color_fondo)

        self.texto_notificacion = None

    def construir_interfaz(self):
        
        tk.Label(
            self.ventana_principal, 
            text="Ingrese Nombre del Usuario:", 
            bg=self.color_fondo, 
            fg="white"
        ).pack(pady=10)

        self.campo_entrada = tk.Entry(self.ventana_principal)
        self.campo_entrada.pack(pady=5)

        self.texto_notificacion = tk.Label(
            self.ventana_principal, 
            text="", 
            bg=self.color_fondo, 
            fg="#ecf0f1"
        )
        self.texto_notificacion.pack(pady=20)

        tk.Button(
            self.ventana_principal, 
            text="Confirmar Registro", 
            command=self.procesar_datos,
            bg="#27ae60",
            fg="white"
        ).pack(pady=5)

        tk.Button(
            self.ventana_principal, 
            text="Borrar Campos", 
            command=self.resetear_formulario,
            bg="#e74c3c",
            fg="white"
        ).pack(pady=5)

        return self.ventana_principal

    def procesar_datos(self):
        nombre_ingresado = self.campo_entrada.get()
        self.texto_notificacion.config(text=f"Registro exitoso: {nombre_ingresado}")

    def resetear_formulario(self):
        self.campo_entrada.delete(0, tk.END)
        self.texto_notificacion.config(text="")