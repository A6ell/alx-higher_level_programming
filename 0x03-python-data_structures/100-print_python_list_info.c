#include <Python.h>

void print_python_list_info(PyObject *p)
{
PyListObject *listObj;
Py_ssize_t size, i;

if (!PyList_Check(p))
{
printf("Invalid list object.\n");
return;
}

listObj = (PyListObject *)p;
size = PyList_Size(p);

printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", listObj->allocated);

for (i = 0;  i < size;  i++)
{
PyObject *item = PyList_GetItem(p, i);
const char *typeName = Py_TYPE(item)->tp_name;

printf("Element %zd: %s\n", i, typeName);
}
}
