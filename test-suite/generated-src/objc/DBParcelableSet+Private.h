// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from parcelable.djinni

#import "DBParcelableSet.h"
#include "parcelable_set.hpp"

static_assert(__has_feature(objc_arc), "Djinni requires ARC to be enabled for this file");

@class DBParcelableSet;

namespace djinni_generated {

struct ParcelableSet
{
    using CppType = ::testsuite::ParcelableSet;
    using ObjcType = DBParcelableSet*;

    using Boxed = ParcelableSet;

    static CppType toCpp(ObjcType objc);
    static ObjcType fromCpp(const CppType& cpp);
};

}  // namespace djinni_generated