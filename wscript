

def options(c):
    c.load("compiler_c")
    c.add_option('--oldmagick',action='store_true',default=False,
	help='compile with ImageMagick 6 API')

def configure(c):
    c.load("compiler_c")
    c.check_cfg(package='MagickCore', args='--cflags --libs', uselib_store='MAGICK_CORE')
    c.env.CFLAGS += ['-std=c11']
    if c.options.oldmagick:
       c.env.CFLAGS += ['-DMAGICK6']

def build(c):
    c.program(source='src/normalmap.c src/main.c',
        target='normalmap',
        use='MAGICK_CORE',
        lib='m',
        includes='src')
