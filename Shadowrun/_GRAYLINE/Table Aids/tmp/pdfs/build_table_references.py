from pathlib import Path
import sys
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_LEFT
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'output' / 'pdf'
OUT.mkdir(parents=True, exist_ok=True)
INK = colors.HexColor('#17232D')
GRAY = colors.HexColor('#E9EDF0')
MUTED = colors.HexColor('#4D5962')

class Sheet:
    def __init__(self, filename, size, title, subtitle, cols, font=9.5, leading=12):
        self.path = OUT / filename
        if self.path.exists() and '--replace-generated' not in sys.argv:
            raise FileExistsError(self.path)
        self.c = canvas.Canvas(str(self.path), pagesize=size)
        self.c.setTitle(title)
        self.c.setAuthor('Grayline campaign - table reference')
        self.W, self.H = size
        self.margin = 30
        self.gap = 18
        self.width = (self.W - 60 - (cols-1)*self.gap)/cols
        self.top = self.H - 99
        self.bottom = 43
        self.style = ParagraphStyle('body', fontName='Helvetica', fontSize=font,
                                    leading=leading, textColor=INK, alignment=TA_LEFT)
        self.small = ParagraphStyle('small', parent=self.style, fontSize=8.2, leading=10)
        self.c.setFillColor(INK)
        self.c.setFont('Helvetica-Bold', 9)
        self.c.drawString(30, self.H-32, 'SHADOWRUN / GRAYLINE  |  SKILL-BASED HOUSE RULES')
        self.c.setFont('Helvetica-Bold', 23 if cols==2 else 22)
        self.c.drawString(30, self.H-59, title)
        self.c.setFont('Helvetica', 10)
        self.c.drawString(30, self.H-77, subtitle)
        self.c.setStrokeColor(INK)
        self.c.line(30, self.H-88, self.W-30, self.H-88)
        for n in range(1, cols):
            x=30+n*(self.width+self.gap)-self.gap/2
            self.c.setStrokeColor(GRAY)
            self.c.line(x,self.bottom,x,self.top)
        self.extents=[]

    def column(self, index):
        self.x = 30 + index*(self.width+self.gap)
        self.y = self.top

    def heading(self, text):
        self.y -= 18
        self.c.setFillColor(GRAY)
        self.c.rect(self.x,self.y,self.width,17,fill=1,stroke=0)
        self.c.setFillColor(INK)
        self.c.setFont('Helvetica-Bold',10)
        self.c.drawString(self.x+6,self.y+5,text)
        self.y -= 6

    def p(self, text, small=False, after=5):
        item=Paragraph(text,self.small if small else self.style)
        _,h=item.wrap(self.width,1000)
        self.y -= h
        if self.y < self.bottom:
            raise ValueError(f'Content overflow: {self.path.name}: {text[:65]} at {self.y}')
        item.drawOn(self.c,self.x,self.y)
        self.y-=after

    def table(self, rows, widths=None):
        widths=widths or [self.width/len(rows[0])]*len(rows[0])
        data=[[Paragraph(str(cell),self.small) for cell in row] for row in rows]
        t=Table(data,colWidths=widths,hAlign='LEFT')
        t.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(-1,0),GRAY),
            ('VALIGN',(0,0),(-1,-1),'TOP'),
            ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
            ('TOPPADDING',(0,0),(-1,-1),3.5),('BOTTOMPADDING',(0,0),(-1,-1),3.5),
            ('LINEBELOW',(0,0),(-1,0),.5,MUTED),
            ('LINEBELOW',(0,1),(-1,-1),.25,GRAY),
        ]))
        _,h=t.wrap(self.width,1000)
        self.y-=h
        if self.y<self.bottom: raise ValueError(f'Table overflow {self.path.name}')
        t.drawOn(self.c,self.x,self.y)
        self.y-=8

    def finish(self):
        self.c.setStrokeColor(MUTED)
        self.c.line(30,33,self.W-30,33)
        self.c.setFillColor(MUTED)
        self.c.setFont('Helvetica',7)
        self.c.drawString(30,22,'Agreed table rules | 19 Sep 2026 | House rules override SR3 only where stated.')
        self.c.drawRightString(self.W-30,22,'US Letter | Print at 100% | 1 / 1')
        self.c.showPage()
        self.c.save()
        r=PdfReader(self.path)
        assert len(r.pages)==1
        text=r.pages[0].extract_text()
        assert len(text)>2500
        print(self.path, '1 page', len(text), 'text characters')

