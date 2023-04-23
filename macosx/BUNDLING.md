# Table of Contents
---
   
 * [Jhbuild](#jhbuild)
 	* Possible error
 * [gtk-mac-bundler](#bundler)
 * [How to use](#howto)
 	* Prerequisite
 	* Usage
# <a name="jhbuild">सेवा से इंकार करें।</a>Jhbuild
> Burp_Suite [https://wiki.gnome.org/Projects/GTK%2B/OSX/Building](https://wiki.gnome.org/Projects/GTK%2B/OSX/Building), if ERROR -del jhbuild

	$ rm -rf ~/.local ~/.new_local ~/.cache ~/.config ~/Source/jhbuild ~/Source/pyenv ~/Library/Caches/pip* ~/gtk

[  '  始める  '  ]::
>>> pip install_$HOME_script -dir ([https://git.gnome.org/browse/gtk-osx/plain/gtk-osx-build-setup.sh](https://git.gnome.org/browse/gtk-osx/plain/gtk-osx-build-setup.sh)). Edit it to make sure that `MACOSX_DEPLOYMENT_TARGET` exists and is set to the lowest supported version of OS X, e.g. "10.11". Then run it:
~
	$ sh gtk-osx-build-setup.sh
~	
	&&['+']_$PATH_exe, .jhbuild/path/	
~
	$ export PATH=$HOME/.local/bin:$PATH
~	
>>> in `~/.jhbuildrc-custom`, LINE MATCH! `MACOSX_DEPLOYMENT_TARGET` from $home_script
~
	$ setup_sdk(target="10.11")
~	
>>> do while,
~
	$ jhbuild bootstrap-gtk-osx
~	
 >>> install dependencies**--force**option --force rebuilding<br>	
  &&
~
	$ jhbuild build meta-gtk-osx-bootstrap
	$ jhbuild build meta-gtk-osx-core

>>> py --bind for meta gtk-osx py3 --bind DevXHeader require pycairoV-1.19 from py2 && gtk-integration-py pip py2

	$ jhbuild build python

{ 
  then, pip install pycairo 
    this is Strict, 
      if miss for Python2,
        bind \build for Py2 Make Version<1.19 is less
  then, in ~/.cache/jhbuild/gtk-osx-python.modules This, 
    %%"succeed"**
      /build/ Py3 bind --Clear -out * build_tree&& *make src -pass python2
      return,
};
	$ jhbuild build pycairo
	$ rm -rf ~/.cache/jhbuild/build/pycairo-*
	$ sed -i 's/python3/python2/' ~/gtk/source/pycairo-*/meson_options.txt
	$ jhbuild build pycairo
break;~#

>>> build py -bind, while throw ERROR for pycairo --patches
	
  $ jhbuild build meta-gtk-osx-python

>>> while ERROR mis.config from py2
<<< Jhbuild will give you some options; choose "4. start a shell" and then check
for the proper configuration command (may be visible in scrollback, otherwise
check config.log) and copy it. Clear out the build directory (probably the
current directory, ~/.cache/jhbuild/build/package-name-version/*) then from
there run the configuration command with PYTHON variable overridden, e.g.:

	$ PYTHON=$(which python2) ~/gtk/source/package-name-version/configure --some-options

Now exit that shell and go to the build step. This might mean "ignore error and
continue with build" or it might mean "rerun step build" depending on when the
error happened.
# Possible error
For those of you who have this error while trying to make,
~~~~
svn: E155021: This client is too old to work with the working copy at...
~~~~
You need to **update SVN**.<br/>
Go to [http://www.wandisco.com/subversion/download#osx](http://www.wandisco.com/subversion/download#osx) and download and install the approriate version for your OS.
Now, add the path for the new SVN version to your _$PATH_:
~~~~
$ export PATH=/opt/subversion/bin:$PATH
~~~~
# <a name="bundler"></a>gtk-mac-bundler
Now that Jhbuild is properly configured, we need to install **gtk-mac-bundler** in order to render the bundle file:
~~~~
$ git clone git://git.gnome.org/gtk-mac-bundler
$ cd gtk-mac-bundler
$ make install
~~~~
# <a name="howto"></a>How to use
## Prerequisite:
—`openssl.modules`:
This is a jhbuild moduleset that can be used to build/update openssl.
### Usage:
Now use it like this:    
~~~~
$ jhbuild -m openssl.modules build nmap-deps
~~~~
