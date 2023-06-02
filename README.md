# SOLID PRINCIPLES
S-> en las clases definidas en models.py porque no se combinan clases de diferentes tareas, cada una realiza algo diferente 

O-> al igual que el pricipio L en models se puede cambiar lo que se quiere tener de info y usarla en todo el código y si se quiere cambiar algo de la info que se quiere obtener, sólo se modifica models y el código restante queda igual.

L-> porque si se desea guardar otros datos en las clases de models.py, únicamente se tendría modificar el campo de las clases sin modificar el funcionamiento de todo el código

I->en todo el proyecto porque ninguna clase depende de métodos que no usa 

D-> porque app.py no depende de ningún modulo de nivel inferior

# Design Patterns
Factory method-> en app.py en viene incializada la variable app en la cual se llama al método create_app para después utilizar el objeto variable para no llamar al constructor directamente.

flyweight-> en auth.py en sign-in se aplica porque si los datos que se meten en los campos no están registrados, se crea un nuevo usuario con esos datos, si sí están registrados aparece que ya está en uso y sirve para el login

Observer-> en login se utiliza porque cuando el usuario entra se notifica a sus dependientes como a la barra de navegación que cambia a logout si entra el usuario o viceversa, si hace logout se notifica para que regrese a la ventana de home y aparezca la opción de login.
