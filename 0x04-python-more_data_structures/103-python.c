#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t size = PyList_Size(p);
		Py_ssize_t i;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

		for (i = 0; i < size; i++)
		{
			printf("Element %zd: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		}
	}
	else
	{
		PyErr_Print();
	}
}

void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{
		Py_ssize_t size = PyBytes_Size(p);
		Py_ssize_t max_display = size < 10 ? size : 10;

		printf("[.] bytes object info\n");
		printf("size: %zd\n", size);
		printf("trying string: %s\n", PyBytes_AsString(p));

		printf("first %zd bytes: ", max_display);
		for (Py_ssize_t i = 0; i < max_display; i++)
		{
			printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
			if (i < max_display - 1)
				printf(" ");
		}
		printf("\n");
	}
	else
	{
		PyErr_Print();
	}
}