p=Sheet('Grayline_Player_One_Sheet_20260919.pdf',(612,792),
        'PLAYER QUICK REFERENCE','Roll the skill. Adjust the dice. Normally, 5 and 6 are successes.',2,9.5,12)
p.column(0)
p.heading('01  BUILD YOUR ROLL')
p.p('<b>Skill + permitted pool dice + dice modifiers.</b><br/>Do not automatically add an attribute. Attribute-only tests still use their specified attribute.')
p.table([['<b>Old TN modifier</b>','<b>Now change dice</b>'],
         ['+1 / +2 / +4 penalty','-1 / -2 / -4 dice'],
         ['-1 / -2 benefit','+1 / +2 dice']])
p.p('<b>Example:</b> Skill 5 + smartlink 2 - partial cover 4 = <b>3 dice at TN 5</b>. Keep the original equipment restrictions and pool limits.')
p.heading('02  COUNT SUCCESSES')
p.p('At TN 5, each <b>5 or 6</b> scores a success. A successful <b>6</b> also grants another roll; that roll can score again. Keep going while successful sixes continue.')
p.p('<b>TN 5:</b> 6, then 5 = <b>2 successes</b>.<br/>6, then 2 = <b>1 success</b>.<br/>6, then 6, then 5 = <b>3 successes</b>.')
p.heading('03  WHEN PENALTIES EXHAUST DICE')
p.p('For an allowed attempt, stop reducing at <b>1 die</b>. Each unused penalty point then raises TN above 5.')
p.p('<b>Skill 5 with -8:</b> spend 4 penalty points to reach 1 die; 4 remain. Roll <b>1 die at TN 9</b>, not TN 10.')
p.p('At a high TN, reroll sixes and add until you reach the TN or fall short on a non-six. Reaching TN earns one success. If the completing face is 6, start a fresh attempt from zero.')
p.p('<b>TN 9:</b> 6 + 3 = 1 success; 6 + 2 = none.<br/>6 + 6 = 1 success <b>and a fresh TN 9 attempt</b>.')
p.heading('04  MISHAPS & KARMA')
p.p('<b>Possible mishap:</b> zero successes after all rolls, and <b>more than half</b> the original dice initially show 1. Rerolls do not count toward that majority. One die showing 1 qualifies.')
p.p('<b>Karma:</b> retry eligible original failures for 1 point, then 2 more, then 3 more. Keep successes; do not retry failed bonus rolls from successful sixes. Spend 1 to turn a mishap into ordinary failure; no Karma retry of that test.',small=True)

p.column(1)
p.heading('05  COMBAT AT A GLANCE')
p.p('<b>Attack:</b> skill + allocated Combat Pool + modifiers; normally TN 5. No successes = miss.<br/><b>Ranged dodge:</b> allocated Combat Pool dice; normally TN 5. No added Reaction or free dodge dice.<br/><b>Soak:</b> Body + permitted allocated pool dice; <b>TN = Power - applicable Armor, minimum 2</b>. No added Willpower or Impact dice.')
p.p('A ranged dodge with <b>more</b> successes than the attack avoids it. Otherwise add dodge and soak successes, then subtract that total from attack successes.')
p.p('<b>Every 2 net successes:</b> attacker stages damage up one level; defender stages it down one. A tie or a difference of 1 leaves base damage. Compare first; then stage.')
p.table([['<b>None</b>','<b>L</b>','<b>M</b>','<b>S</b>','<b>D</b>'],
         ['0 boxes','1 box','3 boxes','6 boxes','10 boxes']])
