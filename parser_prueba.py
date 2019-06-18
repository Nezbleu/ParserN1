import lexer_rules
import parser_rules
import lex
import yacc

lexer = lex.lex(module=lexer_rules)
parser = yacc.yacc(module=parser_rules)
text = "(14 - 6) / 2"
ast = parser.parse(text, lexer)

print (ast)
