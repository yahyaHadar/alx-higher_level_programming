#include <stdio.h>
#include <time.h>
#include <Python.h>
#include <object.h>
#include <floatobject.h>

/**
 *print_python_bytes - prints python bytes
 *@p: pointer to the python bytes
 */

void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, i, limit;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;
	printf("  first %ld bytes:", limit);
	for (i = 0; i < limit; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);
	printf("\n");
}

/**
 *print_python_float - prints python float
 *@p: pointer to the python float
 */

void print_python_float(PyObject *p)
{
	double value;
	char *ptr;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = ((PyFloatObject *)(p))->ob_fval;
	ptr = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);
	printf("  value: %s\n", ptr);
}

/**
 *print_python_list - prints python list
 *@p: pointer to the python list
 */

void print_python_list(PyObject *p)
{
	PyListObject *list;
	PyObject *obj;
	long int size;
	int i = 0;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_CheckExact(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
  size = ((PyVarObject *)(p))->ob_size;
  list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %d: %s\n", i, ((obj)->ob_type)->tp_name);

		if (PyBytes_Check(obj))
			print_python_bytes(obj);
		if (PyFloat_Check(obj))
			print_python_float(obj);
	}
}
