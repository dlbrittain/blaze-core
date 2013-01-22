"""
Some tests based on the Kiva loan data set

http://build.kiva.org/docs/data
"""

import unittest
import blaze

from blaze import dshape
from blaze.datashape.parser import parse

def test_one_field_int():
    s = """{
        id: int64
    }"""
    parse(s)
    ds = dshape(s)
    print(ds)
    assert str(ds) == '{ id : int64 }'

def test_one_field_int_trailing_semi():
    s = """{
        id: int64;
    }"""
    parse(s)
    ds = dshape(s)
    print(ds)
    assert str(ds) == '{ id : int64 }'

def test_one_field_string():
    s = """{
        name: string
    }"""
    parse(s)
    ds = dshape(s)
    print(ds)
    assert str(ds) == '{ name : string }'

def test_two_fields():
    s = """{
        id: int64;
        name: string
    }"""
    parse(s)
    ds = dshape(s)
    print(ds)
    
def test_description_languages():
    s = """{
        description: {
            languages: Range(0,inf), string16
        }
    }"""
    parse(s)
    ds = dshape(s)
    print(ds)

def test_option():
    s = """{
        basket_amount: Option(float64)
    }"""
    parse(s)
    ds = dshape(s)
    print(ds)

def test_option_record():
    s = """{
        video: Option({
            id: int64;
            youtube_id: string
        })
    }"""
    parse(s)
    ds = dshape(s)
    print(ds)

@unittest.skip("Map not supported by datashape""")
def test_map():
    # Want to have something like a C++ std::map<S,T> or
    # Apache Thrift's map<S,T> here.
    s = """{
        description: {
            texts: Map(string16, string)
        }
    }"""
    parse(s)
    ds = dshape(s)
    print(ds)

@unittest.skip("Categorical not supported by datashape""")
def test_categorical():
    # Want something like DyND's categorical dtype, for
    # example in the loan status
    s = """{
        status: Categorical(string, ["", "defaulted", "deleted",
                                 "expired", "funded", "fundraising",
                                 "in_repayment", "inactive", "inactive_expired",
                                 "issue", "paid", "refunded", "reviewed"])
    }"""
    parse(s)
    ds = dshape(s)
    print(ds)

