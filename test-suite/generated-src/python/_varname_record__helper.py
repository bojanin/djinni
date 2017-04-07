# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from varnames.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files
from djinni.pycffi_marshal import CPyPrimitive, CPyRecord
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

from _varname_record_ import VarnameRecord

class VarnameRecordHelper:
    @staticmethod
    def release(c_ptr):
        assert c_ptr in c_data_set
        c_data_set.remove(ffi.cast("void*", c_ptr))

    @ffi.callback("int8_t(struct DjinniRecordHandle *)")
    def get__varname_record__f1(cself):
        try:
            _ret = CPyPrimitive.fromPy(CPyRecord.toPy(None, cself)._field_)
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniRecordHandle *(int8_t)")
    def python_create__varname_record_(_field_):
        py_rec = VarnameRecord(
            CPyPrimitive.toPy(_field_))
        return CPyRecord.fromPy(VarnameRecord.c_data_set, py_rec) #to do: can be optional?

    @ffi.callback("void (struct DjinniRecordHandle *)")
    def __delete(dh):
        assert dh in VarnameRecord.c_data_set
        VarnameRecord.c_data_set.remove(dh)

    @staticmethod
    def _add_callbacks():
        lib._varname_record__add_callback_get__varname_record__f1(VarnameRecordHelper.get__varname_record__f1)
        lib._varname_record__add_callback_python_create__varname_record_(VarnameRecordHelper.python_create__varname_record_)
        lib._varname_record__add_callback___delete(VarnameRecordHelper.__delete)

VarnameRecordHelper._add_callbacks()
