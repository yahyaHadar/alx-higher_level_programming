#include <stdio.h>
#include <Python.h>

/**
 *print_python_string - a function that prints Python strings.
 *@p: pointer to the p string
 */
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");
	if (PyUnicode_Check(p))
	{
		if (PyUnicode_IS_COMPACT_ASCII(p))
			printf("  type: %s\n", "compact ascii");
		else
			printf("  type: %s\n", "compact unicode object");
		printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
		printf("  value: %s\n", PyUnicode_AsUTF8(p));
	}
	else
	printf("  [ERROR] Invalid String Object\n");
}
