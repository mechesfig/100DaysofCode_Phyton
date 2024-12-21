print(r'''
  ooo,    .---.
 o`  o   /    |\________________
o`   'oooo()  | ________   _   _)
`oo   o` \    |/        | | | |
  `ooo'   `---'         "-" |_|
  ''')

print("Bienvenido a la Isla del Misterio.")
print("Tu misión es encontrar el tesoro.")
print("Estas en una intersección. ¿Qué camino tomarás?")
road = input('Escribe "d" para dirigirte hacia la derecha o "i" para la izquierda.\n').lower()
if road == "d":
    print("Has caido en un agujero. JUEGO TERMINADO. :(")
else:
    print('Debes cruzar un lago para llegar al castillo.')
    lake = input('Escribe "b" si deseas buscar una lancha para '
                 'cruzar el lago o "n" si deseas nadar.\n').lower()
    if lake == "n":
        print("Nadas demasiado lento. Has sido atacado por un cocodrilo. JUEGO TERMINADO. :(")
    else:
        print('Te encuentras frente al castillo. ¿Qué puerta abriras? ¿1, 2 o 3?')
        door = input('Escribe que puerta abrirás("1","2" o "3").\n').lower()
        if door == "1":
            print("Puerta equivocada. Has sido atacado por un jaguar. JUEGO TERMINADO. :(")
        elif door == "2":
            print("¡Felicidades! Has encontrado el tesoro.")
            print(r'''
                                 .* *.               `o`o`
                     *. .*              o`o`o`o      ^,^,^
                       * \               `o`o`     ^,^,^,^,^
                          \     ***        |       ^,^,^,^,^
                           \   *****       |        /^,^,^
                            \   ***        |       /
                ~@~*~@~      \   \         |      /
              ~*~@~*~@~*~     \   \        |     /
              ~*~@smd@~*~      \   \       |    /     #$#$#        .`'.;.
              ~*~@~*~@~*~       \   \      |   /     #$#$#$#   00  .`,.',
                ~@~*~@~ \        \   \     |  /      /#$#$#   /|||  `.,'
            _____________\________\___\____|_/______/_________|\/\___||______
            ''')
        else:
            print("Puerta equivocada. Has caido en una trampa. JUEGO TERMINADO. :(")