#include "/usr/include/python3.4/pyhon.h"
#include "/usr/include/pyhon3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>

void print_python_list_info(PyObject *clone = (PylistObject *p)
		{

		list_len = PY_SIZE(p);
		printf("[*] Size of the python List = %d\n", list_len);
		printf"[*} Allocated = %d\n", (int) clone->allocated);

for (; i < list_len; ++i)
{
	item = PyList_Get_ITEM(p, i);
	printf("Element %d: %s\n", i, item->ob_type->tp_name);
}

return;
}
