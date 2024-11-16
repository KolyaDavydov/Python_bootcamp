#include <Python.h>

static PyObject* calc_add(PyObject* self, PyObject* args){
    double a, b;
    if(!PyArg_ParseTuple(args, "dd", &a, &b)){
        return NULL;
    }
    return PyFloat_FromDouble(a + b);
}

static PyObject* calc_sub(PyObject* self, PyObject* args){
    double a, b;
    if(!PyArg_ParseTuple(args, "dd", &a, &b)){
        return NULL;
    }
    return PyFloat_FromDouble(a - b);
}

static PyObject* calc_mul(PyObject* self, PyObject* args){
    double a, b;
    if(!PyArg_ParseTuple(args, "dd", &a, &b)){
        return NULL;
    }
    return PyFloat_FromDouble(a * b);
}

static PyObject* calc_div(PyObject* self, PyObject* args){
    double a, b;
    if(!PyArg_ParseTuple(args, "dd", &a, &b)){
        return NULL;
    }
    if(b == 0){
        PyErr_SetString(PyExc_ZeroDivisionError, "\033[31mCannot divide by zero\033[0m");
        return NULL;
    }
    return PyFloat_FromDouble(a / b);
}

static PyMethodDef calcMethods[] = {
    {"add", calc_add, METH_VARARGS, "Add two numbers"},
    {"sub", calc_sub, METH_VARARGS, "Subtract two numbers"},
    {"mul", calc_mul, METH_VARARGS, "Multiply two numbers"},
    {"div", calc_div, METH_VARARGS, "Divide two numbers"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef calculatormodule = {
   PyModuleDef_HEAD_INIT,
   "calculator",   /* name of module */
   "Calculator module", /* module documentation */
   -1,
   calcMethods
};

PyMODINIT_FUNC
PyInit_calculator(void)
{
    return PyModule_Create(&calculatormodule);
}