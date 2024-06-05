#ifndef HAVE_PYPOSTAL_UTILS_H
#define HAVE_PYPOSTAL_UTILS_H

#include <Python.h>
#include <stdlib.h>

void string_array_destroy(char **strings, size_t num_strings);

char *PyObject_to_string(PyObject *obj);
char **PyObject_to_strings_max_len(PyObject *obj, ssize_t max_len,
                                   size_t *num_strings);
char **PyObject_to_strings(PyObject *obj, size_t *num_strings);

PyObject *PyObject_from_strings(char **strings, size_t num_strings);

#endif
