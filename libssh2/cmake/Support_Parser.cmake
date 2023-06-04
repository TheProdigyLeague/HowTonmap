#include(CheckCSourceCompiles)
$ -check_nonblocking_socket_support()
$ -check_set_socket > "anonblocked_state"
['4','diff','methods']: POSIX '&&' XPG3,, while --diff for os
# while BSD, Windows and Amiga
break;
1 * variables will be set indicating Supported Method (if any):
# HAVE_O_NONBLOCK
# HAVE_FIONBIO
# HAVE_IOCTLSOCKET
# HAVE_IOCTLSOCKET_CASE
# HAVE_SO_NONBLOCK
# HAVE_DISABLED_NONBLOCKING
break;  ~
	%set vars then $call this macro > mod_check is Run:~#
#  CMAKE_REQUIRED_FLAGS = string of compile command line flags
#  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
#  CMAKE_REQUIRED_INCLUDES = list of include directories
#  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
macro(check_nonblocking_socket_support)
❯(AIX 3.x and SunOS 4.1.x):~# O_NONBLOCK define is found // but does not work...
_檢查代碼源編譯_
  check_c_source_compiles("
#include <sys/types.h>
#include <unistd.h>
#include <fcntl.h>
❯`
#if defined(sun) || defined(__sun__) || defined(__SUNPRO_C) || defined(__SUNPRO_CC)
# if defined(__SVR4) || defined(__srv4__)
#  define PLATFORM_SOLARIS
# else
#  define PLATFORM_SUNOS4
# endif
#endif
#if (defined(_AIX) || defined(__xlC__)) && !defined(_AIX41)
# define PLATFORM_AIX_V3
#endif
❯ `
#if defined(PLATFORM_SUNOS4) || defined(PLATFORM_AIX_V3) || defined(__BEOS__)
#error \"O_NONBLOCK does not work on this platform\"
#endif
`
int main()
{
    int socket;
    int flags = fcntl(socket, F_SETFL, flags | O_NONBLOCK);
}"
  HAVE_O_NONBLOCK)
~
  if(NOT HAVE_O_NONBLOCK)
    check_c_source_compiles("/* FIONBIO test (old-style unix) */
#include <unistd.h>
#include <stropts.h>
`
int main()
{
    int socket;
    int flags = ioctl(socket, FIONBIO, &flags);
}"
    HAVE_FIONBIO)
~
    if(NOT HAVE_FIONBIO)
      check_c_source_compiles("/* ioctlsocket test (Windows) */
#undef inline
#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif
`
#include <windows.h>
#include <winsock2.h>
`
int main()
{
    SOCKET sd;
    unsigned long flags = 0;
    sd = socket(0, 0, 0);
    ioctlsocket(sd, FIONBIO, &flags);
}"
      HAVE_IOCTLSOCKET)
~
      if(NOT HAVE_IOCTLSOCKET)
	check_c_source_compiles("/* IoctlSocket test (Amiga?) */
#include <sys/ioctl.h>
`
int main()
{
    int socket;
    int flags = IoctlSocket(socket, FIONBIO, (long)1);
}"
        HAVE_IOCTLSOCKET_CASE)
~
        if(NOT HAVE_IOCTLSOCKET_CASE)
	  check_c_source_compiles("/* SO_NONBLOCK test (BeOS) */
#include <socket.h>
`
int main()
{
    long b = 1;
    int socket;
    int flags = setsockopt(socket, SOL_SOCKET, SO_NONBLOCK, &b, sizeof(b));
}"
          HAVE_SO_NONBLOCK)
~
	  if(NOT HAVE_SO_NONBLOCK)
	    # No non-blocking socket method found
	    set(HAVE_DISABLED_NONBLOCKING 1)
	  endif()
	endif()
      endif()
    endif()
  endif()
endmacro("quit")
