#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - Prints information about a Python list object
 * @p: Pointer to the Python list object
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("[*] Python list info\n  [ERROR] Invalid List Object\n");
		fflush(stdout);
		return;
	}

	size = PyList_Size(p);
	printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	fflush(stdout);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		fflush(stdout);
	}
}
/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to the Python bytes object
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("[.] bytes object info\n  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes:", (size + 1 < 10) ? size + 1 : 10);

	for (i = 0; i < size + 1 && i < 10; i++)
		printf(" %02x", (unsigned char)str[i]);

	printf("\n");
	fflush(stdout);
}

void print_python_float(PyObject *p)
{
	PyFloatObject *float_obj = (PyFloatObject *)p;
	char *str;

	if (!PyFloat_Check(p))
	{
		printf("[.] float object info\n  [ERROR] Invalid Float Object\n");
		fflush(stdout);
		return;
	}

	str =
PyOS_double_to_string(float_obj->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("[.] float object info\n  value: %s\n", str);
	PyMem_Free(str);
	fflush(stdout);
}
