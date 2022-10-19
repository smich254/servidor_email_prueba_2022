# servidor_email_prueba_2022

- Que programas tener instalados?
	- Python (la ultima version)
	- Git (Para clonar el repositorio)
	- Navegador web (de preferencia Google chrome o Firefox)
- Cuales son los pasos a seguir?
	1. Creamos una carpeta donde estara nuestro proyecto
	2. Damos click derecho en la pantalla y elegimos la opcion de abrir en terminal
	3. Clonamos el repositorio, en la terminal, escribimos: 
		- git clone https://github.com/smich254/servidor_email_prueba_2022.git
	4. Una vez clonado el proyecto, accedemos a la carpeta que se creo, nos aseguramos de estar dentro de la carpeta y creamos un entorno virtual en python, para eso instalamos "pipenv", en la terminal escribimos:
		- pip install pipenv
	5. Una vez instalado el pipenv, activamos el entorno virtual, escribimos en la terminal:
		- pipenv shell
	6. Ahora procedemos a instalar los paquetes para que nuestro proyecto funcione, escribimos en la terminal
		- pip install -r requirements.txt
	7. Una vez instaldo los paquetes, ejecutamos nuestro programa, escribimos en la terminal
		- uvicorn main:app --reload 
	8. Esperamos a que cargue
		![[Pasted image 20221019064759.png]]
	9. Una vez cargo, abrimos nuestro navegador y escribimos: localhost:8000/docs
		![[Pasted image 20221019065007.png]]
	10. Desplegamos el apartado de POST, donde seleccionaremos Try it out
		![[Pasted image 20221019065232.png]]
	11. En la parte editable, llenamos tanto el correo de donde se enviara el mensaje, su contraseña (es la contraseña para aplicaciones de google), el destinatario, el asunto y en contenido del mensaje
		```
		{
		  "de": "escribe tu correo electronico",
		  "contras": "escribe tu contraseña de aplicaciones de google",
		  "para": "smich254@gmail.com",
		  "asunto": "Mensaje desde nuestro servidor de email",
		  "cuerpo": "Prueba exitosa"
		}
		```
	12. Luego le damos a "Execute" y revisamos nuestra terminal, si aparece "204 No Content", es porque se envio el mensaje
		![[Pasted image 20221019065629.png]]
	13. Revisamos nuestro correo, y listo, tenemos nuestro servidor de correos funcionanndo.
