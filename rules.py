import re
class Rule:
    def action(self, block, handler):   #use handler to do the actions
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True

class HeadingRule(Rule):
    type = 'heading'
    def condition(self, block):
        return not '\n' in block and len(block) <=70 and not block[-1] == ":"

class TitleRule(HeadingRule):
    type = 'title'
    first = True
    def condition(self,block):
        if not self.first: return False
        self.first = False
        return HeadingRule.condition(self,block)

class TableRule(Rule):
    type = 'table'
    def condition(self, block):
        if block[0:13] == "table_note_rp":
            return True
        return False




class ParagraphRule(Rule):
    type = 'paragraph'
    def condition(self, block):
        return True
