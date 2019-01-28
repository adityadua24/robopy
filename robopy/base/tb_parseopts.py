#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FILE: tb_parseopts.py
DATE: Fri Jan 11 08:02:00 2019

@author: garyd
"""

__all__ = ('asSimpleNs', 'tb_parseopts',)


try:
    """
    from namespace import Namespace as SimpleNs     # Eric Snow's version
    from namespace import as_namespace              # does not work in
    def asSimpleNs(obj):                            # Python 3.5
        return SimpleNs(obj) 
    """
    from types import SimpleNamespace as SimpleNs   # added in Python 3.3
    def asSimpleNs(dict_obj):
        return SimpleNs(**dict_obj)
except:
    """
    from namespace import Namespace as SimpleNs     # Eric Snow's version
    from namespace import as_namespace              # does not work in
    def asSimpleNs(obj):                            # Python 2.7
        return SimpleNs(obj) 
    """
    from argparse import Namespace as SimpleNs      # works in Python 2.7
    def asSimpleNs(dict_obj):
        return SimpleNs(**dict_obj)
    
    
def tb_parseopts(opt, **arglist):
    """ A simplified implementation of tb_parseopts from RTB for MATLAB. 
        This implementation only accepts keyword/value pairs in arglist,
        
        This routine, in conjunction with SimpleNamespace and Namespace
        class objects, permits representation and evaluation of optional
        function arguments defined in dict() object data structures
        using the 'dot' notation as shown below.
        
          def aFunc(v, ..., key1=val, key2=val, ..., kwyN=val):
      
               opts = {'key1':key1_val,
                       'key2':key2_val,
                        .
                        .
                        .
                       'keyN':keyN_val,
                      }
               
               opt = asSimpleNs(opts)
               
               opt.key1 = key1_val
               opt.key2 = key2_val
                  .
                  .
                  .
               opt.keyN = keyN_val
       
       Inputs:
       :param opt: opt.keys to set from key/val pair or arglist
       :param arglist: keyword/value pairs 
       :type opt: SimpleNamespace or Namespace object
       :type arglist: dict() object of keyword/value pairs
       
       Returns: updated opt and args with non-opt key/val pairs 
       :return: (opt, args)
       :rtype: tuple
    """
    # initialize list of keyword/value pairs not in opt
    args = {} 
      
    # for each keyword in arglist ...
    for arg_key in arglist:
        arg_val = arglist[arg_key]
        if arg_key in vars(opt):
           opt.__setattr__(arg_key, arg_val)   # update opt
        else:                              #   or
           args.update({arg_key:arg_val})  # update args
           
    return (opt, args)


if __name__ == '__main__':
    
    def test(v, a='a', b='b', z=[1,2,3], **params):
        
        opts = { 'a':a,  # first default keyword/value 
                 'b':b,  # second default keyword/value
                 'z':z,  # third default keyword/value
               }
        
        opt = asSimpleNs(opts)

        assert( opt.a == a )
        assert( opt.b == b )
        assert( opt.z == z )
          
        (opt, args) = tb_parseopts(opt, **params)
        
        if 'a' in params :
            assert ( opt.a == params['a'] )
        else:
            assert ( opt.a == a )
        assert ( 'a' not in args )
            
        if 'b' in params :
            assert ( opt.b == params['b'] )
        else:
            assert ( opt.b == b )
        assert ( 'b' not in args )
        
        if 'z' in params :
            assert ( opt.z == params['z'] )
        else:
            assert ( opt.z == z )
        assert ( 'z' not in args )
        
        return (v, opt, args)
        
    (v, opt, args) = test('test1', a='A', b='B', c='c')
    assert( v == 'test1' )
    assert( opt.a == 'A' )
    assert( opt.b == 'B' )
    assert( ('c' in args) and (args['c'] == 'c') ) 
    
    (v, opt, args) = test('test2', c='C')
    assert( v == 'test2' )
    assert( opt.a == 'a' )
    assert( opt.b == 'b' )
    assert( ('c' in args) and (args['c'] == 'C') )
    
    params = {'a':1, 'b':2, 'c':3}
    (v, opt, args) = test('test3', **params)
    assert( v == 'test3' )
    assert( opt.a == 1 )
    assert( opt.b == 2 )
    assert( ('c' in args) and (args['c'] == 3) )
    
    (v, opt, args) = test('test4')
    assert( v == 'test4' )
    assert( opt.a == 'a' )
    assert( opt.b == 'b' )
    assert( args == {} )
    
    (v, opt, args) = test('test5', z=['a','b','c'])
    assert( v == 'test5' )
    assert( opt.a == 'a' )
    assert( opt.b == 'b' )
    assert( opt.z == ['a', 'b','c'])
    assert( args == {} )