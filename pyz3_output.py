import re
from z3 import *
DEBUG_MODE = False
OPERATOR_STR = "==|\+|-|\*|/|\(|\)|And|Implies|Or|Not|,|>|>=|<|<=|!="
s = Solver()
x0_1 = BitVec('x0_1', 32)
y0_1 = BitVec('y0_1', 32)
z0_1 = BitVec('z0_1', 32)
w0_1 = BitVec('w0_1', 32)
v0_1 = BitVec('v0_1', 32)
x0_2 = BitVec('x0_2', 32)
rettotalRand_0 = BitVec('rettotalRand_0', 32)
x0_3 = BitVec('x0_3', 32)
y0_2 = BitVec('y0_2', 32)
retadd2_0 = BitVec('retadd2_0', 32)
y0_3 = BitVec('y0_3', 32)
retadd2_1 = BitVec('retadd2_1', 32)
z0_2 = BitVec('z0_2', 32)
y0_4 = BitVec('y0_4', 32)
z0_3 = BitVec('z0_3', 32)
retmultiply_0 = BitVec('retmultiply_0', 32)
y0_5 = BitVec('y0_5', 32)
y0_6 = BitVec('y0_6', 32)
retmultiply3_0 = BitVec('retmultiply3_0', 32)
w0_2 = BitVec('w0_2', 32)
w0_3 = BitVec('w0_3', 32)
w0_4 = BitVec('w0_4', 32)
i1_1 = BitVec('i1_1', 32)
v0_2 = BitVec('v0_2', 32)
totalRandx2_0_0 = BitVec('totalRandx2_0_0', 32)
totalRandx2_1_0 = BitVec('totalRandx2_1_0', 32)
add2x2_0_0 = BitVec('add2x2_0_0', 32)
add2x2_1_0 = BitVec('add2x2_1_0', 32)
add2x2_0_1 = BitVec('add2x2_0_1', 32)
add2x2_1_1 = BitVec('add2x2_1_1', 32)
multiplyx2_0_0 = BitVec('multiplyx2_0_0', 32)
multiplyy2_0_0 = BitVec('multiplyy2_0_0', 32)
multiply3x2_0_0 = BitVec('multiply3x2_0_0', 32)
multiply3y2_0_0 = BitVec('multiply3y2_0_0', 32)
multiply3z2_0_0 = BitVec('multiply3z2_0_0', 32)
multiply3a2_1_0 = BitVec('multiply3a2_1_0', 32)
multiply3b2_1_0 = BitVec('multiply3b2_1_0', 32)
multiply3c2_1_0 = BitVec('multiply3c2_1_0', 32)
i1_2 = BitVec('i1_2', 32)
v0_3 = BitVec('v0_3', 32)
i1_3 = BitVec('i1_3', 32)
v0_4 = BitVec('v0_4', 32)
i1_4 = BitVec('i1_4', 32)
v0_5 = BitVec('v0_5', 32)
i1_5 = BitVec('i1_5', 32)
v0_6 = BitVec('v0_6', 32)
i1_6 = BitVec('i1_6', 32)
v0_7 = BitVec('v0_7', 32)
i1_7 = BitVec('i1_7', 32)
v0_8 = BitVec('v0_8', 32)
i1_8 = BitVec('i1_8', 32)
v0_9 = BitVec('v0_9', 32)
i1_9 = BitVec('i1_9', 32)
v0_10 = BitVec('v0_10', 32)
i1_10 = BitVec('i1_10', 32)
v0_11 = BitVec('v0_11', 32)
i1_11 = BitVec('i1_11', 32)
v0_12 = BitVec('v0_12', 32)
i1_12 = BitVec('i1_12', 32)
v0_13 = BitVec('v0_13', 32)
i1_13 = BitVec('i1_13', 32)
v0_14 = BitVec('v0_14', 32)
i1_14 = BitVec('i1_14', 32)
v0_15 = BitVec('v0_15', 32)
i1_15 = BitVec('i1_15', 32)
v0_16 = BitVec('v0_16', 32)
i1_16 = BitVec('i1_16', 32)
v0_17 = BitVec('v0_17', 32)
i1_17 = BitVec('i1_17', 32)
v0_18 = BitVec('v0_18', 32)
i1_18 = BitVec('i1_18', 32)
v0_19 = BitVec('v0_19', 32)
i1_19 = BitVec('i1_19', 32)
v0_20 = BitVec('v0_20', 32)
i1_20 = BitVec('i1_20', 32)
v0_21 = BitVec('v0_21', 32)
i1_21 = BitVec('i1_21', 32)
v0_22 = BitVec('v0_22', 32)
i1_22 = BitVec('i1_22', 32)
v0_23 = BitVec('v0_23', 32)
i1_23 = BitVec('i1_23', 32)
v0_24 = BitVec('v0_24', 32)
i1_24 = BitVec('i1_24', 32)
v0_25 = BitVec('v0_25', 32)
i1_25 = BitVec('i1_25', 32)
v0_26 = BitVec('v0_26', 32)
i1_26 = BitVec('i1_26', 32)
v0_27 = BitVec('v0_27', 32)
i1_27 = BitVec('i1_27', 32)
v0_28 = BitVec('v0_28', 32)
i1_28 = BitVec('i1_28', 32)
v0_29 = BitVec('v0_29', 32)
i1_29 = BitVec('i1_29', 32)
v0_30 = BitVec('v0_30', 32)
i1_30 = BitVec('i1_30', 32)
v0_31 = BitVec('v0_31', 32)
i1_31 = BitVec('i1_31', 32)
v0_32 = BitVec('v0_32', 32)
i1_32 = BitVec('i1_32', 32)
v0_33 = BitVec('v0_33', 32)
i1_33 = BitVec('i1_33', 32)
v0_34 = BitVec('v0_34', 32)
i1_34 = BitVec('i1_34', 32)
v0_35 = BitVec('v0_35', 32)
i1_35 = BitVec('i1_35', 32)
v0_36 = BitVec('v0_36', 32)
i1_36 = BitVec('i1_36', 32)
v0_37 = BitVec('v0_37', 32)
i1_37 = BitVec('i1_37', 32)
v0_38 = BitVec('v0_38', 32)
i1_38 = BitVec('i1_38', 32)
v0_39 = BitVec('v0_39', 32)
i1_39 = BitVec('i1_39', 32)
v0_40 = BitVec('v0_40', 32)
i1_40 = BitVec('i1_40', 32)
v0_41 = BitVec('v0_41', 32)
i1_41 = BitVec('i1_41', 32)
v0_42 = BitVec('v0_42', 32)
i1_42 = BitVec('i1_42', 32)
v0_43 = BitVec('v0_43', 32)
i1_43 = BitVec('i1_43', 32)
v0_44 = BitVec('v0_44', 32)
i1_44 = BitVec('i1_44', 32)
v0_45 = BitVec('v0_45', 32)
i1_45 = BitVec('i1_45', 32)
v0_46 = BitVec('v0_46', 32)
i1_46 = BitVec('i1_46', 32)
v0_47 = BitVec('v0_47', 32)
i1_47 = BitVec('i1_47', 32)
v0_48 = BitVec('v0_48', 32)
i1_48 = BitVec('i1_48', 32)
v0_49 = BitVec('v0_49', 32)
i1_49 = BitVec('i1_49', 32)
v0_50 = BitVec('v0_50', 32)
ppx0_1 = BitVec('ppx0_1', 32)
ppx0_2 = BitVec('ppx0_2', 32)
ppx0_3 = BitVec('ppx0_3', 32)
ppx0_4 = BitVec('ppx0_4', 32)
ppy0_1 = BitVec('ppy0_1', 32)
ppy0_2 = BitVec('ppy0_2', 32)
ppy0_3 = BitVec('ppy0_3', 32)
ppz0_1 = BitVec('ppz0_1', 32)
ppz0_2 = BitVec('ppz0_2', 32)
ppy0_4 = BitVec('ppy0_4', 32)
ppz0_3 = BitVec('ppz0_3', 32)
ppy0_5 = BitVec('ppy0_5', 32)
ppy0_6 = BitVec('ppy0_6', 32)
ppw0_1 = BitVec('ppw0_1', 32)
ppw0_2 = BitVec('ppw0_2', 32)
ppv0_1 = BitVec('ppv0_1', 32)
ppv0_2 = BitVec('ppv0_2', 32)
ppv0_3 = BitVec('ppv0_3', 32)
ppv0_4 = BitVec('ppv0_4', 32)
ppv0_5 = BitVec('ppv0_5', 32)
ppv0_6 = BitVec('ppv0_6', 32)
ppv0_7 = BitVec('ppv0_7', 32)
ppv0_8 = BitVec('ppv0_8', 32)
ppv0_9 = BitVec('ppv0_9', 32)
ppv0_10 = BitVec('ppv0_10', 32)
ppv0_11 = BitVec('ppv0_11', 32)
ppv0_12 = BitVec('ppv0_12', 32)
ppv0_13 = BitVec('ppv0_13', 32)
ppv0_14 = BitVec('ppv0_14', 32)
ppv0_15 = BitVec('ppv0_15', 32)
ppv0_16 = BitVec('ppv0_16', 32)
ppv0_17 = BitVec('ppv0_17', 32)
ppv0_18 = BitVec('ppv0_18', 32)
ppv0_19 = BitVec('ppv0_19', 32)
ppv0_20 = BitVec('ppv0_20', 32)
ppv0_21 = BitVec('ppv0_21', 32)
ppv0_22 = BitVec('ppv0_22', 32)
ppv0_23 = BitVec('ppv0_23', 32)
ppv0_24 = BitVec('ppv0_24', 32)
ppv0_25 = BitVec('ppv0_25', 32)
ppv0_26 = BitVec('ppv0_26', 32)
ppv0_27 = BitVec('ppv0_27', 32)
ppv0_28 = BitVec('ppv0_28', 32)
s.add((x0_1==1))
s.add((y0_1==y0_1))
s.add((z0_1==z0_1))
s.add((w0_1==w0_1))
s.add((v0_1==v0_1))
s.add((And((And((And((And((And((And((And((And((And((And((And((And((And((And((And((And((And((And((1==1),(1==1))),(1==1))),(1==1))),(x0_2==rettotalRand_0))),(x0_3==(x0_2+2)))),(y0_2==(1+retadd2_0)))),(y0_3==retadd2_1))),(z0_2==(y0_3+x0_3)))),(y0_4==(z0_2+x0_3)))),(z0_3==retmultiply_0))),(y0_5==((x0_3+y0_4)+z0_3)))),(y0_6==retmultiply3_0))),(And(And((Implies(And((x0_3>3), (y0_6>100)), (w0_2==-1))),(Implies(Not(And((x0_3>3), (y0_6>100))),(And(And((Implies(And((x0_3<3), (y0_6<0)), (w0_3==-100))),(Implies(Not(And((x0_3<3), (y0_6<0))),(w0_4==-1000)))),(Implies(And((x0_3<3), (y0_6<0)),((w0_4==w0_3))))))))),(Implies(And((x0_3>3), (y0_6>100)),((w0_4==w0_2)))))))),(i1_1==0))),(v0_2==0))),(1==1))),(1==1))),(1==1))))
s.add((123==totalRandx2_0_0))
s.add((And((totalRandx2_1_0==2),(And((Implies((totalRandx2_1_0==0), (rettotalRand_0==1))),(Implies(Not((totalRandx2_1_0==0)),(And((Implies((totalRandx2_1_0==1), (rettotalRand_0==2))),(Implies(Not((totalRandx2_1_0==1)),(rettotalRand_0==3))))))))))))
s.add((2==add2x2_0_0))
s.add((And((add2x2_1_0==(add2x2_0_0+2)),(retadd2_0==add2x2_1_0))))
s.add((4==add2x2_0_1))
s.add((And((add2x2_1_1==(add2x2_0_1+2)),(retadd2_1==add2x2_1_1))))
s.add((x0_3==multiplyx2_0_0))
s.add((y0_4==multiplyy2_0_0))
s.add((retmultiply_0==(multiplyx2_0_0*multiplyy2_0_0)))
s.add((x0_3==multiply3x2_0_0))
s.add((y0_5==multiply3y2_0_0))
s.add((z0_3==multiply3z2_0_0))
s.add((And((And((And((multiply3a2_1_0==multiply3x2_0_0),(multiply3b2_1_0==multiply3y2_0_0))),(multiply3c2_1_0==multiply3z2_0_0))),(retmultiply3_0==((multiply3a2_1_0*multiply3b2_1_0)*multiply3c2_1_0)))))
s.add((And((Implies(And((i1_1<10), (v0_2<300)),(And((i1_2==(i1_1+1)),(v0_3==i1_2))))),(Implies(Not(And((i1_1<10), (v0_2<300))),(And((v0_3==v0_2),(i1_2==i1_1))))))))
s.add((And((Implies(And((i1_2<10), (v0_3<300)),(And((i1_3==(i1_2+1)),(v0_4==i1_3))))),(Implies(Not(And((i1_2<10), (v0_3<300))),(And((v0_4==v0_3),(i1_3==i1_2))))))))
s.add((And((Implies(And((i1_3<10), (v0_4<300)),(And((i1_4==(i1_3+1)),(v0_5==i1_4))))),(Implies(Not(And((i1_3<10), (v0_4<300))),(And((v0_5==v0_4),(i1_4==i1_3))))))))
s.add((And((Implies(And((i1_4<10), (v0_5<300)),(And((i1_5==(i1_4+1)),(v0_6==i1_5))))),(Implies(Not(And((i1_4<10), (v0_5<300))),(And((v0_6==v0_5),(i1_5==i1_4))))))))
s.add((And((Implies(And((i1_5<10), (v0_6<300)),(And((i1_6==(i1_5+1)),(v0_7==i1_6))))),(Implies(Not(And((i1_5<10), (v0_6<300))),(And((v0_7==v0_6),(i1_6==i1_5))))))))
s.add((And((Implies(And((i1_6<10), (v0_7<300)),(And((i1_7==(i1_6+1)),(v0_8==i1_7))))),(Implies(Not(And((i1_6<10), (v0_7<300))),(And((v0_8==v0_7),(i1_7==i1_6))))))))
s.add((And((Implies(And((i1_7<10), (v0_8<300)),(And((i1_8==(i1_7+1)),(v0_9==i1_8))))),(Implies(Not(And((i1_7<10), (v0_8<300))),(And((v0_9==v0_8),(i1_8==i1_7))))))))
s.add((And((Implies(And((i1_8<10), (v0_9<300)),(And((i1_9==(i1_8+1)),(v0_10==i1_9))))),(Implies(Not(And((i1_8<10), (v0_9<300))),(And((v0_10==v0_9),(i1_9==i1_8))))))))
s.add((And((Implies(And((i1_9<10), (v0_10<300)),(And((i1_10==(i1_9+1)),(v0_11==i1_10))))),(Implies(Not(And((i1_9<10), (v0_10<300))),(And((v0_11==v0_10),(i1_10==i1_9))))))))
s.add((And((Implies(And((i1_10<10), (v0_11<300)),(And((i1_11==(i1_10+1)),(v0_12==i1_11))))),(Implies(Not(And((i1_10<10), (v0_11<300))),(And((v0_12==v0_11),(i1_11==i1_10))))))))
s.add((And((Implies(And((i1_11<10), (v0_12<300)),(And((i1_12==(i1_11+1)),(v0_13==i1_12))))),(Implies(Not(And((i1_11<10), (v0_12<300))),(And((v0_13==v0_12),(i1_12==i1_11))))))))
s.add((And((Implies(And((i1_12<10), (v0_13<300)),(And((i1_13==(i1_12+1)),(v0_14==i1_13))))),(Implies(Not(And((i1_12<10), (v0_13<300))),(And((v0_14==v0_13),(i1_13==i1_12))))))))
s.add((And((Implies(And((i1_13<10), (v0_14<300)),(And((i1_14==(i1_13+1)),(v0_15==i1_14))))),(Implies(Not(And((i1_13<10), (v0_14<300))),(And((v0_15==v0_14),(i1_14==i1_13))))))))
s.add((And((Implies(And((i1_14<10), (v0_15<300)),(And((i1_15==(i1_14+1)),(v0_16==i1_15))))),(Implies(Not(And((i1_14<10), (v0_15<300))),(And((v0_16==v0_15),(i1_15==i1_14))))))))
s.add((And((Implies(And((i1_15<10), (v0_16<300)),(And((i1_16==(i1_15+1)),(v0_17==i1_16))))),(Implies(Not(And((i1_15<10), (v0_16<300))),(And((v0_17==v0_16),(i1_16==i1_15))))))))
s.add((And((Implies(And((i1_16<10), (v0_17<300)),(And((i1_17==(i1_16+1)),(v0_18==i1_17))))),(Implies(Not(And((i1_16<10), (v0_17<300))),(And((v0_18==v0_17),(i1_17==i1_16))))))))
s.add((And((Implies(And(And((i1_17<20), (v0_18<300)), (v0_18!=-1)),(And((i1_18==(i1_17+1)),(v0_19==(v0_18+i1_18)))))),(Implies(Not(And(And((i1_17<20), (v0_18<300)), (v0_18!=-1))),(And((v0_19==v0_18),(i1_18==i1_17))))))))
s.add((And((Implies(And(And((i1_18<20), (v0_19<300)), (v0_19!=-1)),(And((i1_19==(i1_18+1)),(v0_20==(v0_19+i1_19)))))),(Implies(Not(And(And((i1_18<20), (v0_19<300)), (v0_19!=-1))),(And((v0_20==v0_19),(i1_19==i1_18))))))))
s.add((And((Implies(And(And((i1_19<20), (v0_20<300)), (v0_20!=-1)),(And((i1_20==(i1_19+1)),(v0_21==(v0_20+i1_20)))))),(Implies(Not(And(And((i1_19<20), (v0_20<300)), (v0_20!=-1))),(And((v0_21==v0_20),(i1_20==i1_19))))))))
s.add((And((Implies(And(And((i1_20<20), (v0_21<300)), (v0_21!=-1)),(And((i1_21==(i1_20+1)),(v0_22==(v0_21+i1_21)))))),(Implies(Not(And(And((i1_20<20), (v0_21<300)), (v0_21!=-1))),(And((v0_22==v0_21),(i1_21==i1_20))))))))
s.add((And((Implies(And(And((i1_21<20), (v0_22<300)), (v0_22!=-1)),(And((i1_22==(i1_21+1)),(v0_23==(v0_22+i1_22)))))),(Implies(Not(And(And((i1_21<20), (v0_22<300)), (v0_22!=-1))),(And((v0_23==v0_22),(i1_22==i1_21))))))))
s.add((And((Implies(And(And((i1_22<20), (v0_23<300)), (v0_23!=-1)),(And((i1_23==(i1_22+1)),(v0_24==(v0_23+i1_23)))))),(Implies(Not(And(And((i1_22<20), (v0_23<300)), (v0_23!=-1))),(And((v0_24==v0_23),(i1_23==i1_22))))))))
s.add((And((Implies(And(And((i1_23<20), (v0_24<300)), (v0_24!=-1)),(And((i1_24==(i1_23+1)),(v0_25==(v0_24+i1_24)))))),(Implies(Not(And(And((i1_23<20), (v0_24<300)), (v0_24!=-1))),(And((v0_25==v0_24),(i1_24==i1_23))))))))
s.add((And((Implies(And(And((i1_24<20), (v0_25<300)), (v0_25!=-1)),(And((i1_25==(i1_24+1)),(v0_26==(v0_25+i1_25)))))),(Implies(Not(And(And((i1_24<20), (v0_25<300)), (v0_25!=-1))),(And((v0_26==v0_25),(i1_25==i1_24))))))))
s.add((And((Implies(And(And((i1_25<20), (v0_26<300)), (v0_26!=-1)),(And((i1_26==(i1_25+1)),(v0_27==(v0_26+i1_26)))))),(Implies(Not(And(And((i1_25<20), (v0_26<300)), (v0_26!=-1))),(And((v0_27==v0_26),(i1_26==i1_25))))))))
s.add((And((Implies(And(And((i1_26<20), (v0_27<300)), (v0_27!=-1)),(And((i1_27==(i1_26+1)),(v0_28==(v0_27+i1_27)))))),(Implies(Not(And(And((i1_26<20), (v0_27<300)), (v0_27!=-1))),(And((v0_28==v0_27),(i1_27==i1_26))))))))
s.add((And((Implies(And(And((i1_27<20), (v0_28<300)), (v0_28!=-1)),(And((i1_28==(i1_27+1)),(v0_29==(v0_28+i1_28)))))),(Implies(Not(And(And((i1_27<20), (v0_28<300)), (v0_28!=-1))),(And((v0_29==v0_28),(i1_28==i1_27))))))))
s.add((And((Implies(And(And((i1_28<20), (v0_29<300)), (v0_29!=-1)),(And((i1_29==(i1_28+1)),(v0_30==(v0_29+i1_29)))))),(Implies(Not(And(And((i1_28<20), (v0_29<300)), (v0_29!=-1))),(And((v0_30==v0_29),(i1_29==i1_28))))))))
s.add((And((Implies(And(And((i1_29<20), (v0_30<300)), (v0_30!=-1)),(And((i1_30==(i1_29+1)),(v0_31==(v0_30+i1_30)))))),(Implies(Not(And(And((i1_29<20), (v0_30<300)), (v0_30!=-1))),(And((v0_31==v0_30),(i1_30==i1_29))))))))
s.add((And((Implies(And(And((i1_30<20), (v0_31<300)), (v0_31!=-1)),(And((i1_31==(i1_30+1)),(v0_32==(v0_31+i1_31)))))),(Implies(Not(And(And((i1_30<20), (v0_31<300)), (v0_31!=-1))),(And((v0_32==v0_31),(i1_31==i1_30))))))))
s.add((And((Implies(And(And((i1_31<20), (v0_32<300)), (v0_32!=-1)),(And((i1_32==(i1_31+1)),(v0_33==(v0_32+i1_32)))))),(Implies(Not(And(And((i1_31<20), (v0_32<300)), (v0_32!=-1))),(And((v0_33==v0_32),(i1_32==i1_31))))))))
s.add((And((Implies(And(And((i1_32<20), (v0_33<300)), (v0_33!=-1)),(And((i1_33==(i1_32+1)),(v0_34==(v0_33+i1_33)))))),(Implies(Not(And(And((i1_32<20), (v0_33<300)), (v0_33!=-1))),(And((v0_34==v0_33),(i1_33==i1_32))))))))
s.add((And((Implies(And((i1_33<30), (v0_34<300)),(And((i1_34==(i1_33+1)),(v0_35==(v0_34+i1_34)))))),(Implies(Not(And((i1_33<30), (v0_34<300))),(And((v0_35==v0_34),(i1_34==i1_33))))))))
s.add((And((Implies(And((i1_34<30), (v0_35<300)),(And((i1_35==(i1_34+1)),(v0_36==(v0_35+i1_35)))))),(Implies(Not(And((i1_34<30), (v0_35<300))),(And((v0_36==v0_35),(i1_35==i1_34))))))))
s.add((And((Implies(And((i1_35<30), (v0_36<300)),(And((i1_36==(i1_35+1)),(v0_37==(v0_36+i1_36)))))),(Implies(Not(And((i1_35<30), (v0_36<300))),(And((v0_37==v0_36),(i1_36==i1_35))))))))
s.add((And((Implies(And((i1_36<30), (v0_37<300)),(And((i1_37==(i1_36+1)),(v0_38==(v0_37+i1_37)))))),(Implies(Not(And((i1_36<30), (v0_37<300))),(And((v0_38==v0_37),(i1_37==i1_36))))))))
s.add((And((Implies(And((i1_37<30), (v0_38<300)),(And((i1_38==(i1_37+1)),(v0_39==(v0_38+i1_38)))))),(Implies(Not(And((i1_37<30), (v0_38<300))),(And((v0_39==v0_38),(i1_38==i1_37))))))))
s.add((And((Implies(And((i1_38<30), (v0_39<300)),(And((i1_39==(i1_38+1)),(v0_40==(v0_39+i1_39)))))),(Implies(Not(And((i1_38<30), (v0_39<300))),(And((v0_40==v0_39),(i1_39==i1_38))))))))
s.add((And((Implies(And((i1_39<30), (v0_40<300)),(And((i1_40==(i1_39+1)),(v0_41==(v0_40+i1_40)))))),(Implies(Not(And((i1_39<30), (v0_40<300))),(And((v0_41==v0_40),(i1_40==i1_39))))))))
s.add((And((Implies(And((i1_40<30), (v0_41<300)),(And((i1_41==(i1_40+1)),(v0_42==(v0_41+i1_41)))))),(Implies(Not(And((i1_40<30), (v0_41<300))),(And((v0_42==v0_41),(i1_41==i1_40))))))))
s.add((And((Implies(And((i1_41<30), (v0_42<300)),(And((i1_42==(i1_41+1)),(v0_43==(v0_42+i1_42)))))),(Implies(Not(And((i1_41<30), (v0_42<300))),(And((v0_43==v0_42),(i1_42==i1_41))))))))
s.add((And((Implies(And((i1_42<30), (v0_43<300)),(And((i1_43==(i1_42+1)),(v0_44==(v0_43+i1_43)))))),(Implies(Not(And((i1_42<30), (v0_43<300))),(And((v0_44==v0_43),(i1_43==i1_42))))))))
s.add((And((Implies(And((i1_43<30), (v0_44<300)),(And((i1_44==(i1_43+1)),(v0_45==(v0_44+i1_44)))))),(Implies(Not(And((i1_43<30), (v0_44<300))),(And((v0_45==v0_44),(i1_44==i1_43))))))))
s.add((And((Implies(And((i1_44<30), (v0_45<300)),(And((i1_45==(i1_44+1)),(v0_46==(v0_45+i1_45)))))),(Implies(Not(And((i1_44<30), (v0_45<300))),(And((v0_46==v0_45),(i1_45==i1_44))))))))
s.add((And((Implies(And((i1_45<30), (v0_46<300)),(And((i1_46==(i1_45+1)),(v0_47==(v0_46+i1_46)))))),(Implies(Not(And((i1_45<30), (v0_46<300))),(And((v0_47==v0_46),(i1_46==i1_45))))))))
s.add((And((Implies(And((i1_46<30), (v0_47<300)),(And((i1_47==(i1_46+1)),(v0_48==(v0_47+i1_47)))))),(Implies(Not(And((i1_46<30), (v0_47<300))),(And((v0_48==v0_47),(i1_47==i1_46))))))))
s.add((And((Implies(And((i1_47<30), (v0_48<300)),(And((i1_48==(i1_47+1)),(v0_49==(v0_48+i1_48)))))),(Implies(Not(And((i1_47<30), (v0_48<300))),(And((v0_49==v0_48),(i1_48==i1_47))))))))
s.add((And((Implies(And((i1_48<30), (v0_49<300)),(And((i1_49==(i1_48+1)),(v0_50==(v0_49+i1_49)))))),(Implies(Not(And((i1_48<30), (v0_49<300))),(And((v0_50==v0_49),(i1_49==i1_48))))))))
s.add((ppx0_1==ppx0_1))
s.add((ppx0_2==1))
s.add((ppx0_3==3))
s.add((ppx0_4==5))
s.add((ppy0_1==ppy0_1))
s.add((ppy0_2==5))
s.add((ppy0_3==6))
s.add((ppz0_1==ppz0_1))
s.add((ppz0_2==11))
s.add((ppy0_4==16))
s.add((ppz0_3==80))
s.add((ppy0_5==101))
s.add((ppy0_6==40400))
s.add((ppw0_1==ppw0_1))
s.add((ppw0_2==-1))
s.add((ppv0_1==ppv0_1))
s.add((ppv0_2==0))
s.add((ppv0_3==1))
s.add((ppv0_4==2))
s.add((ppv0_5==3))
s.add((ppv0_6==4))
s.add((ppv0_7==5))
s.add((ppv0_8==6))
s.add((ppv0_9==7))
s.add((ppv0_10==8))
s.add((ppv0_11==9))
s.add((ppv0_12==10))
s.add((ppv0_13==21))
s.add((ppv0_14==33))
s.add((ppv0_15==46))
s.add((ppv0_16==60))
s.add((ppv0_17==75))
s.add((ppv0_18==91))
s.add((ppv0_19==108))
s.add((ppv0_20==126))
s.add((ppv0_21==145))
s.add((ppv0_22==165))
s.add((ppv0_23==186))
s.add((ppv0_24==208))
s.add((ppv0_25==231))
s.add((ppv0_26==255))
s.add((ppv0_27==280))
s.add((ppv0_28==306))
s.add(Not(And((y0_6==ppy0_6),(z0_3==ppz0_3),(w0_4==ppw0_2),(v0_50==ppv0_28),(x0_3==ppx0_4))))
connectingVars = [('y0_6', 'ppy0_6'), ('z0_3', 'ppz0_3'), ('w0_4', 'ppw0_2'), ('v0_50', 'ppv0_28'), ('x0_3', 'ppx0_4')]
whileChecks = ['((i1_17<10) and (v0_18<300))', '(((i1_33<20) and (v0_34<300)) and (v0_34!=-1))', '((i1_49<30) and (v0_50<300))']

