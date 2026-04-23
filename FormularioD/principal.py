from formulario import InterfazAcceso

# zona de codigo principal
if __name__ == "__main__":
    sistema = InterfazAcceso(None)
    sistema.construir_interfaz()
    
    sistema.ventana_principal.mainloop()