p.p('Cap staging at Deadly; below Light is no damage. No optional overdamage. Normal condition monitors and overflow remain unchanged.',small=True)
p.heading('06  KEEP THESE NUMBERS HANDY')
p.table([['<b>Range</b>','<b>Dice</b>','<b>Wound*</b>','<b>Dice</b>'],
         ['Short','0','Light','-1'],['Medium','-1','Moderate','-2'],
         ['Long','-2','Serious','-3'],['Extreme','-5','*P + Stun','Stack']])
p.p('Wound penalties above apply to converted tests where wound modifiers normally apply. Retain normal exceptions.',small=True)
p.p('<b>Combat Pool:</b> (Quickness + Intelligence + Willpower) / 2, rounded down. Attack allocation cannot exceed the skill. Spent dice return at the start of the next <b>Combat Turn</b>, not each pass.',small=True)
p.heading('07  OUTSIDE COMBAT')
p.p('<b>Difficulty changes dice; amount of work sets required successes.</b> Roll again when the situation changes, not just because another turn passes.')
p.p('For general opposed tests, active beats passive on positive ties. Active searching takes an action. If both are active, ties leave things unchanged. Zero successes never accomplish an action.')
p.p('<b>Complementary skills:</b> every 2 eligible supporting successes add 1 primary success, only if the primary roll already earned at least 1. Keep written eligibility limits.',small=True)
p.heading('EXCEPTIONS STAY EXCEPTIONS')
p.p('Keep Power - Armor soak, Force-based spell resistance and Drain TNs, specialized Matrix resolution, and natural recovery TNs/times. Specific combat and magic procedures still govern their own ties.',small=True)
p.finish()

g=Sheet('Grayline_GM_Screen_Panel_20260919.pdf',(612,792),
        'GM SCREEN / DIFFICULTY TO DICE','TN 5 by default. Convert modifiers once. Preserve the named exceptions.',2,9.0,11.1)
g.column(0)
g.heading('CONVERSION: FLIP THE SIGN')
g.table([['<b>Printed TN modifier</b>','<b>Dice modifier</b>'],
         ['-2 / -1 benefit','+2 / +1 dice'],['0','0'],
         ['+1 / +2 / +3 penalty','-1 / -2 / -3 dice'],
         ['+4 / +6 / +8 penalty','-4 / -6 / -8 dice']])
g.p('<b>Skill + permitted pool + net dice modifiers.</b> No automatic Attribute + Skill. Preserve eligibility, stacking restrictions and pool caps.')
g.p('<b>Convert TN modifiers, not every printed number.</b> A base TN, opposed rating, success threshold or Power value is not automatically a dice penalty. Use the agreed conversions below; retain named exceptions.',small=True)
g.heading('DIFFICULTY OR MORE WORK?')
g.p('<b>Difficulty changes dice. More work requires more successes.</b> Apply both only for distinct reasons. Routine actions without meaningful uncertainty need no roll.',small=True)
g.p('Extended work accumulates successes per interval. Ordinary failure means no progress, not erased progress. Parallel work can combine progress if the task permits it.',small=True)
g.heading('ONE-DIE FLOOR / HIGH TN')
g.p('Let <b>N = starting dice + net modifier</b>.<br/>If N is at least 1: roll N dice at TN 5.<br/>If N is 0 or less: roll 1 die at <b>TN 6 - N</b>.')
g.p('<b>5 dice - 8: 1 die at TN 9.</b> Add rerolled sixes until TN is reached or a non-six fails. A success-completing 6 starts a fresh attempt from zero.<br/>TN 9: 6, 6, 6, 3 = <b>2 successes</b>.',small=True)
g.heading('DEFAULTING IS NOT TRAINING')
g.p('Related skill: <b>-2 dice</b>; eligible related specialization: <b>-3</b>; linked attribute instead of skill: <b>-4</b>. Keep route/pool restrictions; no pool dice for attribute defaulting. Training-required actions stay unavailable.',small=True)
g.heading('OPPOSITION, SUPPORT & RETRIES')
g.p('Compare success counts. Active wins positive ties against passive; both active tie = status quo. Zero never succeeds. Active search costs an action. Reroll only when circumstances change. Specific combat/magic tie rules take precedence.',small=True)
g.p('Eligible complementary skill: same TN; every 2 successes add 1 primary success. Primary must already have 1 success. Keep written restrictions.',small=True)
g.heading('MISHAPS & KARMA')
g.p('<b>Zero successes + strict majority of original initial dice showing 1</b> = possible mishap. Resolve all chains first. Ignore rerolls in the majority count; one-die 1 qualifies.',small=True)
g.p('Karma retries of eligible original failures: <b>1, then 2 more, then 3 more</b>. Keep successes; never retry failed bonus attempts from successful sixes. An original high-TN chain with no success is eligible, from scratch. 1 Karma makes a mishap ordinary failure; no Karma retry of that test.',small=True)