def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

if DEBUG_MODE:
    print ('SMT Expression: ')
    print (s.sexpr())

if s.check() == sat:
    # print ('sat')
    smtModel = s.model()
    if DEBUG_MODE:
        print (smtModel)

    smtModelDict = {}
    for index, item in enumerate(smtModel):
        smtModelDict[str(item)] = smtModel[item].as_long()

    for _, varTuple in enumerate(connectingVars):
        var, ppVar = varTuple[0], varTuple[1]
        varVal, ppVarVal = smtModelDict[var], smtModelDict[ppVar]
        if varVal != ppVarVal:
            print ('{}={} vs. {}={}'.format(var, varVal, ppVar, ppVarVal))

    # Check for under-unrolled
    for item in whileChecks:
        for smtVarName in [ x.strip() for x in re.split(OPERATOR_STR, item) if x.strip() != '']:
            if not representsInt(smtVarName) and smtVarName not in ['and', 'or', 'not']:
                item = item.replace(smtVarName, str(smtModelDict[smtVarName]))
        # If item is True, then we didn't unroll enough
        # return True so we can rerun
        if eval(item):
            # returncode 2 for need more unroll
            exit(2)
    
    # returncode 1 for sat
    exit(1)
    
else:
    # returncode 0 for unsat
    # print ('unsat')
    exit(0)
    