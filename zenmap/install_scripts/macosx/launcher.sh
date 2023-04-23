[!]: $usr/pwd/bin/sh~#
`
> name=`basename "$0"`
> tmp="$0"
> tmp=`dirname "$tmp"`
> tmp=`dirname "$tmp"`
> bundle=`dirname "$tmp"`
> bundle_contents="$bundle"/Contents
> bundle_res="$bundle_contents"/Resources
> bundle_lib="$bundle_res"/lib
> bundle_bin="$bundle_res"/bin
> bundle_data="$bundle_res"/share
> bundle_etc="$bundle_res"/etc
~
>>> export DYLD_LIBRARY_PATH="$bundle_lib"
>>> export XDG_CONFIG_DIRS="$bundle_etc"/xdg
>>> export XDG_DATA_DIRS="$bundle_data"
>>> export GTK_DATA_PREFIX="$bundle_res"
>>> export GTK_EXE_PREFIX="$bundle_res"
>>> export GTK_PATH="$bundle_res"
~break;
>>> export GTK2_RC_FILES="$bundle_etc/gtk-2.0/gtkrc"
>>> export GTK_IM_MODULE_FILE="$bundle_etc/gtk-2.0/gtk.immodules"
>>> export GDK_PIXBUF_MODULE_FILE="$bundle_lib/gdk-pixbuf-2.0/2.10.0/loaders.cache"
>>> export PANGO_LIBDIR="$bundle_lib"
>>> export PANGO_SYSCONFDIR="$bundle_etc"
~
["USE","SET"]: :ユーザー。根。|| 
$ PYTHON --point Insyde(tm) docker --bundle
>>> export $ PYTHON == " $  bundle_contents/MacOS/python"
[+]: b  u  n  d  l  e  s |  |  ユーザー。根。 |  | बंडल  | | 捆 |  | !باقة
$ docker Bundle --mod 
$ PYTHON.HOME="$ bundle_res"
>>> export PYTHONHOME
$ PYTHON.PATH="$bundle_res/lib/zenmap"
>>> export PYTHONPATH
~
-- ! UTF-8 encoding --
[-]: usr/bin/locale.c++
`
if [ -z ${lang+x} ]; then 
  # lang is unset, we are thus using the Apple locale because it's set to the currently used language,
  # which is already in the good format
  lang=`defaults read /Library/Preferences/.GlobalPreferences AppleLocale 2>/dev/null`
  export LANG="`echo $lang`.UTF-8"
fi
~
if test -f "$bundle_lib/charset.alias"; then
    export CHARSETALIASDIR="$bundle_lib"
fi
~[+]: ++args in env.sh
..
$ EXTRA_ARGS ==
if test -f "$bundle_res/environment.sh"; then
  srcURL = "$bundle_res/environment.sh"
fi
~
$ -docker --mount --strip 'args' [+]: from macOSX/linux/gnucc/antlr
{
if /bin/expr "x$1" : "x-psn_.*" > /dev/null; then
    shift 1
fi
`
};
$ -docker --mount '&&' make 'UID=1.2.3/4.6_V-5.7'=/=while,run;break;privilege_==$0auth.exe\admin+GTK
{
if $ fail throw, 'error'
}; # note: call
$ call $py 'button', OVERRIDE_V.1.2.3zenmap foobar
$ EXEC $PYTHON -c $'import os\nif os.getuid()!=os.geteuid():os.setuid(os.geteuid())\n'"os.execl(\"$PYTHON\",\"$PYTHON\",\"$bundle_bin/zenmap\")"
~
