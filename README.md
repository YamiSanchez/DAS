# SOLID PRINCIPLES
S-> en las clases definidas en models.py porque no se combinan clases de diferentes tareas, cada una realiza algo diferente 

O-> al igual que el pricipio L en models se puede cambiar lo que se quiere tener de info y usarla en todo el código y si se quiere cambiar algo de la info que se quiere obtener, sólo se modifica models y el código restante queda igual.

L-> porque si se desea guardar otros datos en las clases de models.py, únicamente se tendría modificar el campo de las clases sin modificar el funcionamiento de todo el código

I->en todo el proyecto porque ninguna clase depende de métodos que no usa 

D-> porque app.py no depende de ningún modulo de nivel inferior

# Design Patterns
**Factory method**-> en app.py en viene incializada la variable app en la cual se llama al método create_app para después utilizar el objeto variable para no llamar al constructor directamente.

![image](https://github.com/YamiSanchez/DAS/assets/88749681/9a850e89-a7ce-4dbe-bc70-126c56462473)

Product base class or interface,en mi caso sería create_app().

Creator (el objeto app en app.py) declara el método de fábrica abstracta (create_app()) y utiliza el método de fábrica internamente para crear un producto, en este caso para crear la app.



**flyweight**-> en auth.py en sign-in se aplica porque si los datos que se meten en los campos no están registrados, se crea un nuevo usuario con esos datos, si sí están registrados aparece que ya está en uso y sirve para el login

![image](https://github.com/YamiSanchez/DAS/assets/88749681/cf029ddc-410c-4982-acd9-9cec7d71cd52)

cliente es el usuario y en sign-in envía datos en los objetos de email y usuario 

flyweightFactory son los campos de email y usuario, estos mandan la info y los comparan con los que ya están en la base de datos

flyweight dependiendo de si están o no, se decide que hacer, si no están se crea un nuevo objeto, si ya existe procede a dar un aviso de existente




**Observer**-> en login se utiliza porque cuando el usuario entra se notifica a sus dependientes como a la barra de navegación que cambia a logout si entra el usuario o viceversa, si hace logout se notifica para que regrese a la ventana de home y aparezca la opción de login.

![image](https://github.com/YamiSanchez/DAS/assets/88749681/e75ba913-7311-4ebc-a1b6-396dbdd60d46)

subject sería la barra de navegación en base.html que espera si el usuario hace login o logout para cambiar las opciones.

ConcreteObservers sería authenticated que se encuentra en base.html el cual checa el estado del usuario si es login o logout para avisar a la barra de navegacion cual es su estado actual.
