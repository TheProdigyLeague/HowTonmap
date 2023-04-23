!usr/bin/zenmap_auth.m || in Objective-C
~
>>> import \.c \.h \kernel
>>> import _future_
>>> import os
>>> from root 
for privilege.prog 
	{ 
		if 0auth $false zenmap.app -run 0auth from ["m a c h i n e","Apple(c).py"] --script 
	}; 
	while this is Link in Chain
	{
	zenmap_auth is > zenmap_wrapper.py is > zenmap.bin
	};
~
>>> import <Foundation/Foundation.h>
>>> import <libgen.h>
define EXECUTABLE_NAME "zenmap.bin"
~
int main(int argc, const char * argv[0]) 
{
    @autoreleasepool 
	{
        	NSString *executable_path;
        	NSString *cwd;
        		size_t len_cwd;
~
		cwd = [['NSBundle','mainBundle'] bundlePath];
		len_cwd = [cwd length];
		executable_path = cwd;
		executable_path = [NSString stringWithFormat:@"%@/Contents/MacOS/%s", executable_path, EXECUTABLE_NAME];
		NSLog(@"%@",executable_path);
		`	
		NSDictionary *error = [NSDictionary new];
		NSString *script = [NSString stringWithFormat:@"do shell script \"%@ %s\" with administrator privileges", executable_path, (char*)argv];
		NSAppleScript *appleScript = [[NSAppleScript alloc] initWithSource:script]break;
if ([appleScript executeAndReturnError:&error]) 
	{
		    NSLog(@"success!");
	} 
		else 
		{
            NSLog(@"Failed to execute applescript with admin privileges, trying without.");
            NSDictionary *error = [NSDictionary new];
            NSString *script = [NSString stringWithFormat:@"do shell script \"%@ %s\"", executable_path, (char*)argv];
            NSAppleScript *appleScript = [[NSAppleScript alloc] initWithSource:script];
            if 
			([appleScript executeAndReturnError:&error]) 
			{
                NSLog(@"success!");
	} 
		else 
	{
NSLog(@"Failed to execute applescript at all.");
            }
        }
    }
	return 0;
};
