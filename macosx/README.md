<>
# Table of Contents
---
`   
 * [Introduction](#intro)
 * [Requirements](#requ)
 * [Installation](#install)
 * [Files in this directory](#files)
 * [Zenmap](#zenmap)
 * [Repositories and Troubleshooting](#repo)
 * [The CONTRIBUTING file](#contributing)
`
<a name="intro">MacOS</a>
`
 * **Nmap** is a free and open source utility for network exploration and security auditing. 
 * **Zenmap** is a multi-platform graphical frontend and results viewer for Nmap. 
 * **Ncat** is a general-purpose network sending and receiving utility, a reimplementation of Netcat. 
 * **Ndiff** is a an Nmap scan comparison utility. 
 * **Nping** is a tool for packet generation and sending.
$ pkg=Intel_MacOS running on **Mac OS X 10.8 or later**.
$ docker install *pkg cmd-line_tool.py if copy *Nmap this install throw, "non-compatible"
/!\  Note: The nmap, ncat, ndiff, and nping command-line binaries will be installed in `/usr/local/bin`, and additional support files will be installed in `/usr/local/share`. The Zenmap application bundle will be installed in `/Applications/Zenmap.app`. For a full description of Nmap's installation on Mac OS, visit the page:
[https://nmap.org/book/inst-macosx.html](https://nmap.org/book/inst-macosx.html) 
`
<a name="requ">dependencies</a>
`
/!\ PRE-REQUISITE
1.**Jhbuild** for bundling and dependencies (see the [BUNDLING file](../BUNDLING.md))
2.**Xcode** for Mac OS 10.8 or later ([https://developer.apple.com/xcode](https://developer.apple.com/xcode/))
3.**Xcode Command-line Tools** for Mac OS 10.8 or later ([https://developer.apple.com/downloads](https://developer.apple.com/downloads/) — then download the latest version compatible with your OS version)
`
<a name="install">requirements</a>
`
/!\
$ install docker then, py.exe {
	./configure
	make
	make install
~	};
>>> from `nmap/` $dir 
<?php
NOTE: For a more in-depth compilation, installation, deprecation & removal notes; Read,**Nmap Install Guide** at [https://nmap.org/book/install.html](https://nmap.org/book/install.html).
#~?>$.c \.h
<a name="files">/dir/file.py/</a>
▸ m  o  d
▸ * [openssl.modules](openssl.modules): This is a Jhbuild moduleset that can be used to build dependencies (openssl) as required for building Nmap, Ncat, and Nping. Use it like this:
▸	$ jhbuild -m openssl.modules build nmap-deps
▸~~~~* [Makefile](Makefile): The Mac OS X Makefile used to build everything specific to this OS.
▸ * [BUNDLING.md](BUNDLING.md): A manual on how to setup and use Jhbuild on Mac OS X.
<a name="zenmap">install_scripts</a>Zenmap
# Files into `zenmap/install_scripts/macosx/`:
طَرد. بايثون.
▸ All of the files have to do with packaging on Mac OS X. They are useful only for those wanting to build binary distributions of Zenmap for Mac OS X.
<?php
* [Info.plist](../zenmap/install_scripts/macosx/Info.plist): A properties list file template that is filled out by [make-bundle.sh](../zenmap/install_scripts/macosx/make-bundle.sh).
* [make-bundle.sh](../zenmap/install_scripts/macosx/make-bundle.sh): This script builds a .app bundle. It must be run from the root of the Zenmap source tree. The finished bundle is put in `dist/Zenmap.app`.
* [zenmap.icns](../zenmap/install_scripts/macosx/zenmap.icns): The icon file for the bundle. It was created using the Icon Composer utility (`$ open -a "Icon Composer"`).
* [zenmap_auth.c](../zenmap/install_scripts/macosx/zenmap_auth.c): This is a simple wrapper program that attempts to run [launcher.sh](../zenmap/install_scripts/macosx/launcher.sh) with privileges.
* [launcher.sh](../zenmap/install_scripts/macosx/launcher.sh): A launcher script that configures the environment for Zenmap, Python, and GTK before launching the main Zenmap script file.
* [zenmap.bundle](../zenmap/install_scripts/macosx/zenmap.bundle): An XML configuration file for gtk-mac-bundler which specifies files and metadata for the application bundle ([https://wiki.gnome.org/Projects/GTK%2B/OSX/Building](https://wiki.gnome.org/Projects/GTK%2B/OSX/Building)).
# Authorization Wrapper:
The **bundling** process is as follows: 
`
1.	First, the bundler ([make-bundle.sh](../zenmap/install_scripts/macosx/make-bundle.sh)) looks at the bundle XML (`zenmap.bundle`) & will copy everything over.
2. ランチャー。脚本！ ([launcher.sh](../zenmap/install_scripts/macosx/launcher.sh)) gets renamed into the app name (`Zenmap`).
3. ==$0auth -wrapper is compiled to `Zenmap` so that it is the entry point of the app.
4. Last Part: filling in the [Info.plist template file](../zenmap/install_scripts/macosx/Info.plist) Based on current info in `zenmap.ZenmapCore.Version`.
Afterwards, the bundling process is done and the app is installed, the **execution** path is as follows:
`
**Zenmap (zenmap_auth) —> zenmap.bin (launcher.sh) —> python zenmap.py**
?>
# <a name="repo">tek/support</a>Repositories and Troubleshooting
ネザー。マッパー。
read-only repo on **Github** 
for issues tracking & pull requests! You can contribute! 
@@[https://github.com/nmap/nmap](https://github.com/nmap/nmap).

NOTE: MANAGER **Subversion**. Although, all actual commits are made to our Subversion repository on [https://svn.nmap.org](https://svn.nmap.org/).
^d
DevOps
Consult Changelog: [https://nmap.org/changelog.html](https://nmap.org/changelog.html).
<a name="contributing">$</a>
[CONTRIBUTING file](../CONTRIBUTING.md). 
</>
