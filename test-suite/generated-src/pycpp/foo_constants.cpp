// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from foo_constants.djinni

#include "foo_constants.hpp"  // my header

namespace testsuite {

bool const FooConstants::BOOL_CONSTANT;

int8_t const FooConstants::I8_CONSTANT;

int16_t const FooConstants::I16_CONSTANT;

int32_t const FooConstants::I32_CONSTANT;

int64_t const FooConstants::I64_CONSTANT;

float const FooConstants::F32_CONSTANT;

double const FooConstants::F64_CONSTANT;

std::string const FooConstants::STRING_CONSTANT = {"string-constant"};

std::experimental::optional<int32_t> const FooConstants::OPTIONAL_INTEGER_CONSTANT = 1;

FooConstants const FooConstants::OBJECT_CONSTANT = FooConstants(
    FooConstants::I32_CONSTANT /* some_integer */ ,
    FooConstants::STRING_CONSTANT /* some_string */ );

SomeConstRecord const FooConstants::SOME_RECORD = SomeConstRecord(
    28 /* number1 */ ,
    FooConstants::I16_CONSTANT /* number2 */ );

}  // namespace testsuite
