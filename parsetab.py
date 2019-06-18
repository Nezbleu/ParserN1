
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVISION LPAREN MINUS NUMBER PLUS RPAREN TIMESexpression : expression PLUS termexpression : expression MINUS termexpression : expression DIVISION termexpression : termterm : term TIMES factorterm : factorfactor : NUMBERfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'DIVISION':([1,2,4,5,7,11,12,13,14,15,],[-4,-7,-6,10,10,-5,-8,-1,-2,-3,]),'RPAREN':([1,2,4,7,11,12,13,14,15,],[-4,-7,-6,12,-5,-8,-1,-2,-3,]),'NUMBER':([0,3,6,8,9,10,],[2,2,2,2,2,2,]),'TIMES':([1,2,4,11,12,13,14,15,],[6,-7,-6,-5,-8,6,6,6,]),'PLUS':([1,2,4,5,7,11,12,13,14,15,],[-4,-7,-6,8,8,-5,-8,-1,-2,-3,]),'LPAREN':([0,3,6,8,9,10,],[3,3,3,3,3,3,]),'MINUS':([1,2,4,5,7,11,12,13,14,15,],[-4,-7,-6,9,9,-5,-8,-1,-2,-3,]),'$end':([1,2,4,5,11,12,13,14,15,],[-4,-7,-6,0,-5,-8,-1,-2,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([0,3,8,9,10,],[1,1,13,14,15,]),'expression':([0,3,],[5,7,]),'factor':([0,3,6,8,9,10,],[4,4,11,4,4,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','parser_rules.py',5),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','parser_rules.py',9),
  ('expression -> expression DIVISION term','expression',3,'p_expression_division','parser_rules.py',13),
  ('expression -> term','expression',1,'p_expression_term','parser_rules.py',17),
  ('term -> term TIMES factor','term',3,'p_term_times','parser_rules.py',21),
  ('term -> factor','term',1,'p_term_factor','parser_rules.py',25),
  ('factor -> NUMBER','factor',1,'p_factor_num','parser_rules.py',29),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','parser_rules.py',33),
]
