#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info -  function that prints some 
 * basic info about Python lists
 * @p: Address to array object
 *
 * Return: ALways 0.
 */

void print_python_list_info(PyObject *p)
{
	int i, len, msize;
	PyObject *obj;
	
	len = Py_SIZE(P);
	msize = ((PyListObject *)p)->allocated

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", msize);

	for (i = 0; i < len; i++)
	{
		print("Element 0: %d", i);
		obj = PyList_GetItem(p, i);
		print("%s\n", Py_TYPE(obj)->tp_name);
	}
}
