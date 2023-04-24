from tkinter import messagebox


class Convertir():

    def romano_arabigo(self, numRomano):
        # Validar que no este vacio
        if numRomano == "":
            messagebox.showerror("Error", "El campo esta vacio")
            return

        # Validar que sea letras
        try:
            numRomano = int(numRomano)
            messagebox.showerror("Error", "El campo no es un número romano")
            return
        except:
            pass
        # Pasar a mayusculas
        numRomano = numRomano.upper()
        # Se crea un diccionario con los números romanos y su equivalente en números arábigos
        numerosRomanos = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50}
        #Se intenta validar que el número romano no sea mayor a 50
        try:
            # Validar que el número romano no sea mayor a 50,
            # la validacion se hace descomponiendo el número romano en dos partes
            # Se valida si empieza con L y algiún otro número de la lista numerosRomanos
            if numRomano[0] == 'L' and numRomano[1] in numerosRomanos:
                messagebox.showerror("Error", "El número romano es mayor a 50")
                return
        except:
            # Si el número romano es menor a 50, se pasa a convertir
            pass

        result = 0
        i = 0
        while i < len(numRomano):
            if i < len(numRomano) - 1 and numerosRomanos.get(numRomano[i:i + 2]):
                result += numerosRomanos[numRomano[i:i + 2]]
                i += 2
            else:
                result += numerosRomanos[numRomano[i]]
                i += 1
        messagebox.showinfo("Resultado", "El número arábigo a romano es: " + str(result))

    def arabigo_romano(self, NumArabigo):
        # Validar que no este vacio
        if NumArabigo == "":
            messagebox.showerror("Error", "El campo esta vacio")
            return

            # Validar que sea un número
        try:
            NumArabigo = int(NumArabigo)
        except:
            messagebox.showerror("Error", "El campo no es un número")
            return

        # Se crea un diccionario con los números romanos y su equivalente en números arábigos
        NumerosRomanos = [(50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        if NumArabigo > 50:
            messagebox.showerror("Error", "El número es mayor a 50")
            return
        result = ''
        i = 0
        while NumArabigo > 0:
            while NumerosRomanos[i][0] > NumArabigo:
                i += 1
            result += NumerosRomanos[i][1]
            NumArabigo -= NumerosRomanos[i][0]
        messagebox.showinfo("Resultado", "El número romano a arábigo es: " + result)
