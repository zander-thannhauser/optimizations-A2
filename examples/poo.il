.data

.text
.frame pre_example, 8, %vr1, %vr2, %vr3
    loadI 0 => %vr4
    i2i %vr4 => %vr5
    loadI 0 => %vr4
    i2i %vr4 => %vr6
    loadI 20 => %vr7
    comp %vr5, %vr7 => %vr8
    testge %vr8 => %vr9
    cbr %vr9 -> .L1
.L0: nop
    loadI 20 => %vr7
    comp %vr6, %vr7 => %vr10
    testge %vr10 => %vr11
    cbr %vr11 -> .L3
.L2: nop
    add %vr1, %vr2 => %vr12
    i2i %vr12 => %vr3
    loadI 1 => %vr13
    add %vr6, %vr13 => %vr14
    i2i %vr14 => %vr6
    loadI 20 => %vr7
    comp %vr6, %vr7 => %vr10
    testge %vr10 => %vr11
    cbrne %vr11 -> .L2
.L3: nop
    loadI 1 => %vr13
    add %vr5, %vr13 => %vr15
    i2i %vr15 => %vr5
    loadI 20 => %vr7
    comp %vr5, %vr7 => %vr8
    testge %vr8 => %vr9
    cbrne %vr9 -> .L0
.L1: nop
    iwrite %vr3
    ret
.frame main, 0 
    loadI 3 => %vr16
    loadI 2 => %vr17
    loadI 0 => %vr4
    call pre_example, %vr16, %vr17, %vr4
    ret
