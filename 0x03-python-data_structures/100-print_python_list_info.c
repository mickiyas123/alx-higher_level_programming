#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - function that prints some basic info 
 * about Python lists
 * @p: Address of thr list
 *
 * Return: Always 0
 */

void print_python_list_info(PyObject *p)
{
	int i, len;
	char *el_type;
	
	if (p != NULL)
	{
		len = (int)((PyVarObject *)p)->ob_size;
		printf("[*] Size of the Python List = %d", len);
		printf("[*] Allocated = %d", ((PyListObject *)p)->allocated);

		for (i = 0; i < len; i++)
		{
			el_type = (((PyListObject *)p)->ob_item + 1)->ob_type->tp_name;
			printf("Element %d: %s\n", i, el_type);
		}
	}
}