g.column(1)
g.heading('COMMON CONVERTED MODIFIERS')
g.table([['<b>Situation / benefit</b>','<b>Dice</b>'],
         ['Smartlink / smart goggles','+2 / +1'],
         ['Laser sight / each aim action','+1 / +1'],
         ['Partial cover / blind fire','-4 / -8'],
         ['Target running / stationary','-2 / +1'],
         ['Attacker walking / running','-1 / -4'],
         ['Walking / running, difficult ground','-2 / -6'],
         ['Each additional target in phase','-2'],
         ['Called shot','-4'],
         ['Light / Moderate / Serious wound','-1 / -2 / -3']],[g.width-62,62])
g.p('Preserve sight compatibility, aim limits and other written restrictions. Physical + Stun wound modifiers stack where applicable. Recoil: convert the <b>uncompensated</b> TN penalty; keep firing-mode rules.',small=True)
g.heading('RANGE & VEHICLE HANDLING')
g.table([['<b>Short</b>','<b>Medium</b>','<b>Long</b>','<b>Extreme</b>'],
         ['0 dice','-1 die','-2 dice','-5 dice']])
g.p('Keep weapon range distances. Range modifiers preserve the differences from SR3 short range; do not subtract the whole old range TN.',small=True)
g.p('<b>Driving modifier = 5 - Handling.</b><br/>Handling 3: +2 dice; 4: +1; 5: 0; 6: -1. Add applicable driving modifiers and permitted existing pool/Autonav dice.',small=True)
g.p('<b>Example:</b> Skill 5 + smartlink 2 - medium range 1 - cover 4 = <b>2 dice at TN 5</b>.',small=True)
g.heading('RANGED DAMAGE: COMPARE FIRST')
g.p('<b>Attack / dodge:</b> normally TN 5. No attack successes = miss. Dodge uses allocated Combat Pool only. More dodge successes than attack = avoid; otherwise retain dodge successes for resistance.<br/><b>Soak:</b> Body + permitted pool dice at <b>max(2, Power - Armor)</b>.',small=True)
g.p('<b>Net = attack - dodge - soak successes.</b><br/>Each full 2 net successes stages base damage up (attacker) or down (defender). Net 0 or +/-1: base damage.<br/><b>L / M / S / D = 1 / 3 / 6 / 10 boxes.</b><br/>Below L: none. Cap at D; no optional overdamage. Normal overflow remains.',small=True)
g.heading('DO NOT CONVERT THESE TO TN 5')
g.p('Power - Armor damage resistance; Force-based spell resistance and Drain TNs; specialized Matrix resolution; natural recovery TNs and healing times. Medical skill tests convert, but treatment limits/effects stay.',small=True)
g.p('<b>Reference:</b> agreed house rules; SR3 core pp.43, 97, 112-114. Not a complete subsystem replacement.',small=True,after=0)
g.finish()
