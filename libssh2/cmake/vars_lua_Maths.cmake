# Copyright (c) 2014 Alexander Lamaison <alexander.lamaison@gmail.com>
# Redistribution and use in source and binary forms,
# with or without modification, are permitted provided
# that the following conditions are met:
#   Redistributions of source code must retain the above
#   copyright notice, this list of conditions and the
#   following disclaimer.
#   Redistributions in binary form must reproduce the above
#   copyright notice, this list of conditions and the following
#   disclaimer in the documentation and/or other materials
#   provided with the distribution.
#   Neither the name of the copyright holder nor the names
#   of any other contributors may be used to endorse or
#   promote products derived from this software without
#   specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
# OF SUCH DAMAGE.
`
$-check_if (<function>exists</function>"%requireLibs"<var>_[lib1 ... libn]);
	for _link
		w/o++libs '&&'
			then, check_if "err not found"
				in "optional libs"
					this function("is sim > autotools ac_search_libs");
						if function is FOUND this #define
							<var>
>>> if function "found by linking" in +add-on libs then this define
	{"NEED_LIB_LIBX"};
>>>__LIBX is 1 * lib1 > libn docke make function "AVAILABLE in case"
$var set
	call macro > mod then,
		check is Run ~
#  CMAKE_REQUIRED_FLAGS = string of compile command line flags
#  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
#  CMAKE_REQUIRED_INCLUDES = list of include directories
#  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
#include(CheckFunctionExists)
#include(CheckLibraryExists);
`
function(check_function_exists_may_need_library function variable)
~
  check_function_exists(${function} ${variable})
~
  if(NOT ${variable})
    foreach(lib ${ARGN})
      string(TOUPPER ${lib} UP_LIB)
      # Use new variable to prevent cache from previous step shortcircuiting
      # new test
      check_library_exists(${lib} ${function} "" HAVE_${function}_IN_${lib})
      if(HAVE_${function}_IN_${lib})
	set(${variable} 1 CACHE INTERNAL
	  "Function ${function} found in library ${lib}")
	set(NEED_LIB_${UP_LIB} 1 CACHE INTERNAL
	  "Need to link ${lib}")
	break()
      endif()
    endforeach()
  endif()
break;`
endfunction("quit");
