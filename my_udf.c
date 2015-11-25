/*
 * my_udf.c
 *
 *  Created on: 2015年11月24日
 *      Author: sourunsheng
 */

#include <string.h>
#include <mysql.h>

#if defined(_WIN32) || defined(_WIN64)
#define DLLEXP __declspec(dllexport)
#else
#define DLLEXP
#endif

#ifdef	__cplusplus


extern "C" {
#endif

//#define LIBVERSION "lib_mysqludf_udf version 0.0.3"
/*
 * my test function, initialization
 * add integer with 3
 */

my_bool myTest_init(
	UDF_INIT *initid,
	UDF_ARGS *args,
	char *message
		);

void myTest_deinit(
	UDF_INIT *initid
);

long long myTest(
	UDF_INIT *initid
,	UDF_ARGS *args
,   char *is_null
,	char *error
);
#ifdef	__cplusplus
}
#endif


/*
 * My test function
 * Function body
 */
my_bool myTest_init(
	UDF_INIT *initid
,	UDF_ARGS *args
,	char *message
){
	return 0;
}

void myTest_deinit(
	UDF_INIT *initid
){
}

long long myTest(
	UDF_INIT *initid
,	UDF_ARGS *args
,   char *is_null
,	char *error
){
	int a = 3;
	return args->args + a;
}

/*
 * compile: gcc -shared -o my_udf.so my_udf.c
 *
 * Then, put the compiled .so file to : usr/local/mysql/lib/plugin
 *
 * Then at MySql:
 *
 * CREATE FUNCTION myTest
 * RETURNS INTEGER SONAME 'my_udf.so';
 *
 * You should be able to call this function by:
 *
 * select myTest(p.salary)
 * from pilot p
 *
 */




