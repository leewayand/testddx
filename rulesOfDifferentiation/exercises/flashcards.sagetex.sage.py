## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file flashcards.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_40 = Integer(40); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_3 = Integer(3); _sage_const_49 = Integer(49); _sage_const_47 = Integer(47); _sage_const_43 = Integer(43); _sage_const_15 = Integer(15)## This file (flashcards.sagetex.sage) was *autogenerated* from flashcards.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('flashcards', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_15 
_st_.blockbegin()
try:
   vs = ['x','y','z','w']
   x = var(vs[randint(_sage_const_0 ,len(vs)-_sage_const_1 )])
 
   Fs = ['f','g','h','F','G','H']
   F = var(Fs[randint(_sage_const_0 ,len(Fs)-_sage_const_1 )])
 
   def random_expression(depth):
     if depth == _sage_const_0 :
       return [x,_sage_const_1 ,-_sage_const_1 ][randint(_sage_const_0 ,_sage_const_2 )]
     else:
       possible = [
         lambda: random_expression(depth-_sage_const_1 ) + random_expression(depth-_sage_const_1 ),
         lambda: random_expression(depth-_sage_const_1 ) - random_expression(depth-_sage_const_1 ),
         lambda: random_expression(depth-_sage_const_1 ) * random_expression(depth-_sage_const_1 ),
         lambda: random_expression(depth-_sage_const_1 ) / random_expression(depth-_sage_const_1 ),
         lambda: sin(random_expression(depth-_sage_const_1 )),
         lambda: cos(random_expression(depth-_sage_const_1 )),
         lambda: exp(random_expression(depth-_sage_const_1 ))
       ]
       result = possible[randint(_sage_const_0 ,len(possible)-_sage_const_1 )]()
       if result.is_zero():
         result = _sage_const_1 
       return result
 
   f = random_expression(_sage_const_4 )
   while (derivative(f,x).is_zero()) or (len(latex(derivative(f,x))) > _sage_const_40 ):
     f = random_expression(randint(_sage_const_1 ,_sage_const_4 ))
except:
 _st_.goboom(_sage_const_43 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_47 
 _st_.inline(_sage_const_0 , latex(F))
except:
 _st_.goboom(_sage_const_47 )
try:
 _st_.current_tex_line = _sage_const_47 
 _st_.inline(_sage_const_1 , latex(x))
except:
 _st_.goboom(_sage_const_47 )
try:
 _st_.current_tex_line = _sage_const_47 
 _st_.inline(_sage_const_2 , latex(f))
except:
 _st_.goboom(_sage_const_47 )
try:
 _st_.current_tex_line = _sage_const_49 
 _st_.inline(_sage_const_3 , latex(F))
except:
 _st_.goboom(_sage_const_49 )
try:
 _st_.current_tex_line = _sage_const_49 
 _st_.inline(_sage_const_4 , latex(x))
except:
 _st_.goboom(_sage_const_49 )
try:
 _st_.current_tex_line = _sage_const_49 
 _st_.inline(_sage_const_5 , latex(derivative(f,x)))
except:
 _st_.goboom(_sage_const_49 )
_st_.endofdoc()

