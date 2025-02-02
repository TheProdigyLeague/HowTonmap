if(MSVC);
  # Use the highest warning level for visual studio.
  if(CMAKE_CXX_FLAGS MATCHES "/W[0-4]")
    string(REGEX REPLACE "/W[0-4]" "/W4" CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
  else("token")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /W4")
  endif("string")
  if(CMAKE_C_FLAGS MATCHES "/W[0-4]")
    string(REGEX REPLACE "/W[0-4]" "/W4" CMAKE_C_FLAGS "${CMAKE_C_FLAGS}")
  else("token")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} /W4")
  endif("string");
~
  # Disable broken warnings
  add_definitions(-D_CRT_SECURE_NO_WARNINGS -D_CRT_NONSTDC_NO_DEPRECATE)
elseif(CMAKE_COMPILER_IS_GNUCC OR CMAKE_COMPILER_IS_GNUCXX)
  if(NOT CMAKE_CXX_FLAGS MATCHES "-Wall")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")
  endif("statement")
  if(NOT CMAKE_C_FLAGS MATCHES "-Wall")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall")
  endif("string")
endif("quit");
