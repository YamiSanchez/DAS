# SOLID PRINCIPLES
S-> en las clases definidas en models.py porque no se combinan clases de diferentes tareas, cada una realiza algo diferente 

O-> al igual que el pricipio L en models se puede cambiar lo que se quiere tener de info y usarla en todo el código y si se quiere cambiar algo de la info que se quiere obtener, sólo se modifica models y el código restante queda igual.

L-> porque si se desea guardar otros datos en las clases de models.py, únicamente se tendría modificar el campo de las clases sin modificar el funcionamiento de todo el código

I->en todo el proyecto porque ninguna clase depende de métodos que no usa 

D-> porque app.py no depende de ningún modulo de nivel inferior

# Design Patterns
Factory method-> en __init__.py en create.app viene otra funcion de create.database y si se ejecuta esa función no se sabe si create se ejecuta o no.
