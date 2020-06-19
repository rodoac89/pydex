# PyDex Beta
Pokédex en consola de Python

**Nota: Esta aplicación no está afiliada ni con Nintendo ni con The Pokémon Company.**

## Instalación de módulos necesarios de PyDex y comprobación de datos

* Ejecutar: `pip install -r requirements.txt` para instalar los módulos.

## PyDex soporta argumentos opcionales

* `python pydex.py -s [--scrap]` Para descargar las imagénes desde el sitio oficial de Pokémon (opcional)
* `python pydex.py -c [--check]` Para verificar la integridad de los datos y si la base de datos se encuentra dentro del directorio
* `python pydex.py -p POKE[-pPOKE, --pokemon=POKE]` carga los datos del pokemon sin encender PyDex (opcional)

## Uso de Pydex
Para encender PyDex se debe ejecutar: `python pydex.py`

Una vez iniciado sólo debe escribir el nombre del pokémon deseado y precionar `Enter`.

PyDex traerá la información del Pokémon deseado y mostrará la imagen del Pokémon en `ASCII`. Si no la tiene, PyDex la descargará automáticamente desde el sitio oficial de pokemon.

Por ejemplo, si su pokémon buscado es **Latias** el resultado será:


```
Imagen del Pokémon: 

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@&AsiAS@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@B3AX:,.;h@@@@hG@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@A;,,iri,:ri;;;iX5#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@Mr::;irsr,   ,:AXA9@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@HX;;i,sr:,.:XM@&X5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@Xi:,,....X@@@9s2@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@&s,.....:3@@#A5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@5;.....,2@SA5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@&i ... .sBA2&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@r....  iX2#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@s. ....  ;XAX3@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@&h552535;,.........;;;sH&&&@@@@@@@@@@@@@@@@@@@@@@@
@@@@@S5AAAA232sri,..,. .,,rrrXXXXXXXXXXXXXXAAAA25M&@@@@@
@@@@@#HH@@@@@@XrXs:..,. .::rsssssssssXXXAAA2XXX5hM&@@@@@
@@@@@@@@@@@@@@3rsssr;:::,;rrrs53hhHG#&@@@@@@@&&H&@@@@@@@
@@@@@@@@@@@@@@@5sssssrrssXXsX2&@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@&hXsrrsssXssXX5@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@#HM3535522XsssA@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@MssAh@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@GsrsAH@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@9srXrs3@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@53hM35#@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


Numero del Pokémon:  380
Sus tipos son: 
  -  Dragon
  -  Psychic
Género único:
  - Hembra
Otras formas del Pokémon: 
  -  Mega Latias
Movimientos que puede aprender el pokémon: 
  -  Aerial Ace
  -  Ally Switch
  -  Attract
  -  Body Slam
  -  Bulldoze
  -  Calm Mind
  -  Captivate
  -  Charge Beam
  -  Charm
  -  Confide
  -  Covet
  -  Cut
  -  Defog
  -  Dive
  -  Double-Edge
  -  Double Team
  -  Draco Meteor
  -  Dragon Breath
  -  Dragon Claw
  -  Dragon Pulse
  -  Dream Eater
  -  Earthquake
  -  Endure
  -  Energy Ball
  -  Facade
  -  Flash
  -  Fly
  -  Frustration
  -  Fury Cutter
  -  Giga Impact
  -  Grass Knot
  -  Guard Split
  -  Healing Wish
  -  Heal Pulse
  -  Helping Hand
  -  Hidden Power
  -  Hone Claws
  -  Hyper Beam
  -  Ice Beam
  -  Icy Wind
  -  Laser Focus
  -  Last Resort
  -  Light Screen
  -  Magic Coat
  -  Magic Room
  -  Mimic
  -  Mist Ball
  -  Mud-Slap
  -  Natural Gift
  -  Outrage
  -  Protect
  -  Psychic
  -  Psycho Shift
  -  Psych Up
  -  Psyshock
  -  Psywave
  -  Rain Dance
  -  Recover
  -  Reflect
  -  Reflect Type
  -  Refresh
  -  Rest
  -  Retaliate
  -  Return
  -  Roar
  -  Role Play
  -  Roost
  -  Round
  -  Safeguard
  -  Sandstorm
  -  Secret Power
  -  Shadow Ball
  -  Shadow Claw
  -  Shock Wave
  -  Sleep Talk
  -  Snore
  -  Solar Beam
  -  Steel Wing
  -  Stored Power
  -  Substitute
  -  Sucker Punch
  -  Sunny Day
  -  Surf
  -  Swagger
  -  Swift
  -  Tailwind
  -  Telekinesis
  -  Thunder
  -  Thunderbolt
  -  Thunder Wave
  -  Toxic
  -  Trick
  -  Twister
  -  Waterfall
  -  Water Pulse
  -  Water Sport
  -  Whirlpool
  -  Wish
  -  Zen Headbutt
```
## Agradecimientos
@ahumeniy por la sugerencia de descarga de imágenes bajo demanda
