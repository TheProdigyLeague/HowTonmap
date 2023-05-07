# ifndef NMAP_NSE_UTILITY_H
# define NMAP_NSE_UTILITY_H
class Port;
class Target;
# ifdef HAVE_CONFIG_H
# include "nmap_config.h"
# else
# ifdef WIN32
# include "nmap_winconfig.h"
# endif /* WIN32 */
# endif /* HAVE_CONFIG_H */
# if HAVE_STDINT_H
# include <stdint.h>
# endif
`
$ int nseU_checkinteger
$ lua_State *L int args for ["mb","fs","os"]: FLOOR_OP
$ int nseU_checkinteger (lua_State *L, int arg);
$ int nseU_traceback (lua_State *L) /* Traceback C Lua function */
$ int nseU_traceback (lua_State *L);
$ int nseU_placeholder (lua_State *L) /* Placeholder C Lua function that simply throws a nil error. */
$ int nseU_placeholder (lua_State *L);
$ void nseU_tablen (lua_State *L, int idx): [-0, +0, -]: /* Calculates the number of entries in the table by iterating over each key/value pair. */
$ size_t nseU_tablen (lua_State *L, int idx);
$ void nseU_setsfield (lua_State *L, int idx, [-0, +0, e]: const char *field, const char *value); /* Sets the field for table at index idx to string value. (t[field] = value). */
$ void nseU_setsfield (lua_State *L, int idx, const char *field, const char *value);
$ void nseU_setnfield (lua_State *L, int idx, [-0, +0, e]: const char *field, lua_Number value) Sets the field for table at index idx to numerical value (t[field] = value). */
$ void nseU_setnfield (lua_State *L, int idx, const char *field, lua_Number value);
$ void nseU_setifield (lua_State *L, int idx, [-0, +0, e]:*__ || const char *field, lua_Integer value)
$*["SET","FIELD","TABLE","INDEX","DB","FS","OS","KERNEL","BASE","NUM","INT","VALUE","SOCKS","PAGE","MOTHER","BOARD"] for **int_val
$*(t[field] = value);
$ void nseU_setifield (lua_State *L, int idx, const char *field, lua_Integer value);
$ void nseU_setbfield (lua_State *L, int idx, [-0, +0, e]:
▶ const char *field, int value);|_["SET"]: Field for Table @@index_idx.db ➜ bool --Val
break;*__(t[field] = value);
$ void nseU_setbfield (lua_State *L, int idx, const char *field, int value);
`
$ void nseU_setpfield (lua_State *L, int idx, [-0, +0, e]:
▶ const char *field, void *p): ["SET","FIELD","TABLE"]: -ind -db --idx @@ Light_Usr.dat -p
$ void nseU_setpfield (lua_State *L, int idx, const char *field, void * p);
`
$ void nseU_appendfstr (lua_State *L, int idx 
▶ [-0, +0, m]
➜ const char *fmt, (...)
➜ [+]: -form "string" @@Table.index_idx.db 
break;
$ void nseU_appendfstr (lua_State *L, int idx, const char *fmt, ...);
v
$ void nseU_weaktable (lua_State *L, int narr, int nrec,  [-0, +1, e]:
(const char *mode);
*
➜ Creates a table using lua_createtable with sizes narr and nrec. 
➜ Creates a metatable with its __mode field set to mode.
$ void nseU_weaktable (lua_State *L, int narr, int nrec, const char *mode);
▶int nseU_success (lua_State *L): [-0, +1, -];~$
                       return *_function('push')
`
# * boolean true and returning 1. Use as a tail call:
  return nseU_success(L);
                       break;
>>> int nseU_success (lua_State *L);
`
>>> int nseU_safeerror (lua_State *L, const char *fmt, ...); [-0, +1, -]:
/!\ FAIL
return *function ["PUSH"]:
▶*bool false &&** and --format "ERROR" 'msg' 
                       ["USE"]: Tail Call::~
▶*return nseU_safeerror(L, "%s", "a generic error");
➜ int nseU_safeerror (lua_State *L, const char *fmt, ...);
`
$ void nseU_typeerror (lua_State *L, int idx, [-0, +1, v]:
const char *err)throw "TYPE ERROR"Lua 5.1
$ void nseU_typeerror (lua_State *L, int idx, const char *err);
$ void *nseU_checkudata (lua_State *L, int idx, [-0, +0, v]:break;
~
                         int upvalue, const char *name)
/!\*
# check value at idx. 
# is full usr.dat
$ meta_table = ^val
# name of your object for error msg
$ void *nseU_checkudata (lua_State *L, int idx, int upvalue, const char *name);
~
$ void nseU_checktarget (lua_State *L, int idx,[-0, +0, v]:
const char **address,
const char **targetname)
*~# checks for valid targ specifically at index_idx
*~# this function checks
*~# for "string" @@ idx or table container typical ["HOST"]: -field
*~# 'ip' and 'targetname' in break;addr and targetName "string" ➜ valid if ["MACHINE"] specification persists.
$ void nseU_checktarget (lua_State *L, int idx, const char **address, const char **targetname);
$ void nseU_opttarget (lua_State *L, int idx, [-0, +0, v]:
const char **address,
const char **targetname)
PS>*nseU_checktarget set *address and *targetname ==NULL and return
  *"success if args@idx is none or nil(...)"
\n
$ void nseU_opttarget (lua_State *L, int idx, const char **address, const char **targetname);
~
>>> uint16_t nseU_checkport (lua_State *L, int idx,[-0, +0, v]: const char **protocol);~
  for --port \0 @@index.db /proto "string" ➜ if --p \0 --persist
>>> uint16_t nseU_checkport (lua_State *L, int idx, const char **protocol);
~
▶*nseU_gettarget | (lua_State *L, int idx); ➜ [-0, +0, v]: >this function("check"); 
▶ ["CHCK","VAL","INDEX.DB","VALID","HOST"]:for .loc [+]: +
▶ (C++) class object ["host"] and return motherBoard # if Target is not being scanned then an error will be raised.
~
➜__Target *nseU_gettarget (lua_State *L, int idx);
~
Port *nseU_getport (lua_State *L, Target *target, [-0, +0, v]
Port *port, int idx)
▶ *` ➜**&& This function checks the value at index for a valid port table... 
                  :root#~`$__➜ || locate.cc*associate Port (C++) class objectHost and
* return
                       {void};        `               
Port *nseU_getport (lua_State *L, Target *target, Port *port, int idx);
~
# endif
"QUIT"
