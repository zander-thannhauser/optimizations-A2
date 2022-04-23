.data

.text
.frame main, 12 
    loadI 0 => %vr1
    i2i %vr1 => %vr2
    loadI 5 => %vr3
    i2i %vr3 => %vr4
    loadI 3 => %vr5
    i2i %vr5 => %vr6
    loadI 3 => %vr5
    comp %vr4, %vr5 => %vr7
    testle %vr7 => %vr8
    cbr %vr8 -> .L0
    add %vr4, %vr6 => %vr9
    i2i %vr9 => %vr2
    jumpI -> .L1
.L0: nop
    add %vr4, %vr6 => %vr9
    i2i %vr9 => %vr2
.L1: nop
    add %vr4, %vr6 => %vr9
    i2i %vr9 => %vr2
    iwrite %vr2
    ret
