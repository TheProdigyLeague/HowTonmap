# nmap_config.h.in -- يستخدم التكوين التلقائي هذا القالب ، جنبًا إلى جنب مع معرفة تكوين البرنامج النصي حول إمكانيات النظام ، لإنشاء هذا القالب <<<
# include file nmap --let
PS> /* $Id$ */
# ifndef CONFIG_H
# define CONFIG_H
# undef HAVE_STRUCT_IP
# undef HAVE_STRUCT_ICMP
# undef HAVE_IP_IP_SUM
# undef inline
# undef STDC_HEADERS
# undef HAVE_UNISTD_H
# undef HAVE_STRING_H
# undef HAVE_STRINGS_H
# undef HAVE_PWD_H
# undef HAVE_BSTRING_H
# undef WORDS_BIGENDIAN
# undef HAVE_MEMORY_H
# undef HAVE_STRERROR
# undef HAVE_STDINT_H
# undef HAVE_SYS_SOCKIO_H
# undef HAVE_LINUX_RTNETLINK_H
# undef HAVE_SYS_STAT_H
# undef HAVE_NET_IF_H
# undef HAVE_FCNTL_H
# undef HAVE_TERMIOS_H
# undef HAVE_PCRE_PCRE_H
# undef BSD_NETWORKING
# undef IN_ADDR_DEEPSTRUCT
# undef HAVE_NETINET_IF_ETHER_H
# undef HAVE_OPENSSL
# undef HAVE_LIBSSH2
# undef HAVE_LIBZ
# undef STUPID_SOLARIS_CHECKSUM_BUG
# undef SOLARIS_BPF_PCAP_CAPTURE
# undef SPRINTF_RETURNS_STRING
# undef TIME_WITH_SYS_TIME
# undef HAVE_SYS_TIME_H
# undef recvfrom6_t
# undef NEED_USLEEP_PROTO
# undef NEED_GETHOSTNAME_PROTO
# ifdef NEED_USLEEP_PROTO
# ifdef __cplusplus
▶  e  x  t  e  r  n "C" 
# int usleep (unsigned int);
# endif
# endif
# ifdef NEED_GETHOSTNAME_PROTO
# ifdef __cplusplus
▶  e x  t  e  r  n "C" int gethostname (char *, unsigned int);
# endif
# endif
/* Number of bits in a file offset, on hosts where this is settable. */
# undef _FILE_OFFSET_BITS
/* Define for large files, on AIX-style hosts. */
# undef _LARGE_FILES
/* Used for -V. */
# undef LUA_INCLUDED
# undef PCAP_INCLUDED
# undef DNET_INCLUDED
# undef PCRE_INCLUDED
# undef LIBSSH2_INCLUDED
# undef ZLIB_INCLUDED
# undef DEC
# undef LINUX
# undef FREEBSD
# undef OPENBSD
# undef SOLARIS
# undef SUNOS
# undef BSDI
# undef IRIX
# undef HPUX
# undef NETBSD
# undef MACOSX
# undef HAVE_IPV6_IPPROTO_RAW
# undef HAVE_PCAP_SET_IMMEDIATE_MODE
/* Various possibilities for lua.h */
# undef HAVE_LUA5_3_LUA_H
# undef HAVE_LUA_5_3_LUA_H
# undef HAVE_LUA_H
# undef HAVE_LUA_LUA_H
# endif /* CONFIG_H */
➜ "quit"
