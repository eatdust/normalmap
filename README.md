
Normalmap generator
===

This code allows you to create a RGB [**normal
map**](https://en.wikipedia.org/wiki/Normal_mapping) from a
[**heightmap**](https://en.wikipedia.org/wiki/Heightmap). The output
picture is RGBA and you can store various combination of the height in
the Alpha channel.


Install & libraries
---

You need development files for recent imagemagick core versions (API7)
to be installed, as well as `pkg-config`. Then just do:

    $ waf configure

and then
    
    $ waf build
    
The binary **normalmap** is self-contained and generated within the directory
`build/`. Simply copy it wherever you like.

Old versions of imagemagick (API6) can be compiled by appending the
option `--oldmagick` to the configure script:

    $ waf configure --oldmagick

and then
    
    $ waf build


Original authors
---

* Richard Plangger (https://github.com/planrich/normalmap)

* The algorithm to compute the normal map comes from the gimp
normal map plugin, see (https://code.google.com/p/gimp-normalmap/).

License
---

[**GPLv2**](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html)